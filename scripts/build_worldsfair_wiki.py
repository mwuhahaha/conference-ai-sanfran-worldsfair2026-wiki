#!/usr/bin/env python3
"""Build an Obsidian-style wiki for AI Engineer World's Fair 2026.

Inputs are intentionally public:
- Official sessions/speakers JSON from ai.engineer.
- AI Engineer YouTube channel metadata gathered with yt-dlp.
- Caption availability metadata gathered with yt-dlp.
"""

from __future__ import annotations

import json
import re
import shutil
import textwrap
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TMP = Path("/tmp")


def load_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text())


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "untitled"


def day_to_date(day: str) -> str:
    if "June 28" in day or "Day 0" in day:
        return "2026-06-28"
    if "June 29" in day or "Day 1" in day:
        return "2026-06-29"
    if "June 30" in day or "Day 2" in day:
        return "2026-06-30"
    if "July 1" in day or "Day 3" in day:
        return "2026-07-01"
    if "July 2" in day or "Day 4" in day:
        return "2026-07-02"
    return "2026-06-29"


def yaml_list(items) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(json.dumps(str(item), ensure_ascii=False) for item in items) + "]"


def frontmatter(fields: dict) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}: {yaml_list(value)}")
        elif value is None:
            continue
        else:
            text = str(value).replace("\n", " ").strip()
            lines.append(f"{key}: {json.dumps(text, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n")


def link_for(category: str, title: str) -> str:
    return f"[[{slugify(title)}]]"


def md_label(value: str) -> str:
    return str(value or "").replace("[", "(").replace("]", ")").replace("|", "/")


def caption_label(status: dict | None) -> str:
    if not status:
        return "unknown"
    if status.get("has_manual_en_subtitles"):
        return "manual English subtitles"
    if status.get("has_auto_en_captions"):
        return "English auto-captions"
    if status.get("ok"):
        return "no English captions detected"
    return "metadata unavailable"


def cached_transcript_note(video_id: str) -> str:
    transcript_path = ROOT / "raw" / "sources" / "youtube-transcripts" / f"{video_id}.txt"
    if not transcript_path.exists():
        return "Not fetched yet."
    word_count = len(transcript_path.read_text(errors="ignore").split())
    return f"Cached at `raw/sources/youtube-transcripts/{video_id}.txt` ({word_count:,} words)."


def load_company_profiles() -> dict:
    """Load curated public company context keyed by company slug."""
    return load_json(ROOT / "raw" / "sources" / "company-profiles.json", {})


def related_transcript_status(video: dict, status: dict | None) -> str:
    return (
        f"Related video transcript availability: {caption_label(status)}. "
        "Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. "
        f"{cached_transcript_note(video.get('video_id', ''))}"
    )


def profile_link_lines(speaker: dict) -> list[str]:
    links = []
    if speaker.get("linkedin"):
        links.append(f"- [LinkedIn]({speaker.get('linkedin')})")
    if speaker.get("twitter"):
        links.append(f"- [X / Twitter]({speaker.get('twitter')})")
    if speaker.get("website"):
        links.append(f"- [Website]({speaker.get('website')})")
    if speaker.get("blog"):
        links.append(f"- [Blog]({speaker.get('blog')})")
    return links


def best_related(session_title: str, related_by_title: dict) -> dict | None:
    matches = related_by_title.get(session_title) or []
    for candidate in matches:
        video = candidate.get("related_video") or {}
        if video.get("speaker_hit"):
            return video
    return matches[0].get("related_video") if matches else None


def copy_source(path: Path, dest_name: str) -> None:
    if path.exists():
        dest = ROOT / "raw" / "sources" / dest_name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, dest)


