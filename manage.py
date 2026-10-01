#!/usr/bin/env python3
"""Project management entrypoint.

Supports a minimal `test` command so CI can run `python manage.py test`.
"""

from __future__ import annotations

import sys
import unittest


def run_tests(args: list[str]) -> int:
    """Run unittest discovery and return a process-style exit code."""
    loader = unittest.defaultTestLoader
    suite = loader.discover(start_dir=".", pattern="test*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv if argv is None else argv)

    if len(argv) < 2:
        print("Usage: python manage.py test")
        return 1

    command = argv[1]
    if command == "test":
        return run_tests(argv[2:])

    print(f"Unknown command: {command}")
    print("Usage: python manage.py test")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
