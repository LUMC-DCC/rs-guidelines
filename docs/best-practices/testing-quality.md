# Testing & quality assurance

Tests and quality checks are how you (and a future maintainer) know that the software still does what it is supposed to do. With even a small test suite, you have a baseline: if the tests pass, certain things have not silently broken.

## Minimum expectations by management level

| Level | Minimum |
|---|---|
| **A** | Manual or smoke checks documented in the README |
| **B** | Smoke tests, unit tests for critical logic, continuous integration (CI) on at least one platform |
| **C** | Unit + integration + end-to-end tests, CI matrix across platforms, release-blocking quality gates |

Start where you are. Add the next level when the project becomes the next level, usually, when a second person starts depending on it.

> **In the SMP:** the Testing question asks whether the project has tests. Documented, repeatable manual checks count as *Yes* at Level A. The follow-ups on test frameworks and continuous integration only apply to automated suites, leave them blank if yours are manual.

## Test types

Different test types catch different bugs. A useful taxonomy:

- **Smoke tests.** Does the software install and run at all? "Run the basic example; assert it produces an output file" is a complete smoke test. These are usually the first tests you write and the ones most worth keeping.
- **Unit tests.** Small, fast, focused tests of individual functions or classes. They are diagnostic — when they fail, you usually know exactly what broke. Good for pure logic.
- **Integration tests.** Multiple components working together. Slower than unit tests, but catch a different class of bug (interface mismatches, side effects, state-handling errors).
- **End-to-end / system tests.** A full workflow from input to output, often with real (or realistically synthetic) input data. Slow and a little flaky, but invaluable for pipelines and CLIs — they catch problems no smaller test would notice.
- **Regression tests.** Tests written specifically to prevent a previously-fixed bug from returning. Every reproducible bug report is an opportunity for a regression test before you fix it.
- **Property-based / fuzz tests.** Generated inputs check that *properties* hold (e.g., "the function always returns a non-negative number for any finite real input"). Tools: [Hypothesis](https://hypothesis.readthedocs.io/) (Python), [QuickCheck](https://hackage.haskell.org/package/QuickCheck) (Haskell, with ports), [proptest](https://docs.rs/proptest/latest/proptest/) (Rust).
- **Doctests.** Run examples embedded in documentation. They keep code samples honest — if you change an API, the doctest fails until you update the example.

A useful mental model is the **test pyramid** (Martin Fowler, [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)): many fast unit tests at the bottom, fewer integration tests in the middle, very few end-to-end tests on top. The shape exists for a reason, large numbers of slow tests waste both compute and developer attention.

Do **not** chase coverage percentages blindly. 100% line coverage on a function that runs `int(x) + 1` proves nothing; 60% coverage on the function that actually controls the scientific output is the one to focus on. **Test the code that can change the scientific conclusions first.**

> **In the Software Management Plan (SMP):** the Test types field is multi-select. Match the depth to the project level and to the risk profile of what the software does. For Level C software making clinical recommendations, expect smoke + unit + integration + end-to-end + regression. For a Level A analysis script, smoke + a couple of unit tests of the critical function may be the right answer.

## Test frameworks

Name the framework so contributors know how to run the tests without guessing. The common defaults are:

| Language | Framework |
|---|---|
| Python | [pytest](https://docs.pytest.org/) |
| R | [testthat](https://testthat.r-lib.org/) |
| Rust | built-in `cargo test`, optionally [`proptest`](https://docs.rs/proptest/latest/proptest/) |
| Go | built-in `go test`, [`testify`](https://github.com/stretchr/testify) |
| Java | [JUnit 5](https://junit.org/junit5/) |
| JavaScript / TypeScript | [Vitest](https://vitest.dev/) or [Jest](https://jestjs.io/) |
| C / C++ | [Catch2](https://github.com/catchorg/Catch2), [GoogleTest](https://google.github.io/googletest/) |
| Bash | [bats-core](https://github.com/bats-core/bats-core) |

For a hands-on walk-through on the Python side, see [Testing with pytest — unit, integration, and smoke tests](https://ucldevs.hashnode.dev/testing-with-pytest-unit-integration-and-smoke-tests).

For [doctests](https://docs.python.org/3/library/doctest.html) in Python specifically — the standard library has a `doctest` module that runs examples in docstrings.

A more general orientation: [The Turing Way — good practice for testing](https://book.the-turing-way.org/reproducible-research/testing/testing-guidance.html).

> **In the SMP:** the Test framework field is free text. Listing more than one framework is fine and common (e.g., `pytest + hypothesis` for unit and property tests).

## Continuous integration

**Continuous integration (CI)** runs your tests automatically on every push or pull request. It is one of the highest-leverage practices in research software.

A minimal CI pipeline:

1. **Checks out the repository.**
2. **Sets up the language version** (e.g., Python 3.11).
3. **Installs the project and its dependencies.**
4. **Runs the tests.**
5. **Runs lint and type checks** if configured.

The default CI platforms:

- **[GitHub Actions](https://docs.github.com/en/actions)** — the default for open-source repositories on GitHub. Generous free tier for public repositories.
- **[GitLab CI](https://docs.gitlab.com/ee/ci/)** — the default for LUMC GitLab projects. Comparable feature set.

For multi-platform projects, run a CI **matrix**: same tests, different combinations of OS and language version. This is what gives "supported on Linux + macOS, Python 3.11 + 3.12" its meaning.

**Continuous deployment (CD)** is the natural extension: on a tagged release, automatically publish the package, push the container image, and deploy the documentation. CD is a Level B/C investment; for Level A, manual releases are fine.

> **In the SMP:** the Automated testing question is a three-state: *Yes*, *Partially*, *No*. "Partially" is the honest answer for projects where tests run in CI but, say, only on Linux and only on one Python version. This question is about **tests**; whether your formatters and linters are also enforced automatically is asked separately, under [Code quality standards](#code-quality-standards).

## Project / dependency management tools

Use tools that make environments reproducible. The choice depends on the language ecosystem, but the *output* is the same in every case: a **lock file** that pins the exact versions used.

| Ecosystem | Typical tools |
|---|---|
| Python | [uv](https://docs.astral.sh/uv/), [Poetry](https://python-poetry.org/), [Hatch](https://hatch.pypa.io/), [Pixi](https://pixi.sh/), [`pip-tools`](https://pip-tools.readthedocs.io/) |
| R | [renv](https://rstudio.github.io/renv/), [rix](https://github.com/b-rodrigues/rix) |
| JavaScript / TypeScript | [npm](https://www.npmjs.com/), [pnpm](https://pnpm.io/), [yarn](https://yarnpkg.com/) |
| Rust | built-in [cargo](https://doc.rust-lang.org/cargo/) |
| C / C++ | [CMake](https://cmake.org/) with [Conan](https://conan.io/) or [vcpkg](https://vcpkg.io/) |
| Java | [Maven](https://maven.apache.org/), [Gradle](https://gradle.org/) |
| Cross-language | [Pixi](https://pixi.sh/), [Nix](https://nixos.org/), [`conda-lock`](https://github.com/conda/conda-lock) |
| Workflows | [Snakemake](https://snakemake.readthedocs.io/), [Nextflow](https://www.nextflow.io/) |

For Conda specifically, see [The Turing Way — Conda package management systems](https://book.the-turing-way.org/reproducible-research/renv/renv-package.html).

> **In the SMP:** the Project / dependency management question is binary (Yes/No), with a follow-up listing the tools. Be specific, name the tools, not just "I use lock files".

## Code quality standards

Quality tooling reduces maintenance cost. It does not make bad science good, but it makes the code easier to read, review, and change.
Useful common combinations:

| Language | Formatter / linter / static analyser |
|---|---|
| Python | [ruff](https://docs.astral.sh/ruff/) (replaces black + isort + flake8), [mypy](https://www.mypy-lang.org/) or [pyright](https://microsoft.github.io/pyright/) for type-checking |
| R | [lintr](https://lintr.r-lib.org/), [styler](https://styler.r-lib.org/) |
| Rust | built-in [rustfmt](https://github.com/rust-lang/rustfmt), [clippy](https://doc.rust-lang.org/clippy/) |
| C / C++ | [clang-format](https://clang.llvm.org/docs/ClangFormat.html), [clang-tidy](https://clang.llvm.org/extra/clang-tidy/) |
| JavaScript / TypeScript | [eslint](https://eslint.org/), [prettier](https://prettier.io/), built-in `tsc` |
| SQL | [sqlfluff](https://sqlfluff.com/) |

Type-checking is a separate discipline but well worth adding for projects above Level A. In Python, `mypy` or `pyright` catch a useful class of bugs at the cost of writing type annotations. In compiled languages, type-checking is just "the compiler".

The classic Python style guide is [PEP 8](https://peps.python.org/pep-0008/) (or, more readably, the [stylized PEP 8 presentation](https://pep8.org/)). For broader Python code-quality tooling and habits, the [Real Python guide](https://realpython.com/python-code-quality/) is a good overview. For an institutional badge program, [OpenSSF Best Practices Badge](https://bestpractices.coreinfrastructure.org/) is the standard self-certification.

For Level B and C, enforce formatting and linting in **CI** or via **pre-commit hooks** (using [`pre-commit`](https://pre-commit.com/)) rather than relying on memory. The point is automation: a contributor's formatting mistake is caught at commit time, not after the maintainer finishes reviewing a PR.

> **In the SMP:** the Code quality standards question is binary, with a follow-up listing the tools. Whether those checks are actually enforced - in CI, as a pre-commit hook, or both - is the separate *Automated enforcement of code quality* follow-up. "Yes" means *something is automated*; if quality is enforced only by manual review and discipline, "No" is the better answer.

## Code review

Code review is the cheapest defect-detection method available, and the main way knowledge about a codebase spreads beyond the person who wrote it. For research software the second effect usually matters more than the first: a project where exactly one person has ever read the code has a continuity problem regardless of how good that code is.

Record **who reviews, when, and against what**:

- **Who.** A second maintainer, a group member, an external RSE. For single-maintainer projects, an honest *"no review; changes are self-merged"* is better than implying a process that does not exist.
- **When.** Every pull request, only for changes touching analysis logic, or before each release. Pick the level you will actually sustain.
- **Against what.** Does it do what the pull request claims, are there tests, does it pass CI, is it documented? A three-line checklist in `CONTRIBUTING.md` beats an unwritten standard.

Review is not a substitute for CI, and CI is not a substitute for review. CI checks that the rules you automated still hold; review catches what no linter can - a wrong statistical choice, a misread specification, an assumption that only holds for your cohort.

> **In the SMP:** Code review is a free-text field. Describe the process you have, not the one you aspire to. *"Self-merged, with a second reader before releases"* is a real and useful answer.

## Cross-platform / environment testing

State which platforms are supported *and tested*. The distinction in [Interoperability](interoperability.md) applies here too:

- **Supported.** Documented in the README, tested manually or in CI, bugs accepted.
- **Expected to work.** Maintainers think it works; not actively tested.

If a CI matrix tests Linux + macOS but not Windows, and you have Windows users, that is a real gap. Either add Windows to the matrix or be explicit in the README that Windows is unsupported.

## Sample data and parameters for tests

For tests to be reproducible, they need stable input. Sample data and parameter sets should live in the repository under `tests/data/` (or `examples/`) and be small enough to commit safely. For larger fixtures, use [Git LFS](https://git-lfs.github.com/) or fetch them at test-time from a documented location (Zenodo, S3, an institutional bucket). See [Data formats](interoperability.md#data-formats) in Interoperability.

Three properties make a fixture useful rather than merely present:

- **Small and fast.** A fixture that takes ten minutes to process will stop being run. Cut a representative slice - one chromosome, one subject, one plate - rather than shipping a whole cohort.
- **Never real personal data.** Test fixtures are committed, copied, and forked. Use synthetic or fully de-identified data; if the software handles patient data, the fixture must not. See [Personal and sensitive data](risks.md#personal-and-sensitive-data).
- **Documented provenance.** Say where the fixture came from and what makes it a valid example. A file called `test_input.csv` with no explanation is a maintenance liability the moment its author leaves.

Record the parameter sets too, not just the data. A pipeline that only reproduces with the right config is not reproducible from the data alone.

This is a different thing from the example file recorded against each entry in the Data formats list. That one is a *format exemplar*, showing what a valid file looks like; this one is a *fixture*, reproducing a specific known-good run.

> **In the SMP:** the Sample data & parameters field asks where the fixtures live and what they cover. A path plus one line on provenance is enough - *"`tests/data/`: synthetic 3-subject cohort generated by `scripts/make_fixture.py`, seed 42"*.

## Further reading

- The Turing Way. [Testing](https://book.the-turing-way.org/reproducible-research/testing/). Broad reference covering all the test types above.
- Fowler. [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html). The canonical short essay on what to test and at which level.
- Atlassian. [Plan your regression-testing strategy](https://community.atlassian.com/forums/Jira-articles/Plan-your-regression-testing-strategy-by-asking-the-relevant/ba-p/1158403). Practical regression-testing guide.
- [OpenSSF Best Practices Badge](https://bestpractices.coreinfrastructure.org/). Self-certifying badge for open-source projects.
- [PEP 8](https://peps.python.org/pep-0008/). The Python style guide; the closest thing to a universal reference in the Python world.
- [pre-commit](https://pre-commit.com/). Framework for running formatters and linters as Git hooks.