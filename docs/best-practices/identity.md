# Project identity & people

Before anything technical, a software project needs a name, a small set of named humans, and a clear statement of whether any external regime governs it.

## Software title

A title is the public name of the software. It travels everywhere: in citations, in the URL of your repository, in package indices, in `pip install <name>` commands, in `import` statements, in slide titles, in Google searches by future users. Renaming later is expensive, and there will be old papers and stale links forever.

A good title is **specific**, **unique**, and **short**:

- *Specific.* Someone who has never heard of your project should be able to guess, within one sentence, what it is broadly about. "ALSGenoTyper" tells you something; "Project Phoenix" tells you nothing.
- *Unique.* Before you finalise a public name, search the places where collisions may occur: GitHub and GitLab, [PyPI](https://pypi.org/), [conda-forge](https://conda-forge.org/), CRAN, Bioconductor, [bio.tools](https://bio.tools/), Zenodo, and Google. Generic names, such as "Pipeline", "Tools", "Analyzer", almost always collide and usually with something better-funded than you.
- *Short.* Long enough to be informative; short enough to fit on a CLI prompt, in a citation key, and in a project banner.

Common pitfalls worth avoiding:

- **Internal codenames as public titles.** Pet names or supervisor's coffee orders are fine in private; rename before publishing.
- **Naming after the cohort or department only.** "ALS-tool" and "LUMC-Pathology" are hard to disambiguate at scale, even within LUMC.
- **Putting the version in the name.** `MyTool2`, `MyToolPro`, `MyToolFinal`. Versions belong in tags, not in names.

If the project might in the future be renamed (this happens), keep the *name* and *identifier* layers separate: the GitHub repo URL, the package name, the documentation site, and the DOI on Zenodo are all things that can be migrated cleanly if the title is the only fixed point.

> **In the SMP:** the Title field should contain the final public name as it would appear in publications or presentations.

## Authors vs. maintainers

In research software, two roles get conflated and then confused. The SMP separates them deliberately.

- **Authors** are people who made scholarly or creative contributions to the software. They go into `CITATION.cff`, into Zenodo deposits, and onto publications. A reasonable test: would they appear on the paper that describes the software, if you wrote that paper today? If yes, they are authors.
- **Maintainers** are people responsible *now*, for *this version*: the repository, releases, issue triage, support, and continuity. A maintainer must be reachable; an author from three years ago need not be.

In most projects, **maintainers ⊆ authors ⊊ contributors**: every maintainer is an author, every author is also (trivially) a contributor, but plenty of contributors (who fixed a typo, opened a useful issue, reviewed a PR) are neither authors nor maintainers.

### Why at least two maintainers

The single most common failure mode of research software is: the only person who knew how it worked left. A second maintainer with repository/admin access can:

- triage issues while the primary is on leave or no longer at LUMC;
- review and merge pull requests, so the project is never bottlenecked on one person;
- keep the project from quietly orphaning when someone moves jobs.

The backup maintainer does not need to be the same person across the lifetime of the project, but at every moment there should be two. If you cannot find a second maintainer at LUMC, consider whether your supervisor or a collaborator with adjacent skills can serve in that role.

### ORCID, affiliation, and contact

For every author and maintainer, record at least full name, affiliation, and a contact route. [ORCID iDs](https://orcid.org/) are strongly recommended as they survive name changes, affiliation changes, and disambiguate people who share names. Zenodo, GitHub, and ORCID can be linked so that a release automatically credits the right people on a Zenodo deposit.

> **In the SMP:** the Authors list captures credit; the Maintainers list captures responsibility. Both will appear in `CITATION.cff` (see [Sharing & licensing](sharing-licensing.md)). Aim for at least two maintainers.

## Funding and project context

Recording the funder, grant number, PI, and internal LUMC project code seems bureaucratic until you need it for a Zenodo deposit, a funder report, or a hand-over.

> **In the SMP:** the Funding section captures funder name, project title (often a working acronym), grant/internal code, and PI(s). Repeat for each distinct funding source. Use the legal-entity name (e.g., "ZonMw", not "ZM"; "Horizon Europe", not "HE").

## The regulated-software flag

Tick the regulated-software flag if your software is (or might plausibly become) subject to a legal, clinical, institutional, or sector-specific regulatory regime. Be conservative. The flag does not mean "we are compliant". It means "this project needs regulatory attention".

Common situations at LUMC that should trigger the flag:

- The software is or will be a **Software as a Medical Device (SaMD)**, IVD product, or otherwise covered by **MDR**, **IVDR**, **FDA**, or comparable rules.
- The software is or will be **clinical decision support**: anything that influences diagnosis, treatment, monitoring, or triage.
- The software is part of a **validated laboratory workflow** (ISO 15189, ISO 13485, IEC 62304, ISO 14971).
- The software runs under departmental SOPs that have regulatory implications.
- The software falls under **NEN 7510** (Dutch information-security standard for healthcare) or comparable institutional security requirements.

A research prototype can become regulated when it starts influencing decisions about real patients. Re-evaluate the flag whenever the project's scope materially changes.

If the flag is set, the SMP is *not* a substitute for the regulatory artefacts you will need: IEC 62304 software life-cycle records, ISO 14971 risk file, MDR/IVDR technical file, and so on. Contact <LUMC legal> early.

> **In the SMP:** answer "Yes" if any regulatory regime applies *now or is plausible during the project's lifetime*. The SMP captures only the fact that the regime applies; the regulatory documentation lives elsewhere.

## Further reading

- [ORCID](https://orcid.org/) - persistent author identifier.
- [Contributor Roles Taxonomy (CRediT)](https://credit.niso.org/) - a vocabulary for describing who did what on a research output. Useful when filling in author roles in `CITATION.cff` or in funder reports.
- [Citation File Format (`CITATION.cff`)](https://citation-file-format.github.io/), see [Sharing & licensing](sharing-licensing.md).
- <LUMC legal> (internal) for SaMD/MDR/IVDR questions.
