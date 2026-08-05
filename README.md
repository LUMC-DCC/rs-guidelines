# Research Software Guidelines

[![GitHub Pages](https://img.shields.io/badge/view-docs-blue?logo=github)](https://lumc-dcc.github.io/rs-guidelines)

This repository contains the source code for the RS Guidelines site [lumc-dcc.github.io/rs-guidelines](https://lumc-dcc.github.io/rs-guidelines),
which provides a navigable approach to managing and developing research software. 


## Installation

### Clone and enter the repository

```bash
git clone https://git.lumc.nl/lumc-dcc/fair-software-stewardship/smp-fair-practices.git
cd smp-fair-practices
```

### Install dependencies

```bash
pip install -e .
```

This will install the project and its dependencies in editable mode, 
allowing you to make changes to the source code and have them reflected immediately. 
You only need to do this once, unless you change [pyproject.toml](pyproject.toml).


## Usage

This command will launch the MkDocs server and output the URL for accessing your documentation 
(usually http://127.0.0.1:8000):

```bash
rs-serve [OPTIONS]
```

You can find the options [here](https://www.mkdocs.org/user-guide/cli/#mkdocs-serve).


## Reference data & how to edit it

Some reference data is single-sourced and injected into the pages at build time
by hooks in [`hooks/`](hooks). Edit the source file and the change flows
everywhere it is used:

| What | Source | How it reaches the pages |
|---|---|---|
| Abbreviations | [`docs/resources/abbreviations.md`](docs/resources/abbreviations.md) | tooltips on every page (`hooks/abbreviations.py`) |
| LUMC contacts | [`docs/resources/contacts.md`](docs/resources/contacts.md) | `{{token}}` expands inline (`hooks/contacts.py`) |
| Organizations | [`docs/resources/organizations.md`](docs/resources/organizations.md) | flat table → categorised page (`hooks/organizations.py`) |

**Everything else — Further-reading lists, tool tables, one-off inline links —
stays inline in the page it belongs to.** The rule of thumb: centralise data
that is *repeated across many pages* or needs *consistent structure*; keep
single-use, context-specific references written inline where they are read.

External links are checked in CI by [`.github/workflows/links.yml`](.github/workflows/links.yml)
(internal LUMC hosts are skipped — see [`.lycheeignore`](.lycheeignore) — and must be checked manually).


## License

This work is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

## Maintainer

This project is maintained by [Mariia Steeghs-Turchina](mailto:m.a.steeghs-turchina@lumc.nl) (👤 Github [@thatmariia](https://github.com/thatmariia)).
For general questions about RS Guidelines or research software support at LUMC, contact us at [LUMCDCC@lumc.nl](mailto:LUMCDCC@lumc.nl)
