# GitHub profile setup

Your profile README is published at https://github.com/souma888. This repository is public and named exactly after your GitHub username, so GitHub automatically displays its root README on your profile.

## Included
- `README.md` — introduction, skill badges, verified project links, and stats cards.
- `assets/banner.svg` — dark purple custom banner.
- `assets/github-metrics.svg` — temporary placeholder before extended metrics is configured.
- `.github/workflows/metrics.yml` — weekly scheduled metrics generation, also runnable manually.

## Enable extended GitHub Metrics (optional)

The ordinary GitHub stats and language charts in the README require no configuration, but depend on a third-party rendering service. The extended metrics SVG is currently a placeholder.

1. Consult the [official Metrics setup guide](https://github.com/lowlighter/metrics/blob/master/.github/readme/partials/documentation/setup/action.md).
2. Create a personal access token with the **minimum permissions required**, using GitHub **Settings → Developer settings → Personal access tokens**. Use the permissions recommended in the guide for the public-data metrics you want.
3. Open this repository's **Settings → Secrets and variables → Actions**. Create the repository secret `METRICS_TOKEN` containing the token.
4. Open **Actions → GitHub Metrics → Run workflow** to generate the live card. A weekly run is configured after that.
5. The workflow commits the rendered SVG to `assets/github-metrics.svg`.

**Never** place a token in source code, README files, screenshots, or chat. If the secret is absent, the generation step is skipped and the placeholder remains.

## Update profile sidebar

GitHub's account profile fields cannot be changed through the connected repository-file integration. Visit https://github.com/settings/profile and consider:

- Name: Soumadip Karan
- Bio: `Engineering @ IIT Mandi | Software Development • AI/ML • Scientific Computing`
- Website: `https://soumadipkaran.vercel.app`
- Location: Optional; only share if comfortable.

## Suggested pins

On https://github.com/souma888 choose **Customize your pins** and select:
`Tastera`, `TerraSight`, `Vectora`, `numpy-matrix-operations`, `Nexora`, and `Reparo`.

## Design notes

- Feature descriptions reflect the current project scope. Nexora and Reparo are marked as in planning.
- The portfolio URL and contact email are intentionally public in the README.
- GitHub Stats is a third-party service, so occasionally its cards may fail to render despite the profile README being available.
