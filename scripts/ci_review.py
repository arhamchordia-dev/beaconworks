#!/usr/bin/env python3
"""
Lesson 17.3 "Run a noninteractive workflow" -- structured review output
meant to be produced by `codex exec` in CI, not typed by hand. This script
is the "what the CI decision should look like" reference: a fixed JSON
shape, non-zero exit on failure, so a pipeline can branch on it.

The lesson's real content is running this shape THROUGH codex exec, not
this script itself -- keep this as the target contract to verify codex
exec's output against, not the deliverable.
"""
import json
import subprocess
import sys
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")


def main():
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-q"]
        if _has_pytest()
        else [sys.executable, "tests/test_priority.py"],
        cwd=ROOT,
        capture_output=True,
    )
    tests_passed = result.returncode == 0

    decision = {
        "tests_passed": tests_passed,
        "reviewed_files": ["server.py", "src/lib/priority.py"],
        "recommendation": "merge" if tests_passed else "block",
    }
    print(json.dumps(decision, indent=2))
    sys.exit(0 if tests_passed else 1)


def _has_pytest():
    try:
        import pytest  # noqa: F401
        return True
    except ImportError:
        return False


if __name__ == "__main__":
    main()
