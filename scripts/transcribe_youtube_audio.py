#!/usr/bin/env python3
"""Create a local transcript for a YouTube video with faster-whisper.

Use this when YouTube captions are missing or blocked. The script downloads a
small audio-only file with yt-dlp, transcribes it locally, and writes the same
plain-text cache consumed by enrich_from_youtube_transcripts.py.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

from faster_whisper import WhisperModel


ROOT = Path(__file__).resolve().parents[1]
AUDIO_CACHE = ROOT / "raw" / "audio-cache"
TRANSCRIPTS = ROOT / "raw" / "sources" / "youtube-transcripts"


def run(cmd: list[str], *, timeout: int | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=timeout)


def yt_dlp_js_runtime_arg() -> str:
    node = shutil.which("node")
    if not node:
        for candidate in sorted(Path("/home/dylan/.nvm/versions/node").glob("*/bin/node"), reverse=True):
            if candidate.exists():
                node = str(candidate)
                break
    return f"node:{node}" if node else "node"


def download_audio(video_id: str) -> Path:
    AUDIO_CACHE.mkdir(parents=True, exist_ok=True)
    output = AUDIO_CACHE / f"{video_id}.mp3"
    if output.exists() and output.stat().st_size > 1024 * 1024:
        return output
    cmd = [
        "yt-dlp",
        "--js-runtimes",
        yt_dlp_js_runtime_arg(),
        "--remote-components",
        "ejs:github",
        "-f",
        "ba[ext=m4a]/ba/bestaudio",
        "-x",
        "--audio-format",
        "mp3",
        "--audio-quality",
        "5",
        "-o",
        str(AUDIO_CACHE / f"{video_id}.%(ext)s"),
        f"https://www.youtube.com/watch?v={video_id}",
    ]
    cp = run(cmd, timeout=900)
    if cp.returncode != 0:
        raise RuntimeError(cp.stderr[-2000:])
    return output


def transcribe(audio: Path, model_name: str) -> str:
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, _info = model.transcribe(str(audio), beam_size=5, vad_filter=True)
    return " ".join(segment.text.strip() for segment in segments if segment.text.strip())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("video_id")
    parser.add_argument("--model", default="base.en")
    args = parser.parse_args()

    audio = download_audio(args.video_id)
    text = transcribe(audio, args.model)
    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    target = TRANSCRIPTS / f"{args.video_id}.txt"
    target.write_text(text.strip() + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(text.split()):,} words)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
