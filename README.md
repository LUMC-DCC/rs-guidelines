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


## License

This work is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

## Maintainer

This project is maintained by [Mariia Steeghs-Turchina](mailto:m.a.steeghs-turchina@lumc.nl) (👤 Github [@thatmariia](https://github.com/thatmariia)).
For general questions about RS Guidelines or research software support at LUMC, contact us at [LUMCDCC@lumc.nl](mailto:LUMCDCC@lumc.nl)
