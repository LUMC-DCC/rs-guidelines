# Motivation & scope

A paragraph about *why this software exists* is the single best return on writing-time in a software project. Future reviewers, future collaborators, future PhD students inheriting your code, and your own future self all begin by reading it.

This chapter walks through how to frame the motivation cleanly: the problem, the audience, what already exists, and why a new project is justified rather than a contribution to an existing one.

## The problem

Every research software project answers some version of the question: *what currently fails, is slow, is missing, is inconsistent, or is unreproducible, and who suffers from it?* A good problem statement says all four:

1. **What currently fails** or is awkward.
2. **Who is affected** and how badly.
3. **Why software is the right intervention** (rather than, say, a different experimental protocol).
4. **What is out of scope**, explicitly.

Two or four sentences is usually enough. A useful template:

> In *<field/context>*, *<task>* is currently *<manual / slow / inconsistent / hard to reproduce>* because *<reason>*. Existing tools such as *<X>* and *<Y>* solve *<part>*, but not *<gap>*. This software addresses the gap by *<approach>*. It does not attempt to *<explicit non-goal>*.

### Anti-patterns to avoid

- **Implementation-as-problem.** *"We needed a way to run X on our data."* That's a method, not a problem. Why does X need running? What goes wrong without it?
- **Jargon overload.** *"Calibration of a spatial transcriptomics pipeline."*. Spell out at least once: *what* is being calibrated, *what* spatial transcriptomics is for in this context, *why* the calibration is non-trivial.
- **Vague scope.** *"We needed better data analysis."* Better than what, by which measure?
- **Confusing the audience with the developer.** A motivation written for the supervisor is not the same as one written for a future user. Aim at the latter.

> **In the SMP:** the Problem field expects 2–4 sentences that an expert from an adjacent sub-field could understand. Drop the jargon by one level from what you would write in a paper's abstract.

## Purpose categories

The Purpose field is a controlled vocabulary: a multi-select list with categories such as *data analysis*, *pipeline / workflow*, *library / framework*, *visualisation*, *clinical decision support*, *simulation*, *infrastructure / utility*, *interface / wrapper*, and so on.

A few rules of thumb:

- **Describe the outputs, not the libraries.** A wrapper that calls scikit-learn is not, on its own, a *machine-learning library*; the library is scikit-learn, your software is a *pipeline*, a *workflow*, or a *CLI*.
- **Genuine reuse vs interfacing.** If your code imports a third-party library and exposes a thin shell, you are *interfacing*. Describe the shell's purpose ("CLI for in-house pipeline X using library Y"), not the library's. Genuine *reuse* means you fork and modify, or you re-implement an algorithm with substantial customisation.
- **Be selective.** Two or three categories is usually right.

Worked examples:

- A Snakemake workflow for RNA-seq processing: **pipeline / workflow** (primary) and possibly **data analysis**.
- A Python package exposing reusable statistical functions: **library / framework**.
- A CLI that wraps an existing tool with project-specific defaults: **interface / wrapper**, not a new method.
- A web service that serves model predictions to a clinical UI: **clinical decision support** plus **infrastructure / utility**.

> **In the SMP:** if no category fits well, use the Additional purpose field to write one short noun phrase. If you find yourself writing a paragraph there, you probably want one of the existing categories plus a clarifying note in the Problem field.

## Audience

The intended users determine many downstream decisions. Choose categories that are as specific as you can defensibly justify.

The audience drives:

- **Packaging.** A library for other developers belongs on PyPI/CRAN; a tool for clinicians belongs in a Docker container, on a Galaxy server, or in a clickable interface.
- **Documentation style.** Developer-focused (API reference, code examples) vs end-user-focused (screenshots, step-by-step recipes, "what does this button do").
- **Support channels.** GitHub issues are great for developers; a clinician will email you. Plan for that.
- **Licensing.** A permissive license is friendlier to reuse; a copyleft license forces downstream openness, which may or may not match your audience's expectations.

> **In the SMP:** pick the most specific audience categories that genuinely apply. The intended audience can evolve over the project; revisit this answer in maintenance.

## Related and upstream software

List the existing software, libraries, and pipelines your project builds on, extends, wraps, replaces, or interoperates with. This is **not** a full dependency manifest (that lives in `pyproject.toml`, `Cargo.lock`, `renv.lock`; see [Interoperability](interoperability.md) and [Versioning & releases](versioning-releases.md)). It is the *conceptual* lineage: which projects matter for understanding what your tool is and is not.

For each related project, capture:

- **Tool/library name** - exactly as it is commonly cited.
- **Reference URL or DOI** - DOI preferred for citation.
- **Relationship** - and here precision is helpful. Useful relationship labels include: *dependency*, *wrapper around*, *fork of*, *reimplementation of*, *interoperates with*, *produces input for*, *consumes output from*, *supersedes*.

A worked example:

```text
- Tool: nnU-Net
  URL/DOI: https://github.com/MIC-DKFZ/nnUNet
  Relationship: dependency - used as the underlying segmentation engine

- Tool: MONAI
  URL/DOI: https://monai.io
  Relationship: alternative considered but not adopted (see Value & need)

- Tool: ourlab/legacy-segmentation
  URL/DOI: https://gitlab.lumc.nl/ourlab/legacy-segmentation
  Relationship: supersedes; we kept the data interface but rewrote the core
```

> **In the SMP:** the Related software list is open-ended; include the projects that a reader actually needs to understand the context.

## Justify the existence of a new project

New software has a real, recurring maintenance cost. If the same problem could be solved by contributing a feature or a fix to an existing project, the existing project is usually the better long-term choice.

A complete answer addresses three questions:

1. **What's out there?** Name the most plausible alternatives. Ideally these are the same projects that appear in *Related software*.
2. **Why is this software better, or different, for the audience identified above?** Concrete advantages: speed, accuracy, fit to a specific data format, integration with an LUMC system, license, language stack.
3. **Why a new project rather than a contribution to an existing one?** Was the upstream unmaintained? Was the change too invasive to merge? Was the license incompatible? Was there no existing project at all? Was the upstream team unresponsive?

Strong reasons:

- No existing tool supports the required domain standard.
- Existing tools are unmaintained, abandoned, or incompatible with LUMC infrastructure.
- The project contributes a genuinely new method.
- Integration across several existing tools is the main contribution.
- Regulatory, privacy, or operational constraints require local control.

Weak reasons:

- *"We wanted our own version."*
- *"The student had already started coding."*
- *"We did not search for alternatives."* (This is the most common.)
- *"Existing tools were unfamiliar."*

If no real alternative exists, say so explicitly. That is itself a strong justification, and it changes the entire shape of the project, because you are now responsible for a primary tool rather than a competing one.

If you are extending an existing tool, name it in *Related software* and explain what was missing. "We tried to upstream this, but the maintainers preferred a different architecture" is a perfectly good answer.