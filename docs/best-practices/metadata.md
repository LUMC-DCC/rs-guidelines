# Software metadata

Structured metadata makes your software findable, citable, and reusable. This page explains which metadata files belong in a research software repository, why they matter, and how to create, check, and maintain them. The field-by-field reference lives in the {{codemeta-profile}}, so that this page and the profile cannot drift apart.

This page focuses on the metadata *files* themselves. For the surrounding decisions, see the guidance on choosing a [repository](sharing-licensing.md#repository) and [license](sharing-licensing.md#software-license), minting [persistent identifiers](sharing-licensing.md#persistent-identifiers), picking [registries](sharing-licensing.md#registries), and recording [programming languages](interoperability.md#programming-languages) and [data formats](interoperability.md#input-and-output-data-formats).

## Quick start

Add two files to the root of your repository:

- **`codemeta.json`** — the primary metadata record, harvested by registries and archives
- **`CITATION.cff`** — a citation-specific file that GitHub and Zenodo render automatically

The LUMC {{rs-metadata}} tool creates both and checks them:

```bash
pip install rs-metadata
rs-metadata init       # writes codemeta.json, CITATION.cff, and a CI workflow
rs-metadata validate   # checks them against the LUMC CodeMeta profile
```

`init` infers what it can from your packaging metadata (`pyproject.toml`, `package.json`, `DESCRIPTION`, `Cargo.toml`, `Project.toml`) and the git remote, and leaves a placeholder wherever it could not. **Replace every placeholder before you publish.** `validate` reports leftovers as errors, because a placeholder is worse than a missing field: it asserts an identifier that does not exist, and registries ingest it anyway.

You can also write both files by hand. Start from the {{codemeta-examples}}, or use the [CodeMeta generator](https://codemeta.github.io/create/) and [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/).

## Why metadata matters

Three purposes, in increasing order of ambition.

**Citability.** A `CITATION.cff` file enables GitHub to show a "Cite this repository" button and allows Zenodo to auto-populate citation records. Without it, users either cite only the associated paper (losing credit for the software itself) or cite the repository URL in a way that is not persistent or versioned.

**Discoverability.** A complete `codemeta.json` is harvested by Zenodo, Software Heritage, the Research Software Directory, and other archives, making your software visible in search results and institutional inventories. EDAM operation terms enable semantic discovery in bio.tools and other life-sciences registries.

**Reuse.** Machine-readable metadata allows automated tools to verify compatibility, resolve dependencies, and reproduce computational environments, which is the practical foundation for genuinely reusable research software.

## The two files

### `codemeta.json`

CodeMeta is a software metadata vocabulary built on schema.org and represented in JSON-LD. It is the primary record: the file registries and archives read. A working group of LUMC, Amsterdam UMC, DReaMS, and ELIXIR-NL scored five candidate standards (CodeMeta, CITATION.cff, Bioschemas, biotoolsSchema, and maSMP) against a weighted rubric that prioritized reuse over discoverability over citability; CodeMeta ranked first. See {{metadata-standards-choice}} for the criteria and the scores.

LUMC defines a profile of CodeMeta v3.1 — the {{codemeta-profile}} — which sets a mandatory minimum and highlights the most useful optional fields. Any valid CodeMeta field is welcome; the profile constrains rather than restricts.

### `CITATION.cff`

CITATION.cff is a YAML file focused on citation. GitHub renders it as a "Cite this repository" button, and Zenodo uses it to populate citation records when a release is archived. It is simpler to write than `codemeta.json` and is native to the GitHub interface.

It has no fields for programming language, software type, or operations, so it is **not** a replacement for `codemeta.json`. Maintain both, and keep name, version, and authors consistent between them — `rs-metadata validate` checks exactly that.

## What goes in them

Ten fields are mandatory under the LUMC profile:

`name`, `description`, `version`, `identifier`, `author`, `license`, `codeRepository`, `programmingLanguage`, `applicationCategory`, and `schema:featureList` (what the software does, EDAM terms preferred).

A further fifteen are recommended, covering release dates, keywords and topics, documentation and issue-tracker URLs, maintainers, funding, related publications, support status, platforms, dependencies, supporting data, containers, changelogs, and continuous integration.

For what each field means, which values are accepted, and how they are constrained, see the {{codemeta-profile}}. A few of the underlying decisions are covered elsewhere in this guide: [software title](identity.md#software-title), [software license](sharing-licensing.md#software-license), [persistent identifiers](sharing-licensing.md#persistent-identifiers), and [functions and operations](interoperability.md#functions-operations).

Note that EDAM-typed **inputs and outputs** have no CodeMeta or schema.org field. If you need them recorded, define them in bio.tools (see [Registering your software](#registering-your-software)).

## When to update

Update both files when you:

- Create a new release (`version`, `identifier`, `datePublished`)
- Add or change authors
- Change the license
- Move the repository
- Change the software's primary function

## Validation

`rs-metadata validate` runs two checks:

- **Schema validation** — that `codemeta.json` conforms to the {{codemeta-profile}} and that `CITATION.cff` is valid CFF 1.2.0.
- **Consistency** — that the shared fields (name, version, authors) agree between the two files and your packaging metadata.

Run it locally while you edit, and in CI on every push and pull request. `rs-metadata init` writes a `.github/workflows/metadata.yml` that does exactly that; the project is also published as a GitHub Action, so an existing workflow can call it directly.

## Registering your software

For where to register and how to choose, see [Registries](sharing-licensing.md#registries). Two registries interact directly with your metadata files:

- **[bio.tools](https://bio.tools/)** — a popular registry for life-sciences tools. A documented CodeMeta–biotoolsSchema crosswalk means most fields map conceptually, though the [bridge tool](https://github.com/bio-tools/biohackathon2025) currently registers from a GitHub repository rather than from `codemeta.json`. After registering, add the bio.tools ID to **both** files.
- **[Research Software Directory](https://research-software-directory.org/)** — the national Dutch registry. It ingests `codemeta.json` from GitHub automatically, so a complete file is the main prerequisite.

## Tools

| Tool | Purpose | Link |
|---|---|---|
| rs-metadata | Create and validate both files against the LUMC profile | {{rs-metadata}} |
| CodeMeta generator | Interactive `codemeta.json` authoring | [codemeta.github.io/create](https://codemeta.github.io/create/) |
| cffinit | Interactive `CITATION.cff` authoring | [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/) |
| EDAM Browser | Browse and search EDAM terms | [edam-browser](https://edamontology.github.io/edam-browser/) |
| Zenodo–GitHub integration | Automatic DOI minting for releases | [GitHub docs](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) |

## Further reading

- {{codemeta-profile}} — the full field reference
- [CodeMeta user guide](https://codemeta.github.io/user-guide/)
- [CITATION.cff specification and schema guide](https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md)
- [EDAM ontology documentation](https://edamontology.org/page)
- [bio.tools curator guide](https://biotools.readthedocs.io/en/latest/curators_guide.html)
- [RDMkit — documentation and metadata](https://rdmkit.elixir-europe.org/metadata_management)
