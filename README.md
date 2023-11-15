# Commit Message Formatting Guide
### Introduction
This guide details the format and conventions for writing commit messages in your project. Following these guidelines ensures that your commit history is readable, consistent, and informative.
### Commit Message Format
The general structure of a commit message is as follows:
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```
### Components
1. **Type**: Indicates the kind of changes in the commit. Valid types include:
- build
- chore
- ci
- docs
- feat
- fix
- perf
- refactor
- revert
- style
- test

You can modify this list to suit your project's needs.

2. **Scope** (Optional): A noun describing the part of the codebase affected by the commit, e.g., `parser`, `api`, `lang`, `pipeline`, `scripts`, `infrastructure`.
3. **Description**: A brief summary of the changes. It should:
- Start with a space after `<type>[optional scope]:`
- Not end with a full stop
- Be concise and informative
- Not be empty
- Not use the following cases: 'sentence-case', 'start-case', 'pascal-case', 'upper-case'
### Additional Rules
- **Commit Length**: The commit message should not exceed 100 characters.
- **Emphasizing Breaking Changes**: Add "BREAKING CHANGE:" after one empty line to highlight significant changes that affect compatibility.
## Alternative for Highlighting Breaking Changes
Instead of using "BREAKING CHANGE:", you can implement a commit message checker:

```bash
#Commit message with ! to draw attention to breaking change
feat!: send an email to the customer when a product is shipped
#Commit message with scope and ! to draw attention to breaking change
feat(api)!: send an email to the customer when a product is shipped
```

## Installation
1. Copy `scripts/commit_msg_checker.py` and `.pre-commit-config.yaml` to your project root directory. If the scripts directory is modified or removed, ensure the paths in these files are updated accordingly.
2. Install pre-commit and set it up for commit messages:
```bash
pip install pre-commit
pre-commit install -t commit-msg
```