def main() -> int:
    sessions_blob = load_json(TMP / "aiewf2026-sessions.json", {})
    speakers_blob = load_json(TMP / "aiewf2026-speakers.json", {})
    sessions = sessions_blob.get("sessions", [])
    speakers = speakers_blob.get("speakers", [])
    related = load_json(TMP / "aiewf2026-speaker-video-map.json", [])
    caption_status = load_json(TMP / "aiewf2026-related-video-caption-status.json", {})
    assign_talk_slugs(sessions)

    for directory in [
        "wiki/events",
        "wiki/talks",
        "wiki/people",
        "wiki/companies",
        "wiki/resources",
        "wiki/topics",
        "raw/sources",
        ".ops/state/runs",
    ]:
        (ROOT / directory).mkdir(parents=True, exist_ok=True)

    copy_source(TMP / "aiewf2026-sessions.json", "official-sessions.json")
    copy_source(TMP / "aiewf2026-speakers.json", "official-speakers.json")
    copy_source(TMP / "aiewf2026-speaker-video-map.json", "speaker-video-map.json")
    copy_source(TMP / "aiewf2026-related-video-caption-status.json", "related-video-caption-status.json")

    related_by_title = defaultdict(list)
    for item in related:
        related_by_title[item.get("title", "")].append(item)

    speaker_by_name = {speaker.get("name"): speaker for speaker in speakers if speaker.get("name")}
    sessions_by_speaker = defaultdict(list)
    for session in sessions:
        for speaker in session.get("speakers", []):
            sessions_by_speaker[speaker].append(session)

    # Conference event/day pages.
    days = [
        ("2026-06-28", "New Engineer Orientation"),
        ("2026-06-29", "Workshop Day and Welcome Reception"),
        ("2026-06-30", "Keynotes and Breakouts"),
        ("2026-07-01", "World Cup and Multi-Track Programming"),
        ("2026-07-02", "Final Day and Last Chance Expo"),
    ]
    for date, title in days:
        day_sessions = [s for s in sessions if day_to_date(s.get("day", "")) == date]
        body = [
            frontmatter({"title": title, "category": "events", "date": date, "type": "conference-day", "source": "Official schedule"}),
            f"# {title}",
            "",
            "## What It Was",
            f"Official AI Engineer World's Fair 2026 programming day at Moscone West in San Francisco. This page is generated from the official schedule data.",
            "",
            "## Scheduled Sessions",
        ]
        for session in day_sessions[:120]:
            body.append(f"- [[{talk_slug(session)}]] — {session.get('time', 'time TBD')} · {session.get('track') or session.get('room') or 'track TBD'}")
        write(ROOT / "wiki" / "events" / f"{date}-{slugify(title)}.md", "\n".join(body))

    # Talk pages.
    talk_paths = []
    for session in sessions:
        date = day_to_date(session.get("day", ""))
        slug = talk_slug(session)
        video = best_related(session.get("title", ""), related_by_title)
        status = caption_status.get(video.get("video_id")) if video else None
        speakers_text = ", ".join(session.get("speakers", [])) or "TBA"
        related_line = "No related AI Engineer channel video found yet."
        if video:
            related_line = (
                f"[{md_label(video.get('youtube_title'))}]({video.get('youtube_url')}) "
                f"({video.get('relationship', 'related video')}; captions: {caption_label(status)})."
            )
        desc = session.get("description") or "No official description published in the schedule data."
        desc = "\n\n".join(textwrap.wrap(desc.replace("\n", " "), width=100)) if desc else desc
        body = [
            frontmatter(
                {
                    "title": session.get("title"),
                    "category": "talks",
                    "date": date,
                    "time": session.get("time"),
                    "track": session.get("track") or session.get("room"),
                    "room": session.get("room"),
                    "scheduleTrack": session.get("track"),
                    "scheduleRoom": session.get("room"),
                    "scheduleLabels": schedule_labels(session),
                    "speakers": session.get("speakers", []),
                    "sourceLabels": ["Official conference schedule", "Public YouTube metadata"],
                }
            ),
            f"# {session.get('title')}",
            "",
            "## Official Schedule Context",
            f"- Date/time: {date} · {session.get('time', 'time TBD')}",
            f"- Track/room: {session.get('track') or 'track TBD'} · {session.get('room') or 'room TBD'}",
            f"- Speaker(s): {speakers_text}",
            f"- Session type/status: {session.get('type', 'unknown')} · {session.get('status', 'unknown')}",
            "",
            "## Schedule Labels",
            f"- Track: {session.get('track') or 'track TBD'}",
            f"- Room: {session.get('room') or 'room TBD'}",
            f"- Session type: {session.get('type', 'unknown')}",
            f"- Status: {session.get('status', 'unknown')}",
            "",
            "## Official Description",
            desc,
            "",
            "## Related YouTube Video",
            related_line,
            "",
            "## Transcript Status",
            "No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run."
            if not video
            else related_transcript_status(video, status),
            "",
            "## People",
        ]
        for speaker in session.get("speakers", []):
            body.append(f"- [[{slugify(speaker)}]]")
        body.extend(["", "## Notes", "- Pending transcript synthesis when an official recording or confirmed matching video is available."])
        path = ROOT / "wiki" / "talks" / f"{slug}.md"
        write(path, "\n".join(body))
        talk_paths.append(path)

    # People pages.
    all_speaker_names = sorted(set(speaker_by_name) | set(sessions_by_speaker))
    for name in all_speaker_names:
        if not name:
            continue
        speaker = speaker_by_name.get(name, {"name": name})
        person_sessions = sessions_by_speaker.get(name, [])
        body = [
            frontmatter(
                {
                    "title": name,
                    "category": "people",
                    "role": speaker.get("role"),
                    "company": speaker.get("company"),
                    "linkedin": speaker.get("linkedin"),
                    "twitter": speaker.get("twitter"),
                    "website": speaker.get("website"),
                    "blog": speaker.get("blog"),
                    "sourceLabels": ["Official speaker roster", "Official conference schedule"],
                }
            ),
            f"# {name}",
            "",
            "## Official Role",
            f"{speaker.get('role') or 'Role not listed'} at {speaker.get('company') or 'company not listed'}.",
            "",
            "## Profile Links",
            *(profile_link_lines(speaker) or ["No public profile links listed in the official speaker roster."]),
            "",
            "## Official Bio",
            speaker.get("bio") or "No official bio included in the speaker JSON.",
            "",
            "## Scheduled Sessions",
        ]
        for session in person_sessions:
            body.append(f"- [[{talk_slug(session)}]] — {session.get('title')} ({day_to_date(session.get('day', ''))}, {session.get('time')})")
        write(ROOT / "wiki" / "people" / f"{slugify(name)}.md", "\n".join(body))

    # Company pages.
    company_people = defaultdict(list)
    for speaker in speakers:
        if speaker.get("company"):
            company_people[speaker["company"]].append(speaker)
    company_pages = build_company_pages(company_people, sessions_by_speaker, load_company_profiles())
    for company_slug, company_page in sorted(company_pages.items()):
        company = company_page["title"]
        aliases = company_page["aliases"]
        people = company_page["people"]
        related_sessions = company_page["sessions"]
        profile = company_page.get("profile") or {}
        source_labels = unique_list(["Official speaker roster", "Official conference schedule", *profile.get("sourceLabels", [])])
        body = [
            frontmatter(
                {
                    "title": company,
                    "category": "companies",
                    "aliases": aliases,
                    "website": profile.get("website"),
                    "sourceLabels": source_labels,
                }
            ),
            f"# {company}",
            "",
            "## What It Is",
            profile.get("summary")
            or "No public company profile has been added yet. This page is grounded in the official speaker roster and schedule context until a relevant company site, product page, or public profile is reviewed.",
            "",
            "## Why It Matters At World's Fair",
            company_importance_text(company, people, related_sessions, profile),
            "",
            "## Related People",
        ]
        for person in sorted(people, key=lambda p: p.get("name", "")):
            body.append(f"- [[{slugify(person.get('name', ''))}]] — {person.get('role') or 'role not listed'}")
        body.extend(["", "## Related Scheduled Sessions"])
        if related_sessions:
            for session in sorted(related_sessions, key=lambda s: (day_to_date(s.get("day", "")), s.get("time", ""), s.get("title", ""))):
                body.append(
                    f"- [[{talk_slug(session)}]] — {session.get('title')} ({day_to_date(session.get('day', ''))}, {session.get('time') or 'time TBD'})"
                )
        else:
            body.append("- No related scheduled sessions were found from the official schedule data.")
        if profile.get("origin"):
            body.extend(["", "## Origin And Context", profile["origin"]])
        if profile.get("notes"):
            body.extend(["", "## Notes"])
            for note in profile["notes"]:
                body.append(f"- {note}")
        body.extend(["", "## Public Sources"])
        links = profile.get("sourceLinks") or []
        if links:
            for link in links:
                body.append(f"- [{md_label(link.get('label') or link.get('url'))}]({link.get('url')})")
        else:
            body.append("- No public company/profile source links have been added yet.")
        body.extend(
            [
                "",
                "## Evidence Boundary",
                "Official roster and schedule facts are treated as canonical for conference participation. Public company sites, documentation, and professional profiles are supporting context used to explain what the organization does and why it is relevant.",
            ]
        )
        write(ROOT / "wiki" / "companies" / f"{company_slug}.md", "\n".join(body))

    # Video resources.
    videos = {}
    linked_sessions = defaultdict(list)
    for item in related:
        video = item.get("related_video") or {}
        vid = video.get("video_id")
        if not vid:
            continue
        videos[vid] = video
        linked_sessions[vid].append(item)
    for vid, video in videos.items():
        status = caption_status.get(vid)
        body = [
            frontmatter({"title": video.get("youtube_title"), "category": "resources", "sourceLabels": ["Public YouTube metadata"]}),
            f"# {video.get('youtube_title')}",
            "",
            "## What It Is",
            "A public AI Engineer YouTube video matched as supporting context for one or more World's Fair 2026 scheduled sessions, usually because the scheduled speaker appears in the video title. Official World's Fair San Francisco 2026 livestreams and cut videos should be reclassified as primary event video sources when imported.",
            "",
            "## Transcript Availability",
            caption_label(status),
            "",
            "## Cached Transcript",
            cached_transcript_note(vid),
            "",
            "## Link",
            f"[YouTube]({video.get('youtube_url')})",
            "",
            "## Related Scheduled Sessions",
        ]
        for session in linked_sessions[vid][:20]:
            body.append(f"- [[{talk_slug(session)}]] — {session.get('title')}")
        write(ROOT / "wiki" / "resources" / f"youtube-{vid}.md", "\n".join(body))

    # Complete talk-video map.
    map_lines = [
        frontmatter({"title": "Talk Video Transcript Map", "category": "resources", "sourceLabels": ["Official conference schedule", "Public YouTube metadata"]}),
        "# Talk Video Transcript Map",
        "",
        "This table starts from the official AI Engineer World's Fair 2026 schedule. Exact session-recording matches on the AI Engineer YouTube channel were not found by normalized title during this run, so related videos are labeled as supporting context.",
        "",
        "| Date | Time | Track | Talk | Speakers | Related video | Transcript status |",
        "|---|---:|---|---|---|---|---|",
    ]
    for session in sessions:
        video = best_related(session.get("title", ""), related_by_title)
        status = caption_status.get(video.get("video_id")) if video else None
        video_cell = "None found"
        if video:
            video_cell = f"[{md_label(video.get('youtube_title'))}]({video.get('youtube_url')})"
        map_lines.append(
            "| "
            + " | ".join(
                [
                    day_to_date(session.get("day", "")),
                    session.get("time", ""),
                    (session.get("track") or session.get("room") or "").replace("|", "/"),
                    f"[[{talk_slug(session)}|{session.get('title', '').replace('|', '/') }]]",
                    ", ".join(session.get("speakers", [])).replace("|", "/"),
                    video_cell.replace("|", "/"),
                    caption_label(status),
                ]
            )
            + " |"
        )
    write(ROOT / "wiki" / "resources" / "talk-video-transcript-map.md", "\n".join(map_lines))

    write_resource_pages(sessions, speakers, len(videos))
    write_indexes(sessions, speakers, company_pages, videos)
    write_registries(sessions, speakers, company_pages, videos)
    write_receipt(sessions, speakers, company_pages, videos)
    return 0


