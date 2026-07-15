# Interoperability

Interoperability is about how your software *talks to the rest of the world*: which languages it is written in, which data formats it reads and writes, what platforms it runs on, and how reproducibly others can recreate your computational environment. The aim is **machine-actionable, reusable information** - both for humans coming to your project, and for tools (registries, CI systems, package managers) that need to do something useful with it.

## Programming languages

List the languages actually used in the project, with version constraints where they matter. This includes more than the primary language: list any language used for non-trivial logic within the project.

A reasonable inventory covers:

- The **primary language** of the package, library, or executable.
- **Workflow languages** if any logic lives there: Snakemake, Nextflow, CWL, WDL.
- **Build / glue languages** with non-trivial logic: Make, CMake, Bash scripts that orchestrate the pipeline.
- **Frontend / backend split**, if applicable.
- **Compiled cores with language bindings** - for example, a Rust core exposed through Python via PyO3, or a C++ core wrapped in R.

For each entry, capture:

- **Language name** as commonly known (e.g., "Python", "Rust", "R").
- **Version constraint** - `"3.14.2"`, `">=3.11"`, `">=1.78,<1.85"`. Constraints belong in your project manifest (`pyproject.toml`, `Cargo.toml`, `DESCRIPTION`).
- **Role in the project** - `"primary library + CLI"`, `"workflow definitions in workflows/"`, `"glue scripts only, no scientific logic"`.

A real-world example:

```text
Python >=3.11,<3.13 - primary package and CLI
Snakemake >=8 - workflow definitions
Bash - small helper scripts only, no scientific logic
Rust >=1.78 - performance-critical parser, exposed through Python bindings
```

> **In the SMP:** the Programming languages list captures language, version constraint, and role.

## Input and output data formats

Listing formats is the easy part. The harder part is describing what your tool expects *within* those formats, because the format itself often does not capture all necessary structure or assumptions.
CSV, JSON, XML, HDF5, and Parquet are *containers*, what makes data interoperable is the **schema** inside.

For each input and output format, capture:

