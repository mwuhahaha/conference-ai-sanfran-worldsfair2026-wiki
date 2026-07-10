#!/usr/bin/env bash
set -euo pipefail

ROOT="/garage/obsidian/conference-ai-sanfran-worldsfair2026-clean"
UNIT_DIR="${HOME}/.config/systemd/user"
SERVICE="aie-wf2026-youtube-monitor.service"
TIMER="aie-wf2026-youtube-monitor.timer"

mkdir -p "${UNIT_DIR}"
cp "${ROOT}/.ops/systemd/${SERVICE}" "${UNIT_DIR}/${SERVICE}"
cp "${ROOT}/.ops/systemd/${TIMER}" "${UNIT_DIR}/${TIMER}"

systemctl --user daemon-reload
systemctl --user enable "${TIMER}"
systemctl --user restart "${TIMER}"
systemctl --user status "${TIMER}" --no-pager

echo
echo "Installed ${TIMER}."
echo "Status page: ${ROOT}/.ops/state/youtube-monitor/status.html"
