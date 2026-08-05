# Contributing

Thank you for helping improve the Research Software Guidelines. Contributions can range
from fixing a typo to writing a new section. This document covers how the site is
built and the conventions to follow so changes stay consistent.

Where practical, this repository follows the practices the guide itself
recommends: see [Documentation & community](docs/best-practices/documentation-community.md)
and [Project identity & people](docs/best-practices/identity.md).

## Ways to contribute

- **Open an issue** for a correction, a suggestion, or a problem with the site.
  Use the issue templates so the maintainers get the details they need.
- **Open a pull request** for a concrete change. For anything large or structural
  (a new chapter, reorganizing the nav, changing the build), open an issue first
  so the approach can be agreed before you invest the effort.

## Development setup

```bash
git clone https://github.com/LUMC-DCC/rs-guidelines.git
cd rs-guidelines
pip install -e .
```

Preview the site locally with live reload (usually at http://127.0.0.1:8000):

```bash
rs-serve
```

`rs-serve` is a thin wrapper around `mkdocs serve`; you can also run `mkdocs`
directly. Before opening a PR, confirm a clean strict build:

```bash
mkdocs build --strict
```

## How the site is built

- **[MkDocs](https://www.mkdocs.org/)** with the **Material** theme renders the
  Markdown in `docs/` into the static site.
- Navigation is driven by **`.pages`** files (the `awesome-pages` plugin), not a
  `nav:` block in `mkdocs.yml`. To add or reorder pages, edit the relevant
  `.pages` file.
- **Build hooks** in [`hooks/`](hooks) inject single-sourced reference data at
  build time. Please verify you understand this before editing
  reference data.

### Single-sourced reference data

Some data lives in one place and flows into the pages automatically. Edit the
source and the change applies everywhere it is used. Never copy these values
inline.

| What | Source (edit here) | How it reaches the pages |
|---|---|---|
| Abbreviations | [`docs/resources/abbreviations.md`](docs/resources/abbreviations.md) | dotted-underline tooltips on every page (`hooks/abbreviations.py`) |
| LUMC contacts | [`docs/resources/contacts.md`](docs/resources/contacts.md) | a `{{token}}` (e.g. `{{rsd}}`) expands to the linked contact inline (`hooks/contacts.py`) |
| Organizations | [`docs/resources/organizations.md`](docs/resources/organizations.md) | one flat table (with a `Category` column) → categorized page (`hooks/organizations.py`) |

Other one-off inline links stay inline in the page they belong to.
Please centralize data that is *repeated across many pages* or needs *consistent structure*.

## Making a change

1. Branch from `main` (`main` is the deployed branch, pushes to it publish the
   site via [`.github/workflows/gh-pages.yml`](.github/workflows/gh-pages.yml)).
2. Make your change; keep one focused change per PR.
3. Run `mkdocs build --strict` and confirm it passes.
4. Open a pull request into `main`. The PR template's checklist covers the basics;
   CI runs a [link check](.github/workflows/links.yml) on the built site.
5. A maintainer reviews and merges. Merging to `main` deploys automatically.

Commit messages: short, imperative, and scoped (e.g. "fix broken link in risks").

## Code of conduct

Be respectful and constructive. Participation in this project is governed by the
project's `CODE_OF_CONDUCT.md`.

## License of contributions

The guide is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
By contributing, you agree that your contributions are licensed under the same
terms.
