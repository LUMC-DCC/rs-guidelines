# Documentation & community

A lack of documentation is the most frequently cited reason for research software becoming unsable. The code keeps working; the knowledge of *how to use it* dissipates the moment the original author moves on.

This chapter is about the documentation and the social structures around the code: what users need to know, what the next developer needs to know, and how the community around the project organises itself.

## Three audiences

Documentation falls roughly into three layers, each for a different reader:

1. **User documentation** - for the person who runs your software. They want to install it, run an example, and get answers to their questions.
2. **Deployment documentation** - for the person who has to *make it work* in a new environment. Often the same person as the user; sometimes a sysadmin, an IT&DI engineer, or a future you on a new machine.
3. **Developer documentation** - for the person who has to *change the code*. That is almost certainly a future colleague; possibly a community contributor; very likely a future you who has forgotten how the project is structured.

These three layers overlap, but they answer different questions.

## User documentation

Every project, regardless of level, needs a `README` that answers, preferably, all the following:

1. **What is this software?** One sentence.
2. **Who is it for?** Audience and prerequisites.
3. **How do I install it?** A copy-pasteable command, or a link to the installation section.
4. **How do I run a minimal example?** A working example, not a placeholder.
5. **Where are the full docs?** A link to the documentation site, if there is one.
6. **How do I cite it?** A reference to `CITATION.cff` or a citation block.
7. **What is the license?** A pointer to `LICENSE`.
8. **Where do I get help?** Issue tracker, email, mailing list, helpdesk, or community Q&A forums.

For Level B and C, a README is often not enough. Add a proper documentation site once the README starts being more than a single screen. Common, well-supported choices:

