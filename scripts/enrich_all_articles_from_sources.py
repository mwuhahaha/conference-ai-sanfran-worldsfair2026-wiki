#!/usr/bin/env python3
"""General source-backed enrichment for wiki articles.

Every article is eligible for source-derived evidence from schedule pages,
linked videos, transcripts, and slide material. Generated article text uses
neutral source/evidence language.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

try:
    import process_slide_corpus_ai as slide_corpus
    import quarantine_stale_slide_ai as slide_quarantine
except ModuleNotFoundError:  # Imported as scripts.enrich_all_articles_from_sources.
    from scripts import process_slide_corpus_ai as slide_corpus
    from scripts import quarantine_stale_slide_ai as slide_quarantine


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
WORDLIST_PATHS = [
    Path("/usr/share/dict/words"),
    Path("/usr/share/dict/american-english"),
]

TRANSCRIPT_DIRS = [
    RAW / "youtube-transcripts",
    RAW / "external-youtube-transcripts",
    RAW / "youtube-livestream-transcripts",
]
OFFICIAL_VIDEO_MANIFEST = RAW / "official-wf26-video-manifest.json"
PRIVATE_POLICY_PROFILE = (
    ROOT / ".ops" / "state" / "cache" / "wiki-maker" / "private-policy.json"
)
PRIVATE_CREDIBILITY_V2_POLICY = (
    ROOT
    / ".ops"
    / "state"
    / "cache"
    / "wiki-maker"
    / "credibility-v2"
    / "writing-policy.json"
)
TALK_GENERATED_SOURCE_HEADINGS = (
    "Evidence Graph",
    "Media Evidence",
    "Transcript Markdown",
    "Slides",
    "Synthesis",
)
TOPIC_GENERATED_SOURCE_HEADINGS = (
    "Evidence Graph",
    "Livestream Source",
    "Slide-Derived Scheduled Session Signals",
    "Slide-Derived Supporting Decks",
    "Source Coverage",
)

STOPWORDS = {
    "about", "actually", "after", "again", "agent", "agents", "all", "also", "because", "basically",
    "being", "build", "building", "could", "different", "every", "example", "from", "going", "have",
    "good", "here", "in", "into", "just", "kind", "know", "like", "make", "more", "much", "need",
    "needs", "only", "other", "people", "really", "right", "same", "slide", "slides", "some",
    "something", "sort", "talk", "that", "their", "there", "these", "them", "then", "they", "thing",
    "things", "think", "this", "those", "through", "time", "using", "very", "video", "videos",
    "want", "were", "what", "when", "where", "which", "will", "with", "work", "would", "yeah",
    "you", "your",
}
RELEVANCE_STOPWORDS = STOPWORDS | {
    "agentic", "and", "any", "are", "before", "better", "building",
    "but", "can", "cannot", "category", "code", "conference", "context",
    "data", "derived", "engineering", "for", "general", "has", "llm",
    "made", "model", "models", "not", "one", "out", "over", "overview",
    "production", "should", "significance", "sourcelabels", "support",
    "supporting", "system", "systems", "the", "title", "tool", "tools",
    "topics", "training", "use", "user", "useful", "without", "world",
}
TITLE_RELEVANCE_STOPWORDS = STOPWORDS | {
    "agentic", "engineering", "general", "system", "systems",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_words() -> set[str]:
    for path in WORDLIST_PATHS:
        if path.exists():
            return {
                word.strip().lower()
                for word in read(path).splitlines()
                if word.strip().isalpha() and len(word.strip()) >= 3
            }
    return set()


ENGLISH_WORDS = load_words()


def split_frontmatter(text: str) -> tuple[str, str, dict[str, str]]:
    if not text.startswith("---\n"):
        return "", text, {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text, {}
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return text[: end + 5], text[end + 5 :].lstrip(), fields


def title_of(path: Path) -> str:
    text = read(path)
    _fm, body, fields = split_frontmatter(text)
    if fields.get("title"):
        return fields["title"]
    match = re.search(r"^#\s+(.+)$", body, re.M)
    return match.group(1).strip() if match else path.stem.replace("-", " ").title()


def upsert_section(markdown: str, heading: str, body: str) -> str:
    fm, content, _fields = split_frontmatter(markdown)
    replacement = f"## {heading}\n{body.strip()}\n"
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    if pattern.search(content):
        content = pattern.sub(lambda _match: replacement, content).rstrip() + "\n"
    else:
        content = content.rstrip() + "\n\n" + replacement
    return fm + content


def remove_section(markdown: str, heading: str) -> str:
    fm, content, _fields = split_frontmatter(markdown)
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    content = pattern.sub("", content).rstrip() + "\n"
    return fm + content.lstrip()


def source_text_for_enrichment(
    markdown: str,
    generated_headings: tuple[str, ...] = ("Evidence Graph",),
) -> str:
    """Exclude prior generated sections so stale sources cannot self-perpetuate."""

    for heading in generated_headings:
        markdown = remove_section(markdown, heading)
    return markdown


def remove_pending_transcript_note(markdown: str) -> str:
    """Drop the original schedule-only placeholder once richer evidence exists."""
    fm, content, _fields = split_frontmatter(markdown)
    pattern = re.compile(r"^## Notes\n(.*?)(?=^## |\Z)", re.M | re.S)
    match = pattern.search(content)
    if not match:
        return markdown
    lines = [
        line
        for line in match.group(1).splitlines()
        if "Pending transcript synthesis when an official recording or confirmed matching video is available." not in line
    ]
    body = "\n".join(line for line in lines if line.strip()).strip()
    replacement = f"## Notes\n{body}\n" if body else ""
    content = pattern.sub(replacement, content).rstrip() + "\n"
    return fm + content.lstrip()


def video_ids(text: str) -> list[str]:
    ids = set(re.findall(r"(?:watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})", text))
    ids.update(re.findall(r"youtube-([A-Za-z0-9_-]{11})(?=[\]\)\s/#-]|$)", text))
    return sorted(video_id for video_id in ids if has_video_evidence(video_id))


def has_video_evidence(video_id: str) -> bool:
    if (WIKI / "resources" / f"youtube-{video_id}.md").exists():
        return True
    if any((folder / f"{video_id}.txt").exists() for folder in TRANSCRIPT_DIRS):
        return True
    return any((WIKI / "slides" / f"youtube-{video_id}-{suffix}.md").exists() for suffix in ["slides", "dense-slides", "reconstructed-slides"])


@lru_cache(maxsize=1)
def official_video_manifest() -> dict[str, dict]:
    if not OFFICIAL_VIDEO_MANIFEST.is_file():
        return {}
    payload = json.loads(read(OFFICIAL_VIDEO_MANIFEST))
    videos = payload.get("videos", [])
    if not isinstance(videos, list):
        raise ValueError("official WF26 video manifest must contain a videos array")
    return {
        str(item["id"]): item
        for item in videos
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }


@lru_cache(maxsize=1)
def official_event_video_ids() -> frozenset[str]:
    return frozenset(official_video_manifest())


def official_recording_ids_for_talk(talk_slug: str) -> list[str]:
    rows = []
    for video_id, item in official_video_manifest().items():
        if item.get("mediaType") != "talk_recording":
            continue
        matched_talks = item.get("matchedTalks")
        if isinstance(matched_talks, list) and talk_slug in matched_talks:
            rows.append(video_id)
    return rows


def talk_evidence_video_ids(talk_slug: str, markdown: str) -> list[str]:
    """Select exact event recordings plus explicitly linked supporting media."""

    exact = official_recording_ids_for_talk(talk_slug)
    manifest_ids = official_event_video_ids()
    supporting = [
        video_id
        for video_id in video_ids(markdown)
        if video_id not in manifest_ids
    ]
    return list(dict.fromkeys([*exact, *supporting]))


def strip_unmatched_event_media(markdown: str, talk_slug: str) -> str:
    """Remove generated media blocks for official event videos matched elsewhere."""

    exact = set(official_recording_ids_for_talk(talk_slug))
    excluded = set(official_event_video_ids()) - exact
    if not excluded:
        return markdown

    def filter_section(heading: str, text: str) -> str:
        fm, content, _fields = split_frontmatter(text)
        pattern = re.compile(
            rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)",
            re.M | re.S,
        )
        match = pattern.search(content)
        if match is None:
            return text
        lines: list[str] = []
        skipping_block = False
        for line in match.group(1).splitlines():
            source_match = re.match(
                r"^- Source video: `youtube-([A-Za-z0-9_-]{11})`\s*$",
                line,
            )
            if source_match:
                skipping_block = source_match.group(1) in excluded
                if skipping_block:
                    continue
            if skipping_block:
                continue
            if any(f"youtube-{video_id}-transcript" in line for video_id in excluded):
                continue
            lines.append(line)
        body = "\n".join(lines).strip()
        if body:
            replacement = f"## {heading}\n{body}\n"
        else:
            replacement = ""
        content = content[: match.start()] + replacement + content[match.end() :]
        return fm + content.lstrip().rstrip() + "\n"

    cleaned = filter_section("Media Evidence", markdown)
    return filter_section("Transcript Markdown", cleaned)


def ensure_talk_media_evidence(
    markdown: str,
    talk_slug: str,
    selected_video_ids: list[str],
) -> str:
    """Rebuild the required talk evidence section from selected sources."""

    exact = set(official_recording_ids_for_talk(talk_slug))
    lines = []
    for video_id in selected_video_ids:
        if video_id in exact:
            lines.append(
                f"- [[youtube-{video_id}]] - dedicated official event recording."
            )
            transcript_path, _transcript = transcript_text(video_id)
            if transcript_path is not None:
                lines.append(
                    f"- [[youtube-{video_id}-transcript]] - dedicated official "
                    "recording transcript."
                )
        else:
            lines.append(
                f"- [[youtube-{video_id}]] - supporting context; not the exact "
                "session recording."
            )
    if not lines:
        lines.append(
            "No exact recording or transcript evidence is attached yet; the official "
            "schedule remains the source for this session."
        )
    return upsert_section(markdown, "Media Evidence", "\n".join(lines))


@lru_cache(maxsize=1)
def private_credibility_v2_policy() -> dict:
    if not PRIVATE_CREDIBILITY_V2_POLICY.is_file():
        return {}
    try:
        payload = json.loads(read(PRIVATE_CREDIBILITY_V2_POLICY))
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def private_writing_decision(
    article_slug: str | None,
    video_id: str,
) -> dict:
    policy = private_credibility_v2_policy()
    if article_slug:
        topic_rows = policy.get("topicVideoWritingDecisions", {})
        if isinstance(topic_rows, dict):
            article_rows = topic_rows.get(article_slug, {})
            if isinstance(article_rows, dict):
                decision = article_rows.get(video_id)
                if isinstance(decision, dict):
                    return decision
    video_rows = policy.get("videoWritingDecisions", {})
    if isinstance(video_rows, dict):
        decision = video_rows.get(video_id)
        if isinstance(decision, dict):
            return decision
    return {}


def private_topic_video_writing_decision(
    article_slug: str,
    video_id: str,
) -> dict:
    """Return only an exact topic/video decision, without video-level fallback."""

    topic_rows = private_credibility_v2_policy().get(
        "topicVideoWritingDecisions", {}
    )
    if not isinstance(topic_rows, dict):
        return {}
    article_rows = topic_rows.get(article_slug, {})
    if not isinstance(article_rows, dict):
        return {}
    decision = article_rows.get(video_id)
    return decision if isinstance(decision, dict) else {}


def private_topic_writing_decision(article_slug: str) -> dict:
    rows = private_credibility_v2_policy().get("topicWritingDecisions", {})
    if not isinstance(rows, dict):
        return {}
    decision = rows.get(article_slug)
    return decision if isinstance(decision, dict) else {}


def private_entity_writing_decision(kind: str, article_slug: str) -> dict:
    key = (
        "peopleWritingDecisions"
        if kind == "people"
        else "companyWritingDecisions"
    )
    rows = private_credibility_v2_policy().get(key, {})
    if not isinstance(rows, dict):
        return {}
    decision = rows.get(article_slug)
    return decision if isinstance(decision, dict) else {}


def writing_allows_source(article_slug: str | None, video_id: str) -> bool:
    return private_writing_decision(article_slug, video_id).get(
        "writingDisposition"
    ) != "omit"


def private_topic_video_candidates(article_slug: str) -> list[str]:
    """Return only evidence-bearing official media explicitly gated for a topic."""

    topic_rows = private_credibility_v2_policy().get(
        "topicVideoWritingDecisions", {}
    )
    if not isinstance(topic_rows, dict):
        return []
    decisions = topic_rows.get(article_slug, {})
    if not isinstance(decisions, dict):
        return []
    values: list[str] = []
    manifest = official_video_manifest()
    for video_id, decision in sorted(decisions.items()):
        if not isinstance(decision, dict):
            continue
        if decision.get("writingDisposition") == "omit":
            continue
        item = manifest.get(video_id, {})
        if item.get("mediaType") in {
            "scheduled_premiere",
            "unavailable_playlist_item",
        }:
            continue
        transcript, _text = transcript_text(video_id)
        has_slides = any(
            (WIKI / "slides" / f"youtube-{video_id}-{suffix}.md").is_file()
            for suffix in ("slides", "dense-slides", "reconstructed-slides")
        )
        if transcript is not None or has_slides:
            values.append(video_id)
    return values


def prioritize_video_ids(
    values: list[str],
    *,
    supporting_limit: int,
) -> list[str]:
    ordered = list(dict.fromkeys(values))
    official_ids = official_event_video_ids()
    primary = [video_id for video_id in ordered if video_id in official_ids]
    supporting = [video_id for video_id in ordered if video_id not in official_ids]
    return primary + supporting[:supporting_limit]


def wikilinks(text: str) -> list[str]:
    links = []
    for raw in re.findall(r"\[\[([^\]]+)\]\]", text):
        target = raw.split("|", 1)[0].strip()
        if target:
            links.append(target)
    return links


def transcript_text(video_id: str) -> tuple[Path | None, str]:
    for folder in TRANSCRIPT_DIRS:
        path = folder / f"{video_id}.txt"
        if path.exists():
            return path, read(path)
    return None, ""


def normalized_relevance_text(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", value.lower()))


def relevance_token(value: str) -> str:
    aliases = {
        "benchmarking": "benchmark",
        "benchmarks": "benchmark",
        "coded": "code",
        "coder": "code",
        "coders": "code",
        "coding": "code",
        "eval": "eval",
        "evals": "eval",
        "evaluate": "eval",
        "evaluated": "eval",
        "evaluates": "eval",
        "evaluating": "eval",
        "evaluation": "eval",
        "evaluations": "eval",
        "indexes": "index",
        "retrieval": "retrieve",
        "retriever": "retrieve",
        "retrievers": "retrieve",
        "retrieving": "retrieve",
        "sandboxes": "sandbox",
        "searched": "search",
        "searches": "search",
        "searching": "search",
    }
    return aliases.get(value, value)


def relevance_tokens(
    value: str,
    *,
    stopwords: set[str] = RELEVANCE_STOPWORDS,
) -> set[str]:
    normalized = {
        relevance_token(token)
        for token in normalized_relevance_text(value).split()
        if len(token) >= 3
    }
    return {token for token in normalized if token not in stopwords}


def article_topic_vocabulary(value: str) -> set[str]:
    owned_sections = re.split(
        r"^## (?:Connections|Evidence Graph|Source Coverage)\s*$",
        value,
        maxsplit=1,
        flags=re.M,
    )[0]
    return relevance_tokens(owned_sections)


@lru_cache(maxsize=None)
def private_source_selection_profile(
    article_slug: str,
) -> tuple[tuple[str, ...], frozenset[str], frozenset[str]]:
    if not PRIVATE_POLICY_PROFILE.is_file():
        return (), frozenset(), frozenset()
    try:
        payload = json.loads(read(PRIVATE_POLICY_PROFILE))
    except json.JSONDecodeError:
        return (), frozenset(), frozenset()
    profiles = payload.get("sourceSelectionProfiles", [])
    if not isinstance(profiles, list):
        return (), frozenset(), frozenset()
    for profile in profiles:
        if not isinstance(profile, dict) or profile.get("topic") != article_slug:
            continue
        terms = profile.get("titleTerms", [])
        if not isinstance(terms, list):
            terms = []
        approved = profile.get("approvedSupportingMediaIds", [])
        blocked = profile.get("blockedSupportingMediaIds", [])
        if not isinstance(approved, list):
            approved = []
        if not isinstance(blocked, list):
            blocked = []
        return (
            tuple(
                sorted(
                    {
                        normalized_relevance_text(term)
                        for term in terms
                        if isinstance(term, str) and normalized_relevance_text(term)
                    }
                )
            ),
            frozenset(value for value in approved if isinstance(value, str)),
            frozenset(value for value in blocked if isinstance(value, str)),
        )
    return (), frozenset(), frozenset()


def configured_title_matches(text: str, terms: tuple[str, ...]) -> int:
    normalized = f" {normalized_relevance_text(text)} "
    return sum(1 for term in terms if f" {term} " in normalized)


def article_relevance_terms(slug: str, title: str) -> tuple[list[str], list[str]]:
    phrases = list(
        dict.fromkeys(
            value
            for value in (
                normalized_relevance_text(title),
                normalized_relevance_text(slug.replace("-", " ")),
            )
            if value
        )
    )
    tokens = list(
        dict.fromkeys(
            relevance_token(token)
            for phrase in phrases
            for token in phrase.split()
            if len(token) >= 3 and token not in TITLE_RELEVANCE_STOPWORDS
        )
    )
    if not tokens:
        tokens = list(
            dict.fromkeys(
                token
                for phrase in phrases
                for token in phrase.split()
                if len(token) >= 3
            )
        )
    return phrases, tokens


def relevance_features(
    text: str,
    phrases: list[str],
    tokens: list[str],
) -> tuple[int, int]:
    normalized = f" {normalized_relevance_text(text)} "
    phrase_matches = sum(
        1 for phrase in phrases if f" {phrase} " in normalized
    )
    token_matches = len(
        set(tokens)
        & relevance_tokens(text, stopwords=TITLE_RELEVANCE_STOPWORDS)
    )
    return phrase_matches, token_matches


def select_relevant_video_ids(
    values: list[str],
    *,
    article_slug: str,
    article_title: str,
    article_text: str,
    association_pages: list[Path],
    supporting_limit: int,
) -> list[str]:
    """Keep primary sources and choose bounded context using private evidence signals."""
    ordered = list(dict.fromkeys(values))
    official_ids = official_event_video_ids()
    article_video_ids = set(video_ids(article_text))
    primary = [
        video_id
        for video_id in ordered
        if video_id in official_ids
        and writing_allows_source(article_slug, video_id)
        and bool(private_topic_video_writing_decision(article_slug, video_id))
    ]
    supporting = [video_id for video_id in ordered if video_id not in official_ids]
    phrases, tokens = article_relevance_terms(article_slug, article_title)
    configured_terms, approved_media_ids, blocked_media_ids = (
        private_source_selection_profile(article_slug)
    )
    article_positions = {
        video_id: article_text.find(video_id)
        for video_id in article_video_ids
    }
    topic_vocabulary = article_topic_vocabulary(article_text)
    association_context: dict[str, list[tuple[str, str]]] = defaultdict(list)
    supporting_set = set(supporting)
    for page in association_pages:
        page_text = read(page)
        page_title = title_of(page)
        for video_id in video_ids(page_text):
            if video_id in supporting_set:
                association_context[video_id].append((page_title, page_text))

    @lru_cache(maxsize=None)
    def selection_key(video_id: str) -> tuple[int | str, ...]:
        resource_path = WIKI / "resources" / f"youtube-{video_id}.md"
        resource_text = read(resource_path)
        resource_title = title_of(resource_path) if resource_path.exists() else ""
        _transcript_path, transcript = transcript_text(video_id)
        slide_signal = "\n".join(slide_text(video_id))
        media_text = "\n".join([resource_text, transcript, slide_signal])
        contexts = association_context.get(video_id, [])
        context_titles = "\n".join(title for title, _text in contexts)

        title_phrase, title_tokens = relevance_features(
            resource_title, phrases, tokens
        )
        media_phrase, media_tokens = relevance_features(media_text, phrases, tokens)
        context_title_phrase, context_title_tokens = relevance_features(
            context_titles, phrases, tokens
        )
        resource_topic_tokens = len(relevance_tokens(resource_title) & topic_vocabulary)
        context_topic_tokens = len(relevance_tokens(context_titles) & topic_vocabulary)
        configured_matches = configured_title_matches(
            resource_title, configured_terms
        )
        approved_media = int(video_id in approved_media_ids)
        exact_article_link = int(
            any(
                re.search(
                    rf"\[\[{re.escape(article_slug)}(?:\||\]\])",
                    context,
                    flags=re.I,
                )
                for _title, context in contexts
            )
        )
        features = (
            approved_media,
            configured_matches,
            title_phrase,
            title_tokens,
            resource_topic_tokens,
            media_phrase,
            media_tokens,
            context_title_phrase,
            context_title_tokens,
            context_topic_tokens,
            int(video_id in article_video_ids),
            exact_article_link,
            int(bool(transcript)),
            int(bool(slide_signal)),
        )
        if video_id in blocked_media_ids:
            has_article_relevance = False
        elif approved_media:
            has_article_relevance = True
        elif configured_terms:
            has_article_relevance = configured_matches > 0
        else:
            has_article_relevance = any(
                (
                    title_phrase,
                    title_tokens,
                    resource_topic_tokens,
                    context_title_phrase,
                    context_title_tokens,
                    context_topic_tokens,
                    exact_article_link,
                )
            )
        article_position = article_positions.get(video_id, len(article_text) + 1)
        return (
            0 if has_article_relevance else 1,
            *(-value for value in features),
            article_position,
            video_id,
        )

    selected_supporting = [
        video_id
        for video_id in sorted(supporting, key=selection_key)
        if selection_key(video_id)[0] == 0
    ][:supporting_limit]
    return primary + selected_supporting


def compact_line(value: str) -> str:
    value = re.sub(r"\s+", " ", value.replace("->", "→")).strip(" -•\t")
    return value


def useful_line(value: str, *, strict: bool = False) -> bool:
    value = compact_line(value)
    if len(value) < 8 or len(value) > 180:
        return False
    if "\\" in value:
        return False
    if re.match(r"^[^\w(]", value):
        return False
    low = re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()
    words = low.split()
    if not words:
        return False
    noise_words = {"a", "c", "ee", "ae", "oo", "sb", "ss"}
    if sum(1 for word in words if word in noise_words) >= 2:
        return False
    if len(words[0]) == 1:
        return False
    if "world ss" in low:
        return False
    if len(words) <= 4 and words[-1] in STOPWORDS:
        return False
    if not any(word not in STOPWORDS for word in words):
        return False
    noisy_phrases = [
        "innovation partner",
        "platinum sponsor",
        "platinum sponsors",
        "presented by",
        "presenting sponsor",
        "world s fair",
        "worldsfair",
        "ai engineer",
        "aiengineer",
        "alengineer",
    ]
    if any(phrase in low for phrase in noisy_phrases) and len(words) <= 8:
        return False
    if len(words) == 1 and not any(ch.isdigit() for ch in low):
        return False
    if len(words) < 3 and not any(ch.isdigit() for ch in value) and not any(mark in value for mark in [":", "/", "→", "-"]):
        return False
    if strict and len(words) < 4 and not any(ch.isdigit() for ch in value):
        return False
    short_words = sum(1 for word in words if len(word) <= 2)
    if len(words) >= 4 and short_words / len(words) > 0.55:
        return False
    if re.search(r"\b(?:e{3,}|a{3,}|o{3,})\b", low):
        return False
    letters = sum(ch.isalpha() for ch in value)
    if letters < 5:
        return False
    if re.fullmatch(r"[\W\d_]+", value):
        return False
    return True


def display_slide_line(value: str) -> bool:
    if not useful_line(value, strict=True):
        return False
    tokens = re.findall(r"[A-Za-z][A-Za-z']{2,}", value)
    if not tokens:
        return False
    if any(len(token) > 24 for token in tokens):
        return False
    known = 0
    checked = 0
    for token in tokens:
        bare = token.strip("'").lower()
        if len(bare) < 4:
            continue
        if token.isupper() and len(token) <= 6:
            known += 1
            checked += 1
            continue
        if bare in ENGLISH_WORDS:
            known += 1
        checked += 1
    return checked == 0 or (known / checked) >= 0.55


def extract_block_text(markdown: str, *, strict: bool = False) -> list[str]:
    lines: list[str] = []
    capture = False
    for line in markdown.splitlines():
        stripped = line.rstrip()
        if stripped in {"Slide text:", "OCR text:"}:
            capture = True
            continue
        if capture:
            if stripped.startswith(">"):
                clean = compact_line(stripped.lstrip("> "))
                if useful_line(clean, strict=strict):
                    lines.append(clean)
                continue
            if not stripped:
                continue
            capture = False
    return dedupe(lines)


@lru_cache(maxsize=None)
def classification_audit_violations(
    deck_kind: str,
    video_id: str,
) -> tuple[str, ...]:
    if deck_kind not in slide_corpus.DECKS:
        return ("unsupported_deck_kind",)
    item = slide_quarantine.item_for(deck_kind, video_id)
    return tuple(
        slide_corpus.audit_validation(
            item,
            slide_quarantine.contract_args(),
        )
    )


def classification_text(video_id: str) -> list[str]:
    lines: list[str] = []
    audit_root = RAW / "slide-ai-classification"
    for audit in sorted(audit_root.glob(f"*/{video_id}/audit.json")):
        deck_kind = audit.parent.parent.name
        if audit != slide_corpus.audit_path(video_id, deck_kind):
            continue
        if classification_audit_violations(deck_kind, video_id):
            continue
        data = slide_corpus.load_json(audit)
        accepted = data.get("accepted", [])
        if not isinstance(accepted, list):
            continue
        for item in accepted:
            if not isinstance(item, dict):
                continue
            for line in str(item.get("text") or "").splitlines():
                clean = compact_line(line)
                if useful_line(clean):
                    lines.append(clean)
    return dedupe(lines)


def slide_text(video_id: str) -> list[str]:
    classified = classification_text(video_id)
    if classified:
        return classified[:10]
    lines: list[str] = []
    for suffix in ["dense-slides", "reconstructed-slides"]:
        page = WIKI / "slides" / f"youtube-{video_id}-{suffix}.md"
        if page.exists():
            lines.extend(extract_block_text(read(page)))
    page = WIKI / "slides" / f"youtube-{video_id}-slides.md"
    if page.exists():
        lines.extend(extract_block_text(read(page), strict=True))
    return dedupe(lines)


def dedupe(items: list[str], limit: int = 20) -> list[str]:
    seen = set()
    result = []
    for item in items:
        key = re.sub(r"\W+", "", item.lower())
        if not key or key in seen:
            continue
        seen.add(key)
        result.append(item)
        if len(result) >= limit:
            break
    return result


def keyword_summary(text: str, limit: int = 8) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9-]{3,}", text.lower())
    counts = Counter(w for w in words if w not in STOPWORDS)
    return [word for word, _count in counts.most_common(limit)]


def slide_keyword_summary(lines: list[str], limit: int = 8) -> list[str]:
    words = []
    for line in lines:
        for word in re.findall(r"[A-Za-z][A-Za-z'-]{3,}", line.lower()):
            word = word.strip("-'")
            if word in STOPWORDS:
                continue
            if word in ENGLISH_WORDS or word in {"agentic", "playwright", "browserbase", "stagehand", "openclaw", "mcp"}:
                words.append(word)
    counts = Counter(words)
    return [word for word, _count in counts.most_common(limit)]


def evidence_for_video(video_id: str, *, article_slug: str | None = None) -> dict:
    tpath, transcript = transcript_text(video_id)
    slides = [line for line in slide_text(video_id) if display_slide_line(line)]
    resource = WIKI / "resources" / f"youtube-{video_id}.md"
    manifest = official_video_manifest().get(video_id, {})
    decision = private_writing_decision(article_slug, video_id)
    return {
        "video_id": video_id,
        "transcript_path": tpath,
        "transcript_words": len(transcript.split()) if transcript else 0,
        "keywords": keyword_summary(transcript, 8) if transcript else [],
        "slide_lines": slides[:10],
        "slide_keywords": slide_keyword_summary(slides, 8),
        "resource_exists": resource.exists(),
        "source_role": (
            "primary event evidence"
            if video_id in official_event_video_ids()
            else "supporting context only"
        ),
        "media_type": str(manifest.get("mediaType") or ""),
        "writing_disposition": str(decision.get("writingDisposition") or ""),
        "attribution": str(decision.get("attribution") or ""),
        "slide_pages": [
            f"youtube-{video_id}-{suffix}"
            for suffix in ["slides", "dense-slides", "reconstructed-slides"]
            if (WIKI / "slides" / f"youtube-{video_id}-{suffix}.md").exists()
        ],
    }


def has_synthesis_grade_slide_signal(evidence: dict) -> bool:
    return len(evidence["slide_lines"]) >= 3 and len(evidence["slide_keywords"]) >= 3


def slide_page_summary(page_id: str) -> dict:
    path = WIKI / "slides" / f"{page_id}.md"
    text = read(path)
    images = re.findall(r"!\[\[([^\]]+\.(?:jpg|jpeg|png|webp))(?:\|[^\]]+)?\]\]", text, flags=re.I)
    recreation_count = len(re.findall(r"open HTML recreation", text))
    no_visible = "No slide-like frames are visible after AI slide classification" in text
    title = title_of(path) if path.exists() else page_id
    return {
        "page_id": page_id,
        "title": title,
        "images": images,
        "recreation_count": recreation_count,
        "no_visible": no_visible,
    }


def render_talk_slides_section(video_ids_: list[str]) -> str:
    if not video_ids_:
        return ""
    lines: list[str] = []
    found = False
    for video_id in video_ids_[:6]:
        ev = evidence_for_video(video_id)
        slide_pages = ev["slide_pages"]
        if not slide_pages:
            continue
        found = True
        lines.append(f"- Source video: `youtube-{video_id}`")

        preferred = sorted(
            slide_pages,
            key=lambda page_id: (
                0 if page_id.endswith("-dense-slides") else 1 if page_id.endswith("-reconstructed-slides") else 2,
                page_id,
            ),
        )
        primary = preferred[0]
        summary = slide_page_summary(primary)
        bits = []
        if summary["images"]:
            bits.append(f"{len(summary['images'])} visible slide image(s)")
        if summary["recreation_count"]:
            bits.append(f"{summary['recreation_count']} HTML recreation(s)")
        if summary["no_visible"]:
            bits.append("no readable content slides after AI classification")
        detail = "; ".join(bits) if bits else "slide evidence page"
        lines.append(f"- Slide deck: [[{primary}|{summary['title']}]] — {detail}.")
        for image in summary["images"][:3]:
            lines.append(f"![[{image}]]")

        alternates = [page_id for page_id in slide_pages if page_id != primary]
        if alternates:
            links = ", ".join(f"[[{page_id}|{title_of(WIKI / 'slides' / f'{page_id}.md')}]]" for page_id in alternates)
            lines.append(f"- Additional slide evidence: {links}")
        if ev["slide_keywords"]:
            lines.append(f"- Slide-derived themes for `youtube-{video_id}`: {', '.join(ev['slide_keywords'])}.")
    return "\n".join(lines) if found else ""


def render_evidence_section(
    video_ids_: list[str],
    *,
    include_title: bool = True,
    max_supporting: int = 8,
    article_slug: str | None = None,
) -> str:
    if not video_ids_:
        return "No linked video, transcript, or slide source has been attached yet."
    lines: list[str] = []
    for video_id in prioritize_video_ids(
        video_ids_, supporting_limit=max_supporting
    ):
        if not writing_allows_source(article_slug, video_id):
            continue
        ev = evidence_for_video(video_id, article_slug=article_slug)
        if not ev["transcript_words"] and not ev["slide_lines"] and not ev["resource_exists"] and not ev["slide_pages"]:
            continue
        if include_title:
            bits = []
            if ev["transcript_words"]:
                bits.append(f"{ev['transcript_words']:,} transcript words")
            if has_synthesis_grade_slide_signal(ev):
                bits.append(f"{len(ev['slide_lines'])} slide-derived text signals")
            detail = "; ".join(bits) if bits else "source page linked"
            lines.append(
                f"- `youtube-{video_id}` — {detail}; role: {ev['source_role']}."
            )
            if ev["attribution"] == "source_attributed":
                lines.append(
                    f"- Interpretation rule for `youtube-{video_id}`: attribute claims to the recording or speaker unless independently corroborated."
                )
        if ev["keywords"]:
            lines.append(f"- Transcript signals for `youtube-{video_id}`: {', '.join(ev['keywords'])}.")
        if has_synthesis_grade_slide_signal(ev):
            lines.append(f"- Slide-derived themes for `youtube-{video_id}`: {', '.join(ev['slide_keywords'])}.")
        links = []
        if ev["resource_exists"]:
            links.append(f"[[youtube-{video_id}]]")
        if ev["transcript_path"]:
            links.append(f"[[youtube-{video_id}-transcript]]")
        links.extend(f"[[{page}]]" for page in ev["slide_pages"])
        if links:
            lines.append(
                f"- Evidence links for `youtube-{video_id}` ({ev['source_role']}): "
                f"{', '.join(links)}"
            )
    return "\n".join(lines) if lines else "No linked video, transcript, or slide source has been attached yet."


def enrich_talk(path: Path) -> bool:
    text = read(path)
    new_text = strip_unmatched_event_media(text, path.stem)
    selection_text = source_text_for_enrichment(
        new_text,
        TALK_GENERATED_SOURCE_HEADINGS,
    )
    ids = talk_evidence_video_ids(path.stem, selection_text)
    new_text = ensure_talk_media_evidence(new_text, path.stem, ids)
    new_text = remove_pending_transcript_note(new_text) if ids else new_text
    slides_section = render_talk_slides_section(ids)
    new_text = upsert_section(new_text, "Slides", slides_section) if slides_section else remove_section(new_text, "Slides")
    section = [
        "This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.",
        "",
        "### Media Signals",
        render_evidence_section(ids, article_slug=path.stem),
        "",
        "### Agent Reading Notes",
        "Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.",
    ]
    new_text = upsert_section(new_text, "Evidence Graph", "\n".join(section))
    if new_text != text:
        write(path, new_text)
        return True
    return False


def page_mentions_for(
    slug: str,
    title: str,
    folders: list[str],
    limit: int | None = 12,
) -> list[Path]:
    needles = {slug.lower(), title.lower()}
    parts = [part for part in re.split(r"[^a-z0-9]+", slug.lower()) if len(part) > 3]
    paths = []
    for folder in folders:
        for path in sorted((WIKI / folder).glob("*.md")):
            text = read(path)
            if folder == "talks":
                text = source_text_for_enrichment(
                    text, TALK_GENERATED_SOURCE_HEADINGS
                )
            hay = text.lower()
            if any(needle and needle in hay for needle in needles) or sum(part in hay for part in parts) >= 2:
                paths.append(path)
                if limit is not None and len(paths) >= limit:
                    return paths
    return paths


def collect_video_ids_from_pages(
    paths: list[Path],
    *,
    supporting_limit: int | None = None,
) -> list[str]:
    ids: list[str] = []
    for path in paths:
        text = read(path)
        if path.parent.name == "talks":
            ids.extend(official_recording_ids_for_talk(path.stem))
            text = source_text_for_enrichment(
                text, TALK_GENERATED_SOURCE_HEADINGS
            )
        ids.extend(video_ids(text))
    if supporting_limit is None:
        return list(dict.fromkeys(ids))
    return prioritize_video_ids(ids, supporting_limit=supporting_limit)


def enrich_topic(path: Path) -> bool:
    text = read(path)
    source_text = source_text_for_enrichment(
        text, TOPIC_GENERATED_SOURCE_HEADINGS
    )
    title = title_of(path)
    related = [WIKI / "talks" / f"{target}.md" for target in wikilinks(source_text) if (WIKI / "talks" / f"{target}.md").exists()]
    related.extend(page_mentions_for(path.stem, title, ["talks"], limit=None))
    related = dedupe_paths(related)
    ids = select_relevant_video_ids(
        [
            *collect_video_ids_from_pages(related),
            *video_ids(source_text),
            *private_topic_video_candidates(path.stem),
        ],
        article_slug=path.stem,
        article_title=title,
        article_text=source_text,
        association_pages=related,
        supporting_limit=8,
    )
    lines = [
        "This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.",
        "",
    ]
    topic_decision = private_topic_writing_decision(path.stem)
    if topic_decision.get("writingDisposition") == "assert_with_citations":
        lines.extend(
            [
                "The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.",
                "",
            ]
        )
    elif topic_decision.get("writingDisposition") == "attribute_to_source":
        lines.extend(
            [
                "Current media support is attributable to one official recording; it is context for the theme rather than independent corroboration of every claim.",
                "",
            ]
        )
    lines.append("### Linked Sessions")
    if related:
        for talk in related[:10]:
            lines.append(f"- [[{talk.stem}|{title_of(talk)}]]")
    else:
        lines.append("- No related talks were found by link or text match in this pass.")
    lines.extend(
        [
            "",
            "### Media Signals",
            render_evidence_section(
                ids,
                max_supporting=8,
                article_slug=path.stem,
            ),
        ]
    )
    new_text = upsert_section(text, "Evidence Graph", "\n".join(lines))
    if new_text != text:
        write(path, new_text)
        return True
    return False


def dedupe_paths(paths: list[Path], limit: int | None = None) -> list[Path]:
    seen = set()
    out = []
    for path in paths:
        if path in seen or not path.exists():
            continue
        seen.add(path)
        out.append(path)
        if limit is not None and len(out) >= limit:
            break
    return out


def enrich_person_or_company(path: Path, kind: str) -> bool:
    text = read(path)
    source_text = source_text_for_enrichment(text)
    links = [target for target in wikilinks(source_text) if (WIKI / "talks" / f"{target}.md").exists()]
    talk_paths = [WIKI / "talks" / f"{target}.md" for target in links]
    if not talk_paths:
        talk_paths = page_mentions_for(path.stem, title_of(path), ["talks"], limit=None)
    talk_paths = dedupe_paths(talk_paths)
    ids = select_relevant_video_ids(
        [
            *collect_video_ids_from_pages(talk_paths),
            *video_ids(source_text),
        ],
        article_slug=path.stem,
        article_title=title_of(path),
        article_text=source_text,
        association_pages=talk_paths,
        supporting_limit=6,
    )
    label = "person" if kind == "people" else "organization"
    entity_decision = private_entity_writing_decision(kind, path.stem)
    lines = [
        f"This section summarizes how this {label} appears across the conference source graph: scheduled sessions, linked videos, transcripts, and slide-derived evidence.",
        "",
    ]
    if entity_decision.get("writingDisposition") == "attribute_to_source":
        lines.extend(
            [
                "Event participation, role, and affiliation details remain attributed to the official event program; publication here is not an endorsement.",
                "",
            ]
        )
    elif entity_decision.get("writingDisposition") == "assert_with_citations":
        lines.extend(
            [
                "The entity relationship is supported by more than one independently attributed source, while each technical or product claim still requires its own cited evidence.",
                "",
            ]
        )
    lines.append("### Linked Sessions")
    if talk_paths:
        for talk in talk_paths[:10]:
            lines.append(f"- [[{talk.stem}|{title_of(talk)}]]")
    else:
        lines.append("- No related scheduled session was found in this pass.")
    lines.extend(
        [
            "",
            "### Media Signals",
            render_evidence_section(
                ids,
                max_supporting=6,
                article_slug=path.stem,
            ),
        ]
    )
    new_text = upsert_section(text, "Evidence Graph", "\n".join(lines))
    if new_text != text:
        write(path, new_text)
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--talks", action="store_true")
    parser.add_argument("--topics", action="store_true")
    parser.add_argument("--people", action="store_true")
    parser.add_argument("--companies", action="store_true")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    if not any([args.talks, args.topics, args.people, args.companies, args.all]):
        args.all = True

    counts = defaultdict(int)
    targets: list[tuple[str, Path]] = []
    if args.all or args.talks:
        targets.extend(("talks", p) for p in sorted((WIKI / "talks").glob("*.md")))
    if args.all or args.topics:
        targets.extend(("topics", p) for p in sorted((WIKI / "topics").glob("*.md")) if p.name != "index.md")
    if args.all or args.people:
        targets.extend(("people", p) for p in sorted((WIKI / "people").glob("*.md")) if p.name != "index.md")
    if args.all or args.companies:
        targets.extend(("companies", p) for p in sorted((WIKI / "companies").glob("*.md")) if p.name != "index.md")
    if args.limit:
        targets = targets[: args.limit]

    for kind, path in targets:
        changed = False
        if kind == "talks":
            changed = enrich_talk(path)
        elif kind == "topics":
            changed = enrich_topic(path)
        elif kind in {"people", "companies"}:
            changed = enrich_person_or_company(path, kind)
        if changed:
            counts[kind] += 1

    print(json.dumps({"updated": dict(counts), "processed": len(targets)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