def talk_slug(session: dict) -> str:
    if session.get("_slug"):
        return session["_slug"]
    date = day_to_date(session.get("day", ""))
    speaker = (session.get("speakers") or ["session"])[0]
    return f"{date}-{slugify(speaker)}-{slugify(session.get('title', 'session'))}"[:180].rstrip("-")


def assign_talk_slugs(sessions: list[dict]) -> None:
    used = set()
    for index, session in enumerate(sessions, start=1):
        date = day_to_date(session.get("day", ""))
        speaker = (session.get("speakers") or ["session"])[0]
        base = f"{date}-{slugify(speaker)}-{slugify(session.get('title', 'session'))}"[:150].rstrip("-")
        disambiguator = slugify(f"{session.get('time', '')}-{session.get('room', '')}-{index}")[:40]
        candidate = base
        if candidate in used:
            candidate = f"{base}-{disambiguator}"[:190].rstrip("-")
        suffix = 2
        while candidate in used:
            candidate = f"{base}-{disambiguator}-{suffix}"[:195].rstrip("-")
            suffix += 1
        used.add(candidate)
        session["_slug"] = candidate


def schedule_labels(session: dict) -> list[str]:
    return [
        label
        for label in [
            session.get("track"),
            session.get("room"),
            session.get("type"),
            session.get("status"),
        ]
        if label
    ]


def unique_list(items) -> list:
    seen = set()
    values = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            values.append(item)
    return values


def build_company_pages(company_people: dict, sessions_by_speaker: dict | None = None, profiles: dict | None = None) -> dict:
    sessions_by_speaker = sessions_by_speaker or {}
    profiles = profiles or {}
    grouped = defaultdict(lambda: {"aliases": [], "people": []})
    for company, people in company_people.items():
        company_slug = slugify(company)
        grouped[company_slug]["aliases"].append(company)
        grouped[company_slug]["people"].extend(people)
    pages = {}
    for company_slug, data in grouped.items():
        aliases = sorted(set(data["aliases"]))
        people_by_name = {person.get("name"): person for person in data["people"] if person.get("name")}
        sessions_by_slug = {}
        for person in people_by_name.values():
            for session in sessions_by_speaker.get(person.get("name"), []):
                sessions_by_slug[talk_slug(session)] = session
            for session in person.get("sessions") or []:
                sessions_by_slug[talk_slug(session)] = session
        pages[company_slug] = {
            "title": aliases[0],
            "aliases": aliases,
            "people": list(people_by_name.values()),
            "sessions": list(sessions_by_slug.values()),
            "profile": profiles.get(company_slug, {}),
        }
    return pages


def company_importance_text(company: str, people: list[dict], sessions: list[dict], profile: dict) -> str:
    if profile.get("why_it_matters"):
        return profile["why_it_matters"]
    people_count = len(people)
    session_count = len(sessions)
    if session_count:
        session_titles = "; ".join(session.get("title", "Untitled session") for session in sessions[:3])
        return (
            f"{company} appears through {people_count} official speaker(s) connected to {session_count} scheduled session(s). "
            f"Those sessions make the organization relevant to the conference knowledge graph around: {session_titles}."
        )
    return (
        f"{company} appears through {people_count} official speaker(s) in the AI Engineer World's Fair 2026 roster. "
        "Add a public company profile when a relevant company site or professional source is reviewed."
    )


