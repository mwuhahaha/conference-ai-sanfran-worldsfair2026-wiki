#!/usr/bin/env python3
"""Discover and cache public company profiles for company wiki pages.

The script is intentionally conservative. It uses the official roster as the
company list, tries several public discovery methods, fetches lightweight HTML
metadata from likely official sites, and writes profile records that the
company-page renderer can use.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import time
from collections import defaultdict
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import parse_qs, quote_plus, unquote, urlparse

import requests
from bs4 import BeautifulSoup

from build_worldsfair_wiki import ROOT, assign_talk_slugs, day_to_date, slugify, talk_slug


RAW = ROOT / "raw" / "sources"
PROFILES = RAW / "company-profiles.json"
REPORT = RAW / "company-profile-fetch-report.json"

USER_AGENT = "WorldsfairWikiCompanyEnricher/1.0 (+https://aie-worldsfair2026.plusrobot.ai/)"
TIMEOUT = 7
TLD_CANDIDATES = [".ai", ".com", ".io", ".dev", ".co", ".app", ".org", ".cloud"]
SKIP_DOMAINS = {
    "linkedin.com",
    "x.com",
    "twitter.com",
    "facebook.com",
    "instagram.com",
    "youtube.com",
    "wikipedia.org",
    "crunchbase.com",
    "github.com",
    "wellfound.com",
    "pitchbook.com",
    "glassdoor.com",
    "tracxn.com",
    "cbinsights.com",
}
PARKED_PATTERNS = [
    "domain is for sale",
    "for sale |",
    "buy this domain",
    "secure checkout and guided transfer",
    "parkingcrew",
    "sedo",
    "spaceship.com",
    "godaddy",
    "rebrandly",
]
GENERIC_METADATA_PATTERNS = [
    "your company description goes here",
    "description goes here",
    "lorem ipsum",
]
MANUAL_SUMMARIES = {
    "emulated": (
        "Emulated builds reinforcement-learning environments that simulate real production systems "
        "for coding and infrastructure agents, according to the official AI Engineer World's Fair schedule PDF."
    ),
}
MANUAL_URLS = {
    "adaption": "https://adaptionlabs.ai/",
    "agentmail": "https://agentmail.to/",
    "ai-engineer": "https://www.ai.engineer/",
    "amazon-web-services": "https://aws.amazon.com/",
    "amazon-web-services-aws": "https://aws.amazon.com/",
    "aws": "https://aws.amazon.com/",
    "amazon-agi": "https://www.amazon.science/",
    "amazon-agi-lab": "https://www.amazon.science/",
    "badass-dev-egghead-io": "https://badass.dev/",
    "china-resources-holdings": "https://en.crc.com.hk/",
    "coinbase": "https://www.coinbase.com/",
    "deasy-labs-collibra": "https://www.deasylabs.com/about-us",
    "dfpi": "https://dfpi.ca.gov/",
    "egghead-io": "https://egghead.io/",
    "emulated": "https://emulated.so/",
    "every-cora": "https://cora.computer/",
    "exo-labs": "https://github.com/exo-explore/exo",
    "fidelity-investments": "https://www.fidelity.com/",
    "friendliai": "https://friendli.ai/",
    "gepa": "https://github.com/gepa-ai/gepa",
    "google-deepmind": "https://deepmind.google/",
    "hornet-dev": "https://hornet.dev/",
    "independent-state-of-data": "https://www.stateofdata.org/",
    "joyce-consulting-group": "https://www.joycezhang.io/",
    "kiduna-club": "https://kiduna.design/",
    "latent-space-ai-engineer": "https://www.latent.space/",
    "laude-institute": "https://www.laude.org/",
    "linkedin": "https://www.linkedin.com/",
    "mckinsey-and-company": "https://www.mckinsey.com/",
    "mcp-apps": "https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/",
    "microsoft-research": "https://www.microsoft.com/en-us/research/",
    "mit-media-lab": "https://www.media.mit.edu/",
    "morgan-stanley": "https://www.morganstanley.com/",
    "nubank": "https://nubank.com.br/en/",
    "openai": "https://openai.com/",
    "oracle": "https://www.oracle.com/",
    "paper-compute-co": "https://papercompute.com/about/",
    "paypal-braintree": "https://www.braintreepayments.com/",
    "philo-ventures": "https://philo.ventures/",
    "quantumblack-ai-by-mckinsey": "https://www.mckinsey.com/capabilities/quantumblack/overview",
    "reactor": "https://reactor.inc/",
    "renaissance-geek-inc": "https://www.paulbakaus.com/about/",
    "servicenow": "https://www.servicenow.com/",
    "spotify": "https://www.spotify.com/",
    "stanford-university-together-ai": "https://hai.stanford.edu/people/james-zou",
    "stanford-university": "https://www.stanford.edu/",
    "t3-tools-and-youtuber": "https://t3.gg/",
    "the-new-york-times": "https://www.nytimes.com/",
    "the-new-york-times-games": "https://www.nytimes.com/crosswords",
    "uc-berkeley": "https://www.berkeley.edu/",
    "ucal-berkeley": "https://www.berkeley.edu/",
    "untapped-capital": "https://www.untapped.vc/about",
    "urun": "https://jobs.ashbyhq.com/Urun/cb392c87-5df1-4400-9b1f-8737fcf892f4",
    "weights-and-biases-by-coreweave": "https://wandb.ai/",
    "w-and-b-from-coreweave": "https://wandb.ai/",
    "wisedocs": "https://www.wisedocs.ai/company/about-us",
    "you-com-recursive-superintelligence": "https://www.socher.org/",
    "youtube": "https://www.youtube.com/",
    "zions-bancorporation": "https://www.zionsbancorporation.com/",
}


@dataclass
class Candidate:
    url: str
    method: str
    score: int
    title: str = ""
    snippet: str = ""


def load_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def company_name_from_slug(slug: str, speakers: list[dict]) -> str:
    for speaker in speakers:
        company = speaker.get("company") or ""
        if slugify(company) == slug:
            return company
    return slug.replace("-", " ").title()


def normalize_company_name(name: str) -> str:
    cleaned = re.sub(r"\([^)]*\)", " ", name)
    cleaned = cleaned.replace("&", " and ")
    cleaned = re.sub(r"\b(inc|inc\.|llc|ltd|labs|lab|ai|technologies|technology|company|corp|corporation)\b", " ", cleaned, flags=re.I)
    cleaned = re.sub(r"[^a-z0-9]+", "", cleaned.lower())
    return cleaned


def domain_tokens(domain: str) -> str:
    host = urlparse(domain if "://" in domain else f"https://{domain}").netloc or domain
    host = host.lower().removeprefix("www.")
    base = host.split(".")[0]
    return re.sub(r"[^a-z0-9]+", "", base)


def acceptable_domain(url: str) -> bool:
    host = urlparse(url).netloc.lower().removeprefix("www.")
    return bool(host) and not any(host == d or host.endswith("." + d) for d in SKIP_DOMAINS)


def clean_url(url: str) -> str:
    if not url:
        return ""
    if url.startswith("//"):
        url = "https:" + url
    if url.startswith("/l/?"):
        qs = parse_qs(urlparse(url).query)
        if qs.get("uddg"):
            url = qs["uddg"][0]
    return unquote(url)


def fetch(url: str) -> requests.Response | None:
    try:
        return requests.get(url, timeout=TIMEOUT, headers={"User-Agent": USER_AGENT}, allow_redirects=True)
    except requests.RequestException:
        return None


def discover_search(company: str, limit: int = 8) -> list[Candidate]:
    query = quote_plus(f"{company} official site AI company")
    url = f"https://html.duckduckgo.com/html/?q={query}"
    response = fetch(url)
    if not response or response.status_code >= 400:
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    candidates: list[Candidate] = []
    for result in soup.select(".result")[:limit]:
        link = result.select_one("a.result__a")
        if not link:
            continue
        href = clean_url(link.get("href", ""))
        if not href.startswith("http") or not acceptable_domain(href):
            continue
        title = link.get_text(" ", strip=True)
        snippet_node = result.select_one(".result__snippet")
        snippet = snippet_node.get_text(" ", strip=True) if snippet_node else ""
        candidates.append(Candidate(href, "duckduckgo", 40, title, snippet))
    return candidates


def discover_domain_guesses(company: str) -> list[Candidate]:
    base = normalize_company_name(company)
    guesses = []
    for suffix in TLD_CANDIDATES:
        if base:
            guesses.append(Candidate(f"https://{base}{suffix}/", "domain-guess", 20))
    return guesses


def score_candidate(company: str, candidate: Candidate) -> int:
    score = candidate.score
    host = urlparse(candidate.url).netloc.lower().removeprefix("www.")
    name_norm = normalize_company_name(company)
    domain_norm = domain_tokens(host)
    title_norm = normalize_company_name(candidate.title)
    snippet_norm = normalize_company_name(candidate.snippet)
    if name_norm and (name_norm == domain_norm or domain_norm in name_norm or name_norm in domain_norm):
        score += 60
    if name_norm and name_norm in title_norm:
        score += 30
    if name_norm and name_norm in snippet_norm:
        score += 15
    if host.endswith(".ai"):
        score += 5
    if any(word in (candidate.title + " " + candidate.snippet).lower() for word in ["official", "platform", "developers", "ai", "agents", "inference"]):
        score += 8
    return score


def score_final_metadata(company: str, candidate: Candidate, meta: dict) -> int:
    visible = " ".join([meta.get("title", ""), meta.get("site_name", ""), meta.get("description", ""), meta.get("h1", "")]).lower()
    if not visible.strip():
        return 0
    if any(pattern in visible for pattern in PARKED_PATTERNS):
        return 0
    if any(pattern in visible for pattern in GENERIC_METADATA_PATTERNS):
        return 0
    score = 0
    name_norm = normalize_company_name(company)
    host_norm = domain_tokens(meta.get("url") or candidate.url)
    blob_norm = normalize_company_name(" ".join([meta.get("title", ""), meta.get("site_name", ""), meta.get("description", ""), meta.get("h1", "")]))
    if name_norm and (name_norm == host_norm or host_norm in name_norm or name_norm in host_norm):
        score += 65
    if name_norm and name_norm in blob_norm:
        score += 40
    if candidate.method == "duckduckgo" and name_norm and name_norm in normalize_company_name(candidate.title + " " + candidate.snippet):
        score += 20
    if ".ai" in (meta.get("url") or ""):
        score += 5
    if any(word in (meta.get("description", "") + " " + meta.get("title", "")).lower() for word in ["ai", "agent", "developer", "platform", "model", "data", "inference", "automation"]):
        score += 8
    return score


def metadata_from_html(url: str, html_text: str) -> dict:
    soup = BeautifulSoup(html_text, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    metas = {}
    for meta in soup.find_all("meta"):
        key = (meta.get("property") or meta.get("name") or "").lower()
        value = meta.get("content") or ""
        if key and value:
            metas[key] = html.unescape(value.strip())
    h1 = soup.find("h1")
    description = metas.get("og:description") or metas.get("description") or metas.get("twitter:description") or ""
    site_name = metas.get("og:site_name") or ""
    return {
        "url": url,
        "title": html.unescape(title.strip()),
        "site_name": site_name,
        "description": re.sub(r"\s+", " ", description).strip(),
        "h1": h1.get_text(" ", strip=True) if h1 else "",
    }


def fetch_site_metadata(candidate: Candidate) -> tuple[dict | None, str]:
    response = fetch(candidate.url)
    if not response:
        return None, "request_failed"
    if response.status_code >= 400:
        return None, f"http_{response.status_code}"
    ctype = response.headers.get("content-type", "")
    if "text/html" not in ctype and "application/xhtml" not in ctype and "<html" not in response.text[:1000].lower():
        return None, "not_html"
    meta = metadata_from_html(response.url, response.text[:700000])
    visible = " ".join([meta.get("title", ""), meta.get("site_name", ""), meta.get("description", ""), meta.get("h1", "")]).lower()
    if any(pattern in visible for pattern in GENERIC_METADATA_PATTERNS):
        return None, "generic_metadata"
    return meta, "ok"


def sentence(value: str) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    if not value:
        return ""
    if value[-1] not in ".!?":
        value += "."
    return value


def conference_context(company: str, people: list[dict], sessions: list[dict]) -> tuple[str, str]:
    people_text = ", ".join(p.get("name", "") for p in people[:6] if p.get("name")) or "official roster speaker(s)"
    if sessions:
        titles = "; ".join(s.get("title", "Untitled session") for s in sessions[:3])
        why = (
            f"{company} matters to this wiki through {len(people)} official speaker(s) and {len(sessions)} scheduled session(s), "
            f"including: {titles}."
        )
    else:
        why = f"{company} matters to this wiki because it appears in the official speaker roster through {people_text}."
    origin = f"The official speaker roster connects {company} to {people_text}."
    return why, origin


def build_profile(company: str, people: list[dict], sessions: list[dict], meta: dict | None, candidate: Candidate | None, status: str, score: int, slug: str = "") -> dict:
    why, origin = conference_context(company, people, sessions)
    manual_summary = MANUAL_SUMMARIES.get(slug, "")
    if manual_summary:
        summary = f"{company} is represented at AI Engineer World's Fair 2026. {manual_summary}"
        source_labels = ["Official speaker roster", "Official conference schedule", "Public company site", "Manual company URL override", "Automated company profile fetch"]
        if candidate:
            origin = f"{origin} The public source was attached through a manual URL override because the fetched homepage metadata was generic or incomplete."
            links = [{"label": f"{company} public site", "url": candidate.url}]
        elif meta:
            origin = f"{origin} The public source was fetched, but the official schedule provided the usable company context."
            links = [{"label": meta.get("site_name") or meta.get("title") or f"{company} website", "url": meta["url"]}]
        else:
            links = []
    elif meta and status == "fetched" and meta.get("description"):
        summary = f"{company} is represented at AI Engineer World's Fair 2026. Its public site describes it this way: {sentence(meta['description'])}"
        source_labels = ["Official speaker roster", "Official conference schedule", "Public company site", "Automated company profile fetch"]
        origin = f"{origin} The public company site was discovered by {candidate.method if candidate else 'automated discovery'} and fetched for homepage metadata."
        links = [{"label": meta.get("site_name") or meta.get("title") or f"{company} website", "url": meta["url"]}]
    elif meta and status == "fetched":
        title = meta.get("title") or meta.get("h1") or company
        summary = f"{company} is represented at AI Engineer World's Fair 2026. The automated fetch found a likely public site titled \"{title}\", but the page did not expose a concise public description in metadata."
        source_labels = ["Official speaker roster", "Official conference schedule", "Public company site", "Automated company profile fetch"]
        origin = f"{origin} The public company site was discovered by {candidate.method if candidate else 'automated discovery'} and fetched, but usable metadata was limited."
        links = [{"label": title, "url": meta["url"]}]
    elif candidate and candidate.method == "manual-url-override":
        summary = (
            f"{company} is represented at AI Engineer World's Fair 2026 through the official roster and related scheduled sessions. "
            f"A known public site was attached for source navigation, but automated metadata extraction was unavailable in this pass ({status})."
        )
        source_labels = ["Official speaker roster", "Official conference schedule", "Public company site", "Manual company URL override", "Automated company profile fetch"]
        origin = f"{origin} A manual URL override attaches the public site for source navigation because automated discovery or metadata extraction was inconclusive."
        links = [{"label": f"{company} public site", "url": candidate.url}]
    else:
        summary = (
            f"{company} is represented at AI Engineer World's Fair 2026 through the official roster and related scheduled sessions. "
            f"Automated public-site discovery did not attach a reliable company profile source in this pass ({status})."
        )
        source_labels = ["Official speaker roster", "Official conference schedule", "Automated company profile fetch"]
        links = []
    profile = {
        "website": meta.get("url") if meta else (candidate.url if candidate and candidate.method == "manual-url-override" else ""),
        "summary": summary,
        "why_it_matters": why,
        "origin": origin,
        "notes": [
            f"Automated company profile fetch status: {status}.",
            f"Discovery confidence score: {score}.",
        ],
        "sourceLabels": source_labels,
        "sourceLinks": links,
        "fetchStatus": status,
        "fetchConfidence": score,
    }
    if meta:
        profile["fetchedMetadata"] = {k: v for k, v in meta.items() if k in ["title", "site_name", "description", "h1"]}
    return profile


def merge_profile(existing: dict, fetched: dict, force: bool = False) -> dict:
    if not existing:
        return fetched
    if force and "Automated company profile fetch" in existing.get("sourceLabels", []):
        return fetched
    merged = {**fetched, **existing}
    if not existing.get("sourceLinks"):
        merged["sourceLinks"] = fetched.get("sourceLinks", [])
    if not existing.get("website"):
        merged["website"] = fetched.get("website", "")
    if not existing.get("fetchStatus"):
        merged["fetchStatus"] = fetched.get("fetchStatus", "")
        merged["fetchConfidence"] = fetched.get("fetchConfidence", 0)
    return merged


def collect_company_context() -> tuple[dict[str, str], dict[str, list[dict]], dict[str, list[dict]]]:
    speakers = load_json(RAW / "official-speakers.json", {}).get("speakers", [])
    sessions = load_json(RAW / "official-sessions.json", {}).get("sessions", [])
    assign_talk_slugs(sessions)
    slug_to_company = {}
    people_by_company = defaultdict(list)
    sessions_by_company = defaultdict(dict)
    for speaker in speakers:
        company = speaker.get("company")
        if not company:
            continue
        slug = slugify(company)
        slug_to_company[slug] = company
        people_by_company[slug].append(speaker)
    for session in sessions:
        for speaker_name in session.get("speakers", []):
            for speaker in speakers:
                if speaker.get("name") == speaker_name and speaker.get("company"):
                    sessions_by_company[slugify(speaker["company"])][talk_slug(session)] = session
    return slug_to_company, people_by_company, {k: list(v.values()) for k, v in sessions_by_company.items()}


def fetch_profile_for_company(slug: str, company: str, people: list[dict], sessions: list[dict], delay: float) -> tuple[dict, dict]:
    candidates = []
    if slug in MANUAL_URLS:
        candidates.append(Candidate(MANUAL_URLS[slug], "manual-url-override", 90))
    candidates.extend(discover_domain_guesses(company))
    candidates.extend(discover_search(company))
    dedup: dict[str, Candidate] = {}
    for candidate in candidates:
        if not acceptable_domain(candidate.url):
            continue
        candidate.score = score_candidate(company, candidate)
        key = urlparse(candidate.url).netloc.lower().removeprefix("www.")
        if key not in dedup or candidate.score > dedup[key].score:
            dedup[key] = candidate
    ordered = sorted(dedup.values(), key=lambda c: c.score, reverse=True)
    attempts = []
    best_meta = None
    best_candidate = None
    manual_candidate = candidates[0] if candidates and candidates[0].method == "manual-url-override" else None
    status = "no_candidates"
    score = 0
    for candidate in ordered[:8]:
        time.sleep(delay)
        meta, fetch_status = fetch_site_metadata(candidate)
        final_score = score_final_metadata(company, candidate, meta) if meta else 0
        attempts.append({"url": candidate.url, "method": candidate.method, "score": candidate.score, "final_score": final_score, "status": fetch_status, "final_url": meta.get("url") if meta else ""})
        if meta:
            if final_score >= 55:
                best_meta = meta
                best_candidate = candidate
                score = final_score
                status = "fetched"
                break
            status = "rejected_low_confidence_site"
            score = max(score, final_score)
            continue
        status = fetch_status
    if not best_meta and manual_candidate:
        best_candidate = manual_candidate
        status = "manual_url_unfetched" if status in {"request_failed", "http_403", "http_429", "not_html", "generic_metadata"} else status
        score = max(score, 50)
    profile = build_profile(company, people, sessions, best_meta, best_candidate, status, score, slug)
    return profile, {"company": company, "status": status, "score": score, "attempts": attempts}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only-missing", action="store_true", help="Only fetch companies missing curated profile entries.")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--delay", type=float, default=0.08)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--force", action="store_true", help="Refetch even when a profile summary already exists.")
    parser.add_argument("--slug", action="append", help="Only fetch this company slug. Repeatable.")
    args = parser.parse_args()

    profiles = load_json(PROFILES, {})
    slug_to_company, people_by_company, sessions_by_company = collect_company_context()
    targets = sorted(slug_to_company)
    if args.slug:
        wanted = set(args.slug)
        targets = [slug for slug in targets if slug in wanted]
    if args.only_missing and not args.force:
        targets = [slug for slug in targets if slug not in profiles or not profiles.get(slug, {}).get("summary")]
    if args.limit:
        targets = targets[: args.limit]

    report = {"updated": [], "skipped_existing": [], "failures": []}
    def process(index_slug: tuple[int, str]) -> tuple[str, dict | None, dict | None, str | None]:
        index, slug = index_slug
        company = slug_to_company[slug]
        existing = profiles.get(slug, {})
        if existing and existing.get("summary") and not args.force:
            return slug, None, None, "skip"
        try:
            profile, entry = fetch_profile_for_company(slug, company, people_by_company.get(slug, []), sessions_by_company.get(slug, []), args.delay)
            entry["slug"] = slug
            entry["index"] = index
            return slug, profile, entry, None
        except Exception as exc:
            return slug, None, {"slug": slug, "company": company, "error": repr(exc)}, "error"

    indexed_targets = list(enumerate(targets, start=1))
    if args.workers > 1:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = [pool.submit(process, item) for item in indexed_targets]
            for future in as_completed(futures):
                slug, profile, entry, marker = future.result()
                if marker == "skip":
                    report["skipped_existing"].append(slug)
                    continue
                if marker == "error":
                    report["failures"].append(entry)
                    print(json.dumps({"slug": slug, "error": entry["error"]}, sort_keys=True))
                    continue
                existing = profiles.get(slug, {})
                profiles[slug] = merge_profile(existing, profile, args.force)
                report["updated"].append(entry)
                print(json.dumps({"index": entry["index"], "total": len(targets), "slug": slug, "status": entry["status"], "score": entry["score"]}, sort_keys=True))
    else:
        for item in indexed_targets:
            slug, profile, entry, marker = process(item)
            if marker == "skip":
                report["skipped_existing"].append(slug)
                continue
            if marker == "error":
                report["failures"].append(entry)
                print(json.dumps({"slug": slug, "error": entry["error"]}, sort_keys=True))
                continue
            existing = profiles.get(slug, {})
            profiles[slug] = merge_profile(existing, profile, args.force)
            report["updated"].append(entry)
            print(json.dumps({"index": entry["index"], "total": len(targets), "slug": slug, "status": entry["status"], "score": entry["score"]}, sort_keys=True))
    save_json(PROFILES, profiles)
    save_json(REPORT, report)
    print(json.dumps({"profiles": len(profiles), "updated": len(report["updated"]), "failures": len(report["failures"])}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
