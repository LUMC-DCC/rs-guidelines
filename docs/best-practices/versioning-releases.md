# Versioning & releases

Versioning and releases are what turn a changing repository into something that can be cited, installed, audited, and reproduced. A research artefact that says "I used the code from the lab's GitHub" without naming a version is often not reproducible. The same project with tagged releases is.

Three habits do most of the work here:

1. Use **version control** from the first commit.
2. Use a **versioning scheme** that tells users what kind of change happened.
3. **Tag and release** at meaningful points, with notes that say what changed.

## Version control

For almost all research software, **Git** (or another version-control system) should be used from the start of active development. Version control gives you:

- a **history** of every change, with attribution and timestamps;
- **branches** for parallel work and **pull requests** for review;
- **tags** for releases;
- **rollback** when you make a mistake;
- a durable **collaboration record** that survives staff changes.

Alternatives to Git exist (Mercurial, Pijul, occasionally still SVN), but Git is the universal default and the tool that integrates with every modern forge and CI system. Pick something else only if you have a specific reason.

Adding Git to an existing folder takes under a minute - `git init`, `git add -A`, `git commit -m "Initial commit"`, and there is rarely a good reason to keep code without it.

For **commit messages**, the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification is a useful default: short, structured messages (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`...) that humans read easily and tools can parse to generate changelogs. It is not mandatory, but it is a low-cost discipline that pays back later.

## Versioning scheme

Use a versioning scheme that communicates the *nature* of each change. The two common choices for research software:

### Semantic Versioning (SemVer)

`MAJOR.MINOR.PATCH`, with the rules:

- **PATCH** - bug fix, no intended change in behaviour or API. Safe to upgrade.
- **MINOR** - new, **backwards-compatible** feature. Safe to upgrade.
- **MAJOR** - breaking change. Read the release notes before upgrading.

SemVer is the right choice for **libraries** and **APIs**, anything where users write code against a stable interface. The full specification is at [semver.org](https://semver.org/).

A nuance often missed: a 0.x.y version means **the API is not yet stable**. Many research projects sit at 0.x for years and that is fine, but consider tagging a 1.0.0 when the interface stabilises.

### Calendar Versioning (CalVer)

`YYYY.MM`, `YYYY.MM.DD`, or `YY.MM.PATCH`. The version *is* the release date.

CalVer suits **pipelines**, **data products**, **operational tools**, and **CLIs** without a stable user-facing API, where "what version are you on?" is essentially "when did you install it?". CalVer is also useful when releases follow a regular cadence (monthly, quarterly).

### Date + build/revision

For internal workflows where releases are frequent and informal, `YYYY-MM-DD.<short-sha>` style tags are sometimes used. This works for internal reproducibility but is weak for public reuse, users cannot easily compare two such versions.

### Tagging conventions

Use Git tags such as `v1.2.0` (the `v` prefix is conventional in Git releases and helps distinguish version tags from branch names). Avoid ambiguous tag names (`final`, `latest`, `paper-version`, `paper-version-2`, `paper-version-NEW`). These names are real, they happen, and they cause real confusion six months later.

> **In the SMP:** the Versioning scheme field is free text. State the scheme (e.g., "SemVer").

## Releases

A *release* is more than a tag. A complete release includes:

- a **Git tag** on the relevant commit (immutable);
- **release notes** describing what changed;
- a **package or container artefact**, if applicable (published to the relevant registry);
- an **archived source snapshot** (typically pushed to Zenodo automatically; see [Sharing & licensing](sharing-licensing.md));
- a **DOI** for public research software;
- **updated citation metadata** (`CITATION.cff` reflecting the new version and DOI);
- **passing CI**.

The recommended workflow is straightforward:

1. Make sure CI is green on the commit you intend to release.
2. Update `CHANGELOG.md` (see below).
3. Tag the commit: `git tag -a v1.2.0 -m "..."`, then `git push --tags`.
4. Create a **GitHub Release** (or GitLab Release) from the tag, pasting the changelog entry into the release notes.
5. Zenodo (if connected) automatically archives the release and mints a DOI.
6. Optionally, your CD pipeline publishes the package to PyPI/conda-forge/etc., and pushes a container image to a registry.

For internal scripts that genuinely are never reused, "no releases" is acceptable but weak. Even for those, a periodic `git tag` to mark a state used for a paper is good practice.

GitHub has a clean reference: [About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases).

> **In the SMP:** the Software releases question is binary, with a follow-up on **release frequency** (on demand, after each major feature, after bug fixes, on schedule, single release).

## Changelog and release notes

A **changelog** explains what changed between versions, in a format readable by both humans and tools. The canonical format is [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), a single `CHANGELOG.md` file (see [Documentation & community](documentation-community.md)) with sections per release, and entries grouped under:

- **Added**
- **Changed**
- **Deprecated**
- **Removed**
- **Fixed**
- **Security**

[Common Changelog](https://github.com/vweevers/common-changelog) is a stricter subset of Keep a Changelog, useful when you want machine-parseable changelogs.

If you use [Conventional Commits](https://www.conventionalcommits.org/), the changelog can be partly auto-generated. Tools like [`git-cliff`](https://git-cliff.org/), [`release-please`](https://github.com/googleapis/release-please), or [`semantic-release`](https://semantic-release.gitbook.io/) parse commit messages and produce a draft changelog. See [A Beginner's Guide to Git - What is a Changelog and How to Generate It](https://www.freecodecamp.org/news/a-beginners-guide-to-git-what-is-a-changelog-and-how-to-generate-it/) for the basics.

**Release notes** can be shorter: the human-friendly highlights from the changelog, plus any migration guidance for breaking changes. For libraries, name the breaking changes explicitly; for tools, note any new flags or output changes.

## Software packaging and distribution

Decide *how users install your software* and design the distribution accordingly. The right channel depends on the audience.

Common patterns:

- **Language package manager.** [PyPI](https://pypi.org/) and [conda-forge](https://conda-forge.org/) for Python; [CRAN](https://cran.r-project.org/) and [Bioconductor](https://www.bioconductor.org/) for R; [npm](https://www.npmjs.com/) for JavaScript; [crates.io](https://crates.io/) for Rust. The right answer when the audience is developers comfortable in that language.
- **Container image.** [Docker Hub](https://hub.docker.com/), [GitHub Container Registry](https://ghcr.io/), [Quay](https://quay.io/), Apptainer Library, [Biocontainers](https://biocontainers.pro/). The right answer for pipelines, end-user tools, and clinical-adjacent software.
- **Source-only.** `git clone && pip install -e .`, build-from-source instructions. Acceptable for libraries with no binary artefacts and a developer audience.
- **Self-hosted installer** - uncommon in research software outside of niche fields.
- **Hosted as a service** - for software where the user *calls your API* rather than installing anything. Documentation, authentication, and uptime become important concerns.

A reasonable rule of thumb: a developer can `pip install` a library; a clinician should not have to. Match the packaging to who the user actually is.

> **In the SMP:** the Software packaging question is binary. The follow-up captures *distribution channels* as a free-text field; list each channel where the software is or will be available.

## Containerisation

Containerisation packages the runtime environment, not just the code. See Containerisation under [Interoperability](interoperability.md).

## Dependency update policy

Dependencies change. Plan how the project handles updates *before* something breaks at an inconvenient moment.

A policy with five elements is usually enough:

- **Update frequency** - weekly, monthly, per release, or security-only.
- **Automation** - [Dependabot](https://docs.github.com/en/code-security/dependabot), [Renovate](https://docs.renovatebot.com/), GitLab's built-in dependency scanning.
- **Review requirement** - CI must pass, plus optionally a maintainer review.
- **Pinning strategy** - permissive ranges in the manifest (`>=2.1,<3.0`), exact versions in the lock file. This is the standard pattern and is what most modern dependency tools default to.
- **Emergency path for security fixes** - what does the team do when a high-severity CVE drops? For Level C, name a severity threshold (e.g., CVSS ≥ 7) and a response time (e.g., five working days).

A small note on the relationship to license-compatibility checks (covered in [Sharing & licensing](sharing-licensing.md)): every dependency update is an opportunity for a license to change.

## Further reading

- [Semantic Versioning](https://semver.org/) - full specification.
- [Calendar Versioning](https://calver.org/) - for time-driven projects.
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) - commit-message convention with tooling support.
- [Keep a Changelog](https://keepachangelog.com/) - changelog format.
- [GitHub - About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) - practical reference on tagging, release notes, and assets.
- [Zenodo–GitHub integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) - automatic archiving and DOI minting at release time.
- [The Turing Way - Reproducible environments](https://book.the-turing-way.org/reproducible-research/renv) - good orientation across lock files, containers, and whole-environment tools.