# Profile maintenance

The root README appears on the GitHub profile. All project links point to public repositories; personal website links are intentionally omitted.

- `assets/banner.svg`: custom vector header, with no external dependencies.
- `scripts/design_assets.py`: regenerate the signal-field header, five project cards, section titles, about panel, and contact footer. The header includes a periodic SVG interference-field animation, with a static reduced-motion fallback.
- `scripts/contributions.py`: renders the actual public GitHub contribution calendar as a constellation. Intensity levels come from GitHub; the display never invents activity.
- `assets/contributions.svg`: last successfully generated contribution constellation.
- `assets/github-metrics.svg`: committed public repository dashboard, so the image remains available if an API request fails.
- `scripts/update_metrics.py`: generates the dashboard using Python's standard library and public GitHub repository data. Forks and private repositories are excluded. Language share is measured by code bytes, not skill level.
- `.github/workflows/metrics.yml`: refreshes the dashboard daily and after generator changes. Uses the built-in `GITHUB_TOKEN`; no personal access token or repository secret needs to be added.

Run `python scripts/update_metrics.py` to refresh locally, or select **Actions → Refresh profile metrics → Run workflow**. The scheduled run is at 03:17 UTC (08:47 IST). If Actions is disabled, the last committed dashboard remains visible.

To edit the introduction or project descriptions, update `README.md`. Verify that any added repository is public before linking it. Keep personal website addresses and private project links out of profile assets and documentation.