def write_resource_pages(sessions, speakers, video_count):
    resources = {
        "official-conference-site": ("Official Conference Site", "https://www.ai.engineer/worldsfair/2026"),
        "official-sessions-json": ("Official Sessions JSON", "https://www.ai.engineer/worldsfair/sessions.json"),
        "official-speakers-json": ("Official Speakers JSON", "https://www.ai.engineer/worldsfair/speakers.json"),
        "ai-engineer-youtube-channel": ("AI Engineer YouTube Channel", "https://www.youtube.com/@aiDotEngineer"),
    }
    for slug, (title, url) in resources.items():
        write(
            ROOT / "wiki" / "resources" / f"{slug}.md",
            "\n".join(
                [
                    frontmatter({"title": title, "category": "resources", "sourceLabels": ["Public source"]}),
                    f"# {title}",
                    "",
                    "## What It Is",
                    "A public source used to build the AI Engineer World's Fair 2026 wiki.",
                    "",
                    "## Link",
                    f"[{url}]({url})",
                ]
            ),
        )
    write(
        ROOT / "wiki" / "resources" / "source-boundary.md",
        "\n".join(
            [
                frontmatter({"title": "Source Boundary", "category": "resources"}),
                "# Source Boundary",
                "",
                "Allowed sources for this run:",
                "- Official AI Engineer World's Fair 2026 schedule endpoints.",
                "- Public AI Engineer YouTube channel metadata, with official World's Fair San Francisco 2026 videos treated as primary event video sources for media/transcript/slide evidence.",
                "- Public YouTube caption availability metadata.",
                "",
                "The run did not import private Miami notes, personal recordings, queue state, or diary content.",
                "",
                f"Current generated scale: {len(sessions)} sessions, {len(speakers)} speakers, {video_count} related YouTube resources.",
            ]
        ),
    )


def write_indexes(sessions, speakers, company_people, videos):
    all_people_count = len({speaker.get("name", "") for speaker in speakers if speaker.get("name")} | {name for session in sessions for name in session.get("speakers", []) if name})
    write(
        ROOT / "wiki" / "overview.md",
        "\n".join(
            [
                "# AI Engineer World's Fair 2026 Wiki Overview",
                "",
                "AI Engineer World's Fair 2026 runs June 28-July 2, 2026 in San Francisco, with main programming at Moscone West.",
                "",
                "This wiki is currently an official-schedule-first scaffold. It records every public schedule session, every official speaker entry, organizations from the official speaker roster, and AI Engineer YouTube videos that are related by speaker match.",
                "",
                "## Current Status",
                f"- {len(sessions)} official schedule sessions generated as talk pages.",
                f"- {all_people_count} people pages generated from the official speaker roster plus schedule-only speaker names.",
                f"- {len(company_people)} company pages generated from speaker affiliations.",
                f"- {len(videos)} related YouTube video resource pages generated.",
                "- Exact YouTube title matches for official session recordings were not found during this run.",
                "",
                "## Next Synthesis Pass",
                "Prioritize confirmed captions for speaker-matched videos, then update the relevant talk pages with transcript-derived themes. Keep external, historical, or non-event videos labeled as supporting context; official World's Fair San Francisco 2026 videos are primary event video sources for transcript and slide evidence.",
            ]
        ),
    )
    index = [
        "# AI Engineer World's Fair 2026 Index",
        "",
        "## Core Resources",
        "- [[overview]]",
        "- [[talk-video-transcript-map]]",
        "- [[official-conference-site]]",
        "- [[official-sessions-json]]",
        "- [[official-speakers-json]]",
        "",
        "## Talks",
    ]
    for session in sessions:
        index.append(f"- [[{talk_slug(session)}]] — {session.get('title')}")
    index.extend(["", "## People"])
    for speaker in speakers:
        if speaker.get("name"):
            index.append(f"- [[{slugify(speaker['name'])}]]")
    write(ROOT / "wiki" / "index.md", "\n".join(index))
    write(ROOT / "wiki" / "quotes.md", "# Quotes\n\nNo transcript quotes have been promoted yet.\n")
    write(
        ROOT / "wiki" / "log.md",
        f"# Log\n\n- {datetime.now(timezone.utc).isoformat()} — Generated official schedule scaffold and related YouTube transcript map for AI Engineer World's Fair 2026.\n",
    )


