# Contributing to AutoDevHub
Thank you for considering contributing to AutoDevHub, an AI-powered automated development environment for GitHub repositories. This document outlines the steps and guidelines for contributing to the project.

## Setup Steps
To start contributing, follow these steps:
1. **Fork** the repository to your GitHub account.
2. **Clone** the forked repository to your local machine using `git clone`.
3. **Install** the required dependencies using `pip install -r requirements.txt` (for Python) or `npm install` (for TypeScript).
4. **Configure** your development environment by setting up a `.env` file with the required environment variables.

## Branch Naming Convention
We use a standardized branch naming convention to ensure clear and descriptive branch names:
* `feat/` for new features or enhancements.
* `fix/` for bug fixes or patches.
* `docs/` for documentation updates or changes.

## Conventional Commits
We use Conventional Commits to ensure that commit messages are clear and descriptive. Please follow the format:
type(scope): brief description

body
Where `type` is one of:
* `feat` for new features or enhancements.
* `fix` for bug fixes or patches.
* `docs` for documentation updates or changes.
* `style` for code style changes.
* `refactor` for code refactoring.
* `perf` for performance improvements.
* `test` for test additions or changes.
* `build` for build system changes.
* `ci` for continuous integration changes.
* `chore` for miscellaneous changes.

## Pull Request Checklist
Before submitting a pull request, ensure that:
* You have followed the branch naming convention and conventional commits format.
* Your code changes are formatted according to the code style guidelines (see below).
* You have run the tests (see below) and they pass.
* You have included a clear and descriptive commit message.
* You have included a brief summary of the changes made in the PR description.

## Code Style
We use the following code style guidelines:
* **Python**: Follow PEP 8 guidelines. Use `black` for code formatting and `isort` for import sorting.
* **TypeScript**: Follow the official TypeScript style guide. Use `prettier` for code formatting.
* **Terraform**: Follow the official Terraform style guide. Use `terraform fmt` for code formatting.

## Running Tests
To run tests, use the following commands:
* **Python**: `pytest` (install using `pip install pytest`).
* **TypeScript**: `npm run test` (uses Jest for testing).
* **Terraform**: `terraform test` (uses Terratest for testing).

## Reporting Bugs
If you find a bug, please report it by creating a new issue on the GitHub repository. Include:
* A clear and descriptive title.
* A step-by-step guide to reproduce the bug.
* The expected and actual behavior.
* Any relevant logs or error messages.
* Your environment and configuration (e.g., operating system, Python version).