- [**MkDocs**](https://www.mkdocs.org/) - fast, simple, Markdown-only. The Material theme is the de-facto default for many research projects.
- [**Sphinx**](https://www.sphinx-doc.org/) with the [**MyST**](https://myst-parser.readthedocs.io/) parser - Markdown plus reStructuredText, great for Python projects that need API reference; the standard for scientific Python.
- [**Quarto**](https://quarto.org/) - integrates well with R, Julia, and Python notebooks; good when documentation includes executable code.
- [**pkgdown**](https://pkgdown.r-lib.org/) - purpose-built for R packages.
- [**Docusaurus**](https://docusaurus.io/) - React-based; common for JavaScript projects with marketing-style landing pages.

Documentation sites are usually hosted on **Read the Docs** (free for open-source projects, with versioned builds), **GitHub Pages**, or **GitLab Pages**.

If you write only one section thoroughly, write the "getting started in 10 minutes" one.

### The community wisdom on documentation

A great deal of collective wisdom is collected at [Write the Docs - Software documentation guide](https://www.writethedocs.org/guide/). It covers everything from voice and tone to information architecture; worth reading once even if you do not act on all of it.

For API documentation specifically:

- [**Sphinx**](https://www.sphinx-doc.org/) with [`autodoc`](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) and [`napoleon`](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/) - the Python standard.
- [**Redoc**](https://redocly.com/redoc/) or [**Swagger UI**](https://swagger.io/tools/swagger-ui/) - for REST APIs documented with OpenAPI.
- Language-native generators: `rustdoc` (Rust), `pkgdown` (R), `JSDoc` (JavaScript), `Javadoc` (Java), `Doxygen` (C/C++).

> **In the SMP:** the User documentation question distinguishes three states - *full docs* (a site), *README only*, and *no docs*. Level A projects often legitimately stop at a good README. For Level B and C, "README only" is a limitation.

## Deployment & dependency documentation

Deployment documentation tells someone how to install, configure, and run the software *in their environment*. For reproducible research, users should not have to infer environment requirements from source code.

A useful deployment section covers:

- **Supported platforms** - OS, architecture, language version constraints.
- **Install command** - exact, copy-pasteable. Multiple paths if the audience needs them (pip vs. conda; Docker vs. source).
- **Required configuration** - environment variables, config files, paths.
- **Test command** - how to verify the install worked.
- **Known setup problems** - common pitfalls and their fixes.

The *machine-readable* part of deployment (`pyproject.toml`, `requirements.txt`, `environment.yml`, `Dockerfile`, `Cargo.lock`, `renv.lock`) lives in the repository and is captured in the [Interoperability](interoperability.md) chapter. The *human* instructions live in the documentation.

> **In the SMP:** the Deployment documentation question simply asks whether it exists, with a URL. The machine-readable manifests are captured separately.

## Developer documentation

Developer documentation helps the next person change the code safely. A minimal developer guide covers:

- **Repository layout** - what is in which directory, and why.
- **How to create a development environment** - provide exact commands, not just a vague reference to `requirements.txt`.
- **How to run the tests** - the command, plus any setup quirks.
- **How to add a feature** - a worked example or a pointer to "good first issues".
- **Code style and linting** - which tools and rules are used, and when to run them (see [Testing & quality](testing-quality.md)).
- **Release process** - who can cut a release, which checks must pass, and how the tag is created (see [Versioning & releases](versioning-releases.md)).
- **Architecture notes** - short rationale for non-obvious design decisions.

For libraries, generated API reference can count as developer documentation, but only if it is complete enough to help a new contributor. A wall of auto-generated function signatures with one-line docstrings is not sufficient developer documentation.

### Contributing guidelines

A `CONTRIBUTING.md` file explains how outsiders (and forgetful insiders) should contribute. It includes:

- how to open an issue (link to templates);
- how to set up a development environment;
- how to run tests;
- branch and pull request (PR) expectations (branch naming, target branch, commit-message conventions);
- review process and timelines;
- coding style and linting;
- whether external contributions require a CLA, DCO, or attribution.

The GitHub guide on [setting guidelines for repository contributors](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors) is a solid reference.

### Code of conduct

For any project that accepts external contributions, or that might in the future, a `CODE_OF_CONDUCT.md` is recommended. For Level C and often public Level B projects, it should be present.

The [Contributor Covenant](https://www.contributor-covenant.org/) is the de-facto default; GitHub provides a template under [Adding a code of conduct to your project](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project). Pick a version (2.1 is current at the time of writing), specify the contact channel for reports, and link to it from the README.

### Changelog

A `CHANGELOG.md` makes version history human-readable. The standard format is [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), with sections:

- **Added** - new features.
- **Changed** - changes to existing functionality.
- **Deprecated** - features marked for removal in a future version.
- **Removed** - features removed in this version.
- **Fixed** - bug fixes.
- **Security** - security-relevant fixes.

[Common Changelog](https://github.com/vweevers/common-changelog) is a stricter subset, useful if you want machine-parseable changelogs. For details on generating changelogs from Git history, see [A Beginner's Guide to Git - What is a changelog and how to generate it](https://www.freecodecamp.org/news/a-beginners-guide-to-git-what-is-a-changelog-and-how-to-generate-it/).

Short changelog entries are fine. See also the [Versioning & releases](versioning-releases.md) chapter.

> **In the SMP:** the Developer documentation block captures the documentation URL, the API-reference URL (if separate), `CONTRIBUTING`, `CODE_OF_CONDUCT`, and `CHANGELOG`. Each is a URL to the relevant file in the repository or documentation site.

## Bug reporting & feature requests

Users and collaborators need a clear route to report bugs, request features, and ask support questions. For most projects, the right answer is the issue tracker on GitHub or GitLab, with [issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) that prompt for the information you actually need.

Email-only support is acceptable for Level A. For Level B/C it is weak because reports are not visible or searchable, and they disappear when the relevant inbox owner moves on.

A useful bug-report template asks for:

- **Expected behaviour.**
- **Actual behaviour.**
- **Steps to reproduce** - including input, command, and environment.
- **Software version** and **operating system / environment**.
- **A minimal example input** if possible.

A feature-request template asks:

- the **user need** in plain language;
- the **expected benefit**;
- **possible alternatives** the requester has considered;
- whether the requester **can contribute**;
- **urgency**.

For Level B/C, define a small set of labels (`bug`, `enhancement`, `documentation`, `security`, `good first issue`, `wontfix`) and use them consistently. GitHub's [About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) covers configuration; the same concepts apply to GitLab.

> **In the SMP:** the Bug reporting question expects at least one concrete system or contact route, with a URL. "Email the maintainer" is acceptable for Level A; not enough for Level B/C.

## Governance

Governance describes how decisions are made when contributors disagree, who handles releases and security disclosures, and what the conflict-resolution path is. For small projects, governance can be short:

> The primary maintainer decides releases. Non-trivial changes require review by the backup maintainer. Scientific changes require review by the domain expert.

Larger projects need more. A useful governance document specifies:

- **Maintainers** and their responsibilities.
- **Release manager(s)** - who can create a release.
- **Security contact** - usually pointed to by `SECURITY.md`.
- **Steering group**, if any - composition and decision rights.
- **Decision-making model** - lazy consensus, BDFL ("benevolent dictator for life"), formal voting, or a hybrid.
- **Conflict resolution** - what happens when contributors disagree and lazy consensus fails.
- **Succession** - how a new maintainer is added or removed.

Research-software projects often use **lazy consensus** for routine changes (a PR is merged if no maintainer objects within a stated window) and explicit escalation for substantive or contested changes. Make that explicit so contributors know which kind of change theirs is.

> **In the SMP:** the Governance field is a single free-text question. For smaller projects, one or two sentences suffice. For Level C, expect a paragraph or a link to a governance document in the repository.

## Further reading

- [Write the Docs - Software documentation guide](https://www.writethedocs.org/guide/) - broad, community-built reference on documentation craft.
- [The Turing Way - Communication and reporting](https://book.the-turing-way.org/communication/communication) - chapters on accessible documentation, citation, and persistent links.
- [Diátaxis](https://diataxis.fr/) - a clean framework for thinking about documentation in four modes (tutorials, how-tos, reference, explanation). Genuinely useful when you cannot decide where a piece of documentation belongs.
- [Open Source Guides - Starting an open source project](https://opensource.guide/starting-a-project/) - practical, especially for the social and community side.
- [Contributor Covenant](https://www.contributor-covenant.org/) - code-of-conduct template.
- [Keep a Changelog](https://keepachangelog.com/) - changelog conventions.