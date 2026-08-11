# Software metadata

Structured metadata makes your software findable, citable, and reusable. This page explains what metadata to add to your research software repository, why each field matters, and how to create and maintain the required files. The guidance is layered: the quick start covers the minimum steps, and each subsequent section provides more technical detail for those who need it.

This page focuses on the metadata *files* themselves. For the surrounding decisions, see the guidance on choosing a [repository](sharing-licensing.md#repository) and [license](sharing-licensing.md#software-license), minting [persistent identifiers](sharing-licensing.md#persistent-identifiers), picking [registries](sharing-licensing.md#registries), and recording [programming languages](interoperability.md#programming-languages) and [data formats](interoperability.md#input-and-output-data-formats).

## Quick start

Add two files to the root of your repository:

- **`codemeta.json`** — the primary metadata record, covering all required and recommended fields
- **`CITATION.cff`** — a citation-specific file that GitHub and Zenodo render automatically

If you only have five minutes: fill in the mandatory fields listed in the [field reference](#mandatory-fields) and commit.

> **Planned tooling.** A LUMC research-software template repository (`<template-repo>`), generated from your SMP, will ship both files pre-filled and validate them automatically in CI. Until that gets released, create and maintain the files manually as described below.

## Purpose of software metadata

Metadata serves three purposes, in increasing order of ambition.

**Citability.** A `CITATION.cff` file enables GitHub to show a "Cite this repository" button and allows Zenodo to auto-populate citation records. Without it, users either cite only the associated paper (losing credit for the software itself) or cite the repository URL in a way that is not persistent or versioned.

**Discoverability.** A complete `codemeta.json` is harvested by Zenodo, Software Heritage, the Research Software Directory, and other archives, making your software visible in search results and institutional inventories. EDAM operation terms enable semantic discovery in bio.tools and other life-sciences registries.

**Reuse.** Machine-readable metadata allows automated tools to verify compatibility, resolve dependencies, and reproduce computational environments, which is the practical foundation for genuinely reusable research software.

## The two metadata files

### `codemeta.json`

CodeMeta is a software metadata vocabulary built on schema.org and represented in JSON-LD format. It serves as the primary metadata record and is consumed by the widest range of repositories and tools. LUMC selected it from several software-metadata standards (Bioschemas, biotoolsSchema, and others) for its breadth and crosswalks (see `<metadata-standards-explanation>` for the selection procedure). LUMC defines a specific profile of CodeMeta v3.1 (`<codemeta-schema-repo>`) that specifies which fields are mandatory and what constraints apply. The mandatory and recommended fields below are a curated subset: any valid CodeMeta field is welcome — the profile only sets a mandatory minimum and highlights the most useful optional ones.

A minimal valid `codemeta.json`:

```json
{
  "@context": ["https://w3id.org/codemeta/3.1", "https://schema.org/"],
  "@type": "SoftwareSourceCode",
  "name": "MyTool",
  "description": "A tool for aligning short sequencing reads to a reference genome.",
  "version": "1.3.0",
  "identifier": "https://doi.org/10.5281/zenodo.1234567",
  "author": [
    {
      "@type": "Person",
      "@id": "https://orcid.org/0000-0000-0000-0000",
      "givenName": "Jane",
      "familyName": "Doe",
      "affiliation": {
        "@type": "Organization",
        "name": "Leiden University Medical Center"
      }
    }
  ],
  "license": "https://spdx.org/licenses/Apache-2.0",
  "codeRepository": "https://github.com/lumc/mytool",
  "programmingLanguage": ["Python"],
  "applicationCategory": "Command-line tool",
  "schema:featureList": [
    "http://edamontology.org/operation_3198"
  ]
}
```
The schema repository provides further worked examples (`<codemeta-schema-examples>`) of filled-in files, from minimal to complete, to use as references.

Use the [CodeMeta generator](https://codemeta.github.io/create/) to create your file interactively, or copy and adapt an existing one.

#### What is `@context`?

JSON-LD documents carry a `@context` declaration that maps property names to globally unique identifiers (URIs). This is what makes the file machine-readable in a standardized way: a tool reading your file knows that `name` means `https://schema.org/name`, not something else. The CodeMeta context (`https://w3id.org/codemeta/3.1`) defines the software-metadata vocabulary.

CodeMeta is built on schema.org: almost every field on this page is part of the CodeMeta v3.1 vocabulary and is written plain (no prefix), whether it originated in schema.org (`name`, `version`, `keywords`, `applicationCategory`, `runtimePlatform`, `operatingSystem`, `softwareRequirements`, `supportingData`) or is a CodeMeta-defined extension (`maintainer`, `referencePublication`, `developmentStatus`, `contIntegration`, `issueTracker`). The one exception is `featureList`, a schema.org property **not** included in the CodeMeta context — recording operations therefore uses `schema:featureList` and requires adding the schema.org context as a second entry. This is the sole reason for the dual context. Tools that generate the file include it by default; if you write the file by hand, keep both entries.

### `CITATION.cff`

CITATION.cff is a YAML file focused on citation. GitHub renders it as a "Cite this repository" button, Zenodo uses it to populate citation records when a release is archived. It is simpler to write than `codemeta.json` and is native to the GitHub interface.

A minimal `CITATION.cff`:

```yaml
cff-version: 1.2.0
title: MyTool
message: "If you use this software, please cite it using the metadata in this file."
type: software
authors:
  - family-names: Doe
    given-names: Jane
    orcid: https://orcid.org/0000-0000-0000-0000
    affiliation: Leiden University Medical Center
version: 1.3.0
date-released: 2026-06-01
doi: 10.5281/zenodo.1234567
repository-code: https://github.com/lumc/mytool
license: Apache-2.0
```

Use [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/) to generate this file interactively, or copy and adapt an existing one.

Note that CITATION.cff does not have fields for programming language, software type, or operations. It is not a replacement for `codemeta.json`; maintain both files, keeping name, version, and authors consistent between them.

## Mandatory fields

The following CodeMeta fields are required in every LUMC research software repository; each must be present and non-empty.

Several fields can hold more than one value — provide these as a JSON array. In this reference, the fields that accept multiple values are `identifier`, `author`, `license`, `programmingLanguage`, `applicationCategory`, `schema:featureList` (operations), `keywords`, `maintainer`, `funding`, `referencePublication`, `operatingSystem`, `softwareRequirements`, `supportingData`, and `runtimePlatform`. A single value may be written either as a plain string or as a one-element array.

### Name: `name`

The name of your software, exactly as it should appear in citations and search results.

```json
"name": "MyTool"
```

Avoid version numbers or institutional qualifiers in the name itself.

### Description: `description`

A few sentences describing what the software does. Write for a reader outside your immediate research group: what problem does it solve, and at what level of abstraction?

```json
"description": "A command-line tool for variant calling in whole-genome sequencing data, optimized for low-coverage samples."
```

### Version: `version`

The version of the software this metadata file describes.

```json
"version": "2.1.0"
```

Prefer [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`) for any software that has formal releases. For scripts or notebooks without a release, the full Git commit hash is also acceptable:

```json
"version": "a3f8c2d1b4e7f0291a3f8c2d1b4e7f0291a3f8c2"
```

Update this field on every new release.

### Persistent identifier: `identifier`

A versioned, persistent identifier for this specific release. This is what others should cite when referring to a particular version of your software.

```json
"identifier": "https://doi.org/10.5281/zenodo.1234567"
```

For how to mint one, see [Persistent identifiers](sharing-licensing.md#persistent-identifiers). For scripts or internal tools that will not be formally published, a Git tag URL is acceptable:

```json
"identifier": "https://github.com/lumc/myscript/tree/v1.0"
```

### Authors: `author`

The people responsible for creating the software. Include an ORCID identifier for each author; this is what links software citation to researcher profiles and enables use in research assessments.

```json
"author": [
  {
    "@type": "Person",
    "@id": "https://orcid.org/0000-0000-0000-0001",
    "givenName": "Jane",
    "familyName": "Doe",
    "affiliation": { "@type": "Organization", "name": "Leiden University Medical Center" }
  },
  {
    "@type": "Person",
    "@id": "https://orcid.org/0000-0000-0000-0002",
    "givenName": "John",
    "familyName": "Smith",
    "affiliation": { "@type": "Organization", "name": "Amsterdam UMC" }
  }
]
```

If an author does not have an ORCID, register at [orcid.org](https://orcid.org/register). In the meantime, omit the `@id` field rather than leaving it empty.

### License(s): `license`

The license under which the software is distributed, as an [SPDX identifier](https://spdx.org/licenses/) URI.

```json
"license": "https://spdx.org/licenses/Apache-2.0"
```

```json
"license": ["https://spdx.org/licenses/Apache-2.0", "https://spdx.org/licenses/MIT"]
```

For choosing a license, see [Software license](sharing-licensing.md#software-license).

### Repository URL: `codeRepository`

The URL of the version-controlled source code repository.

```json
"codeRepository": "https://github.com/lumc/mytool"
```

### Programming language(s): `programmingLanguage`

The language(s) in which the software is written.

```json
"programmingLanguage": ["Python", "C++"]
```

### Software type: `applicationCategory`

The category of software. Use one or more values from the controlled vocabulary below:

```json
"applicationCategory": "Command-line tool"
```

```json
"applicationCategory": ["Library", "Web API"]
```

| Value | Use for |
|---|---|
| `Command-line tool` | Tools invoked from a shell or terminal |
| `Library` | Code intended to be imported by other software |
| `Web application` | Browser-based applications with a user interface |
| `Web API` | Programmatic HTTP interfaces |
| `Workflow` | Pipelines composed of multiple steps (Nextflow, Snakemake, CWL, Galaxy) |
| `Script` | Single-purpose scripts, including Jupyter and R Markdown notebooks |
| `Desktop application` | GUI applications installed locally |
| `Database portal` | Web interfaces to databases |
| `Ontology` | Formal ontologies or controlled vocabularies |

This vocabulary is aligned with the [bio.tools toolType list](https://biotools.readthedocs.io/en/latest/curators_guide.html#tool-type) to maximize interoperability with that registry.

### Operations: `schema:featureList`

What your software does. EDAM operation URIs are preferred because they enable semantic search in bio.tools and ELIXIR infrastructure. Plain-text descriptions are acceptable when no suitable EDAM term exists.

```json
"schema:featureList": [
  "http://edamontology.org/operation_3198",
  "http://edamontology.org/operation_3227"
]
```

```json
"schema:featureList": [
  "http://edamontology.org/operation_3198",
  "Dimensionality reduction of high-dimensional omics data"
]
```

To find EDAM terms:

1. Browse at [EDAM Browser](https://edamontology.github.io/edam-browser/)
2. Check what similar tools use in bio.tools
3. Search the EDAM ontology at [EBI OLS](https://www.ebi.ac.uk/ols4/ontologies/edam)

List terms that most closely describe the main function of your software. You can refine these if and when registering in bio.tools.

This field requires the dual `@context` described above.

## Recommended fields

The fields below are not enforced by CI but are strongly encouraged. Several are required by downstream registries.

### Other identifiers: `identifier` (additional values)

```json
"identifier": [
  "https://doi.org/10.5281/zenodo.1234567",
  "https://bio.tools/mytool"
]
```

### Release date: `datePublished`

```json
"datePublished": "2026-06-01"
```

### Keywords: `keywords`

Free-text keywords or ontology term URIs (including EDAM topics) for discovery: subject area, methods, and biological context such as organism, tissue, or disease.

```json
"keywords": [
  "genomics",
  "variant calling",
  "http://edamontology.org/topic_0622",
  "Homo sapiens",
  "breast cancer",
  "http://purl.obolibrary.org/obo/DOID_1612"
]
```

### Documentation URL: `softwareHelp`

```json
"softwareHelp": { "@type": "CreativeWork", "url": "https://mytool.readthedocs.io" }
```

### Issue tracker: `issueTracker`

```json
"issueTracker": "https://github.com/lumc/mytool/issues"
```

### Contact persons: `maintainer`

Contact people responsible for the software. For why a project should have at least two, see [Why a project needs at least two maintainers](identity.md#why-a-project-needs-at-least-two-maintainers).

```json
"maintainer": [
  {
    "@type": "Person",
    "givenName": "Jane",
    "familyName": "Doe",
    "email": "j.doe@lumc.nl"
  },
  {
    "@type": "Person",
    "givenName": "John",
    "familyName": "Smith",
    "email": "j.smith@aumc.nl"
  }
]
```

### Funding: `funding`

```json
"funding": [
  {
    "@type": "Grant",
    "identifier": "NWO-123456",
    "funder": { "@type": "Organization", "name": "Dutch Research Council (NWO)" }
  },
  {
    "@type": "Grant",
    "identifier": "ZonMw-789",
    "funder": { "@type": "Organization", "name": "ZonMw" }
  }
]
```

### Publications: `referencePublication`

```json
"referencePublication": [
  { "@type": "ScholarlyArticle", "@id": "https://doi.org/10.1093/bioinformatics/btXXXX" },
  { "@type": "ScholarlyArticle", "@id": "https://doi.org/10.1371/journal.pone.XXXXXXX" }
]
```

### Support status: `developmentStatus`

Use the [repostatus.org](https://www.repostatus.org/) vocabulary.

```json
"developmentStatus": "https://www.repostatus.org/#active"
```

Permitted values: `concept`, `wip`, `suspended`, `abandoned`, `active`, `inactive`, `unsupported`, `moved`.

### Operating systems: `operatingSystem`

```json
"operatingSystem": ["Linux", "macOS"]
```

### Dependencies: `softwareRequirements`

```json
"softwareRequirements": ["Python >=3.10", "numpy >=1.24"]
```

### Supporting data: `supportingData`

Reference datasets the software depends on, or the data a model was trained on.

```json
"supportingData": [
  {
    "@type": "Dataset",
    "name": "GRCh38 reference genome",
    "version": "GRCh38.p14",
    "url": "https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001405.40/"
  },
  {
    "@type": "Dataset",
    "name": "Training cohort (de-identified)",
    "version": "v2.0",
    "url": "https://doi.org/10.5281/zenodo.7654321"
  }
]
```

### Container and environment: `runtimePlatform`

```json
"runtimePlatform": ["Docker", "Conda", "SURF HPC"]
```

### Training materials: `softwareHelp`

```json
"softwareHelp": [
  { "@type": "CreativeWork", "url": "https://mytool.readthedocs.io" },
  { "@type": "CreativeWork", "url": "https://mybinder.org/v2/gh/lumc/mytool/HEAD" }
]
```

### Changelog: `releaseNotes`

```json
"releaseNotes": "https://github.com/lumc/mytool/blob/main/CHANGELOG.md"
```

### Continuous integration: `contIntegration`

```json
"contIntegration": "https://github.com/lumc/mytool/actions"
```

Where possible, run your tests in CI (see [Continuous integration](testing-quality.md#continuous-integration)).

### Information without a dedicated field

**EDAM-typed inputs and outputs** have no CodeMeta or schema.org field (`fileFormat` describes a file's own media type, not what the tool consumes or produces). Define these in bio.tools if you register there (see [Registering your software](#registering-your-software)).

## When to update the metadata

Update `codemeta.json` and `CITATION.cff` when you:

- Create a new release (update `version`, `identifier`, `datePublished`)
- Add or change authors (update `author` in both files)
- Change the license
- Move the repository
- Change the software's primary function

## Validation

Two checks are planned for the template repository, to run on every push and pull request:

- **Schema validation** — that `codemeta.json` conforms to the LUMC CodeMeta profile (`<codemeta-schema-repo>`) and that `CITATION.cff` is valid CFF 1.2.0.
- **Consistency** — that the shared fields (name, version, authors) match between the two files.

In the meantime you can validate locally with `codemetapy`, `cffconvert`, and a JSON Schema validator (see [Tools](#tools)).

## Registering your software

For where to register and how to choose, see [Registries](sharing-licensing.md#registries). Two registries interact directly with your metadata files:

- **[bio.tools](https://bio.tools/)** — a popular registry for life-sciences tools. A documented CodeMeta–biotoolsSchema crosswalk means most fields map conceptually, though the [bridge tool](https://github.com/bio-tools/biohackathon2025) currently registers from a GitHub repository rather than from `codemeta.json` (CodeMeta-based conversion may follow). After registering, add the bio.tools ID to **both** files — as an additional `identifier` in `codemeta.json`, and under `identifiers` (type `url`) in `CITATION.cff`.
- **[Research Software Directory](https://research-software-directory.org/)** — the national Dutch registry. It ingests `codemeta.json` from GitHub automatically, so a complete file is the main prerequisite.

## Tools

| Tool | Purpose | Link |
|---|---|---|
| CodeMeta generator | Interactive `codemeta.json` authoring | [codemeta.github.io/create](https://codemeta.github.io/create/) |
| cffinit | Interactive `CITATION.cff` authoring | [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/) |
| codemetapy | Python library for generating and validating CodeMeta | [proycon/codemetapy](https://github.com/proycon/codemetapy) |
| cffconvert | Validation and format conversion for `CITATION.cff` | [citation-file-format/cffconvert](https://github.com/citation-file-format/cffconvert) |
| EDAM Browser | Browse and search EDAM terms | [edam-browser](https://edamontology.github.io/edam-browser/) |
| BioHackathon 2025 bridge | CodeMeta-to-bio.tools registration | [bio-tools/biohackathon2025](https://github.com/bio-tools/biohackathon2025) |
| Zenodo–GitHub integration | Automatic DOI minting for releases | [GitHub docs](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) |

## Further reading

- [CodeMeta user guide](https://codemeta.github.io/user-guide/)
- [CITATION.cff specification and schema guide](https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md)
- [EDAM ontology documentation](https://edamontology.org/page)
- [bio.tools curator guide](https://biotools.readthedocs.io/en/latest/curators_guide.html)
- [Repostatus.org vocabulary](https://www.repostatus.org/)
- [SPDX license list](https://spdx.org/licenses/)
- [RDMkit — documentation and metadata](https://rdmkit.elixir-europe.org/metadata_management)
