# pre-commit Hooks for LaTeX [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit) | [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/jonasbb/pre-commit-latex-hooks/master.svg)](https://results.pre-commit.ci/latest/github/jonasbb/pre-commit-latex-hooks/master)

## Example configuration

`.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/jonasbb/pre-commit-latex-hooks
    rev: v1.1.0
    hooks:
      - id: american-eg-ie
      - id: cleveref-capitalization
      - id: csquotes
      - id: no-space-in-cite
      - id: tilde-cite
      - id: consistent-spelling
        args:
            [
              "--emph=et al.",
              "--emph=a priori",
              "--emph=a posteriori",
              '--regex=naive=\bna(i|\\"i)ve',
            ]
      - id: ensure-labels-for-sections
      - id: cispa-syssec-forbidden-words
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.3.0
    hooks:
      - id: check-merge-conflict
      - id: check-yaml
      - id: trailing-whitespace
        files: ".*\\.(?:tex|py)$"
```