def write_registries(sessions, speakers, company_people, videos):
    all_people = sorted({speaker.get("name", "") for speaker in speakers if speaker.get("name")} | {name for session in sessions for name in session.get("speakers", []) if name})
    registries = {
        "talks": [
            {"id": talk_slug(session), "title": session.get("title"), "path": f"wiki/talks/{talk_slug(session)}.md"}
            for session in sessions
        ],
        "people": [
            {"id": slugify(name), "title": name, "path": f"wiki/people/{slugify(name)}.md"}
            for name in all_people
        ],
        "companies": [
            {"id": company_slug, "title": page["title"], "path": f"wiki/companies/{company_slug}.md"}
            for company_slug, page in sorted(company_people.items())
        ],
        "resources": [
            {"id": f"youtube-{vid}", "title": video.get("youtube_title"), "path": f"wiki/resources/youtube-{vid}.md"}
            for vid, video in sorted(videos.items())
        ]
        + [
            {"id": "talk-video-transcript-map", "title": "Talk Video Transcript Map", "path": "wiki/resources/talk-video-transcript-map.md"},
            {"id": "official-conference-site", "title": "Official Conference Site", "path": "wiki/resources/official-conference-site.md"},
            {"id": "official-sessions-json", "title": "Official Sessions JSON", "path": "wiki/resources/official-sessions-json.md"},
            {"id": "official-speakers-json", "title": "Official Speakers JSON", "path": "wiki/resources/official-speakers-json.md"},
            {"id": "ai-engineer-youtube-channel", "title": "AI Engineer YouTube Channel", "path": "wiki/resources/ai-engineer-youtube-channel.md"},
            {"id": "source-boundary", "title": "Source Boundary", "path": "wiki/resources/source-boundary.md"},
        ],
        "events": [
            {"id": "2026-06-28-new-engineer-orientation", "title": "New Engineer Orientation", "path": "wiki/events/2026-06-28-new-engineer-orientation.md"},
            {"id": "2026-06-29-workshop-day-and-welcome-reception", "title": "Workshop Day and Welcome Reception", "path": "wiki/events/2026-06-29-workshop-day-and-welcome-reception.md"},
            {"id": "2026-06-30-keynotes-and-breakouts", "title": "Keynotes and Breakouts", "path": "wiki/events/2026-06-30-keynotes-and-breakouts.md"},
            {"id": "2026-07-01-world-cup-and-multi-track-programming", "title": "World Cup and Multi-Track Programming", "path": "wiki/events/2026-07-01-world-cup-and-multi-track-programming.md"},
            {"id": "2026-07-02-final-day-and-last-chance-expo", "title": "Final Day and Last Chance Expo", "path": "wiki/events/2026-07-02-final-day-and-last-chance-expo.md"},
        ],
    }
    for category, rows in registries.items():
        write(ROOT / "wiki" / category / "registry.json", json.dumps(rows, indent=2, ensure_ascii=False))


def write_receipt(sessions, speakers, company_people, videos):
    now = datetime.now(timezone.utc).isoformat()
    all_people_count = len({speaker.get("name", "") for speaker in speakers if speaker.get("name")} | {name for session in sessions for name in session.get("speakers", []) if name})
    write(
        ROOT / ".ops" / "state" / "runs" / "worldsfair-public-schedule-build-2026-07-02.md",
        "\n".join(
            [
                "---",
                "type: run-receipt",
                "scope: project-local",
                "status: generated",
                f"updated: {now}",
                "---",
                "",
                "# Worldsfair Public Schedule Build 2026-07-02",
                "",
                "## Inputs",
                "- https://www.ai.engineer/worldsfair/2026",
                "- https://www.ai.engineer/worldsfair/sessions.json",
                "- https://www.ai.engineer/worldsfair/speakers.json",
                "- https://www.youtube.com/@aiDotEngineer",
                "",
                "## Output",
                f"- {len(sessions)} talk/session pages",
                f"- {all_people_count} people pages",
                f"- {len(company_people)} company pages",
                f"- {len(videos)} related YouTube resource pages",
                "- Complete talk-video-transcript map",
                "",
                "## Boundary",
                "No private vault content was used as source material.",
            ]
        ),
    )
    write(
        ROOT / ".ops" / "state" / "current.md",
        "\n".join(
            [
                "---",
                "type: orchestration-current",
                "scope: project-local",
                "status: active",
                f"updated: {now}",
                "---",
                "",
                "# AI Engineer World's Fair 2026 Project State",
                "",
                "Current wiki is an official-schedule-first scaffold with related YouTube video/caption metadata.",
                "",
                "Next step: synthesize transcript-backed pages for speaker-matched YouTube videos with confirmed English captions, and revise talk pages when exact session recordings become available.",
            ]
        ),
    )


if __name__ == "__main__":
    raise SystemExit(main())