- **Format name.** Prefer controlled **EDAM Format** terms where available (the SMP integrates with [EDAM](https://edamontology.org/) - start typing and pick from the dropdown). Common entries: `BAM`, `FASTQ`, `VCF`, `DICOM`, `NIfTI`, `BIDS`, `TSV`, `JSON`, `Parquet`, `NetCDF`.
- **Format version / profile** if it matters: `VCF >=4.2`, `DICOM SR`, `BIDS 1.8`.
- **Schema or expected columns/fields**, especially for generic containers. For a CSV, "columns: `subject_id, age_at_scan, group`" is the actual contract. Link to a schema file if one exists (JSON Schema, XSD, BIDS specification).
- **Constraints** that matter for interoperability - e.g., "only ASCII filenames", "no compressed inputs", "must be sorted by chromosome".
- **A sample or example file URL**, ideally checked into the repository under `examples/` or `tests/data/`.

**Never commit real patient data, even as a test fixture.** Use synthetic or thoroughly de-identified data, and have it reviewed before committing if in any doubt.

### EDAM

EDAM is excellent for common bioinformatics formats and operations and increasingly used in clinical-data contexts. If your input is something exotic (a custom binary log from a piece of lab equipment, or a project-internal TSV layout), there will be no EDAM term. In that case, use a clear descriptive name and provide the schema. Do not force-fit an EDAM term that does not really apply.

> **In the SMP:** Input and Output format lists each capture format name (EDAM where possible), version constraint, schema or constraints, and a sample-file URL. Skip the section entirely if the software does not consume or emit external data.

## Functions / operations

For tools that expose multiple operations (a CLI with several subcommands, an API with several endpoints, a library with distinct entry points), the SMP can capture each operation with:

- the **input format** it consumes;
- the **operation** it performs (preferably an **EDAM Operation** term, e.g., `Variant calling`, `Sequence alignment`, `Image segmentation`);
- the **command** or command-line fragment that triggers it;
- the **output format** it produces;
- a **note** clarifying anything unusual about the operation.

This is the same metadata that tools like [bio.tools](https://bio.tools/) and Galaxy use to describe what software does.

> **In the SMP:** the Functions list is only needed when the software exposes one or multiple distinct operations.

## APIs and interfaces

If your software exposes interfaces beyond a single CLI, document them. Common interface types:

- **Command-line interface.** Usable subcommands; flags; standard streams.
- **Language API** - Python, R, JavaScript, Rust. Public functions and their stability guarantees.
- **REST or GraphQL API**, with [OpenAPI](https://www.openapis.org/) or [GraphQL schema](https://graphql.org/learn/schema/) where possible.
- **Plugin system** - extension points, plugin lifecycle, plugin discovery.
- **Web interface** - for clinicians or end-users.
- **Database schema** - if your software reads or writes a structured database, the schema is part of the interface.
- **File-based workflow interface** - e.g., a Snakemake module that consumes and produces specific file layouts.

For each interface, state whether it is **stable**, **experimental**, or **internal**. Users who depend on an "experimental" API have been warned; users who depend on an "internal" API are on their own. This is the contract.

For REST APIs in particular, provide an OpenAPI specification, most modern frameworks (FastAPI, Spring Boot, Express + swagger-jsdoc) generate one from the code. The spec then drives client generation, documentation tools like [Redoc](https://redocly.com/redoc/) and [Swagger UI](https://swagger.io/tools/swagger-ui/), and contract testing.

## Cross-platform compatibility

State which operating systems and architectures the software *officially supports*. There is a real distinction worth respecting:

- **Supported** - CI-tested, advertised in the README, bugs accepted and triaged.
- **Expected to work** - used by maintainers in practice, but no CI; bugs may not be prioritised.
- **Untested** - silence is the right answer; do not claim what you do not verify.

Pure-runtime languages (Python, R, Java, JavaScript without native dependencies) usually work on Linux, macOS, and Windows alike. Anything compiled, anything that calls system libraries, anything that depends on a specific filesystem semantics, anything that uses GPU acceleration, those have real platform constraints worth being explicit about.

For Level B/C, run CI on at least Linux, plus macOS. Windows is genuinely harder for many scientific stacks; "supported under WSL" is a common compromise.

> **In the SMP:** the Cross-platform compatibility question is a multi-select. Tick only the platforms you actually support. "Linux" is the safe default; pick more deliberately.

## Resource requirements

Describe typical and worst-case hardware resources required to run the software. Users planning compute allocations or deploying to clinical infrastructure need this.

A useful structure:

```text
Memory     : ~1 GB typical, up to 16 GB for whole-genome inputs
Storage    : ~200 MB code; ~5 GB for a representative input dataset
Compute    : 1–8 CPU cores typical; scales linearly to 32 in batch mode
GPU        : NVIDIA, ≥ 12 GB VRAM, CUDA ≥ 11.8 (segmentation step only)
Wall clock : ~5 min/subject; ~3 h for a 100-subject cohort on 8 cores
```

If resource use depends strongly on input characteristics, name the driving factor (number of subjects, file size, image dimensions, model parameter count) rather than giving a single point estimate.

> **In the SMP:** the Resource requirements field is free-text. Even a few lines following the structure above is useful.

## Containerisation and environment specification

Beyond your language-level dependency manifest (`pyproject.toml`, `requirements.txt`, `environment.yml`, `Cargo.lock`, `renv.lock`, etc., which live in the repository), three patterns of environment specification offer increasing levels of reproducibility:

1. **Lock-file plus README narrative.** The manifest pins dependency versions; the README explains the supported platform, language version, and installation command. Acceptable for Level A and for smaller Level B projects.
2. **Container image** - a `Dockerfile` or an Apptainer / Singularity recipe. The container *is* executable documentation: it captures the OS, system libraries, language runtime, and all dependencies in a form that anyone can run. This is the practical gold standard.
3. **Whole-environment specification.** Bit-for-bit reproducibility, including system-library versions. Worth the cost for software that *must* produce the same numbers across machines, or for clinical-grade reproducibility.

Useful options:

- [**Docker**](https://www.docker.com/) and [**Podman**](https://podman.io/) - general containers. Podman is daemonless and rootless by default, which matters in some institutional contexts.
- [**Apptainer**](https://apptainer.org/) (formerly **Singularity**) - for HPC environments where Docker is not available.
- [**Nix**](https://nixos.org/) / [**Guix**](https://guix.gnu.org/) - rigorous whole-environment reproducibility, including system libraries.
- [**Pixi**](https://pixi.sh/) and [`conda-lock`](https://github.com/conda/conda-lock) - multi-platform environment locks, lightweight compared to full containers.

A container by itself is not automatically reproducible. Practical hygiene:

- **Pin base images and dependency versions.** `FROM python:3.11` will drift over time as the upstream Python image is rebuilt. `FROM python:3.11.7-slim-bookworm` is much closer to reproducible.
- **Document build commands** in the README or developer documentation.
- **Publish tagged images** rather than relying on `latest`.
- **Build for the right runtime.** HPC clusters almost always need Apptainer images - you can build an Apptainer image from a Docker image with `apptainer build my.sif docker://...`.

[The Turing Way - Containers](https://book.the-turing-way.org/reproducible-research/renv/renv-options.html) covers the trade-offs in more depth.

> **In the SMP:** the Containerisation question offers four states - *Full environment spec*, *Dockerfile or equivalent*, *Lock-file only*, *No*. Pick the strongest pattern that is genuinely in place.