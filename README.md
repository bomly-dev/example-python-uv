# example-python-uv

> Find vulnerabilities, trace reachability, and audit open-source risk in your **Python** project.

## About

This repository is a [Bomly](https://bomly.dev) example project for **Python** with **uv**.
Use it to try every Bomly feature — from basic SCA scans to vulnerability audits, reachability analysis, dependency tracing, and policy-driven CI gates.

## Dependency manifests

| File | Role |
|------|------|
| `pyproject.toml` | Dependency manifest |
| `uv.lock` | Dependency manifest |

## Try it with Bomly

### 1. Discover all dependencies

Map your full dependency graph — direct and transitive:

```bash
bomly scan --url https://github.com/bomly-dev/example-python-uv
```

### 2. Find vulnerabilities

Enrich packages with CVE data and surface real findings:

```bash
bomly scan --url https://github.com/bomly-dev/example-python-uv --enrich --audit
```

### 3. Confirm reachability

Cut alert noise: Bomly traces your call graph to prove which vulnerable code paths
your app actually reaches at runtime.

```bash
bomly scan --url https://github.com/bomly-dev/example-python-uv --enrich --reachability
```

### 4. Trace why a dependency exists

Understand every path that pulls `django` into your graph:

```bash
bomly explain django --url https://github.com/bomly-dev/example-python-uv
```

### 5. Add a security gate to CI

Fail your pipeline automatically when high-severity vulnerabilities are introduced:

```yaml
# .github/workflows/bomly.yml
name: Bomly Security Scan
on: [push, pull_request]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Scan with Bomly
        run: |
          curl -sSfL https://bomly.dev/install.sh | sh
          bomly scan --enrich --audit --fail-on high
```

Made with [Bomly](https://bomly.dev) — open-source SCA for every ecosystem.
