# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

```markdown
## [Unreleased] - YYYY-MM-DD
### Added
### Changed
### Deprecated
### Fixed
### Security
```

## [Unreleased] - YYYY-MM-DD
### Added
- Created CLI sub-commands for run and list.
- Added py.typed marker file for mypy.
- The nox installation directory can now be overriden through the enviroment variable
  `NOX_ENVDIR`. Defaults to `.nox` when environment variable does not exist.
- Add flake8 lint checks.
- Disabled missing type documentation when linting test files with pylint.
- Update the minimum python version to 3.9.
- The GitHub workflow now testing against python versions 3.9 through 3.13.
### Changed
- Renamed project to `labtest`.
- Pylint now uses all availabe extentions by default.
- Updated the nox control file to share virtual environment across sessions.
- Reorganized the test files and created shared test fixtures where useful.
- Enforcing type hints in both the source and test files.
### Deprecated
### Fixed
- The nox session `cli` no longer runs by default and generates an error due to lack
  of command line arguments.
- The nox session `clean` no longer requires the creation of a virtual environment.
- Changed the GitHub workflow badge from the `python-sample` repo to the correct
  `python-labtest` repo.
- Adding missing test to fix implicit coverage of registry execute arguments.
### Security
