#!/usr/bin/env python3

import argparse
import shlex
import subprocess
import sys

parser = argparse.ArgumentParser(
    description='Helper-script for various tasks during development.'
)
commands = parser.add_subparsers(dest='command')
cq_parser = commands.add_parser('code-quality', help='Run various checks for coding standards.')
args = parser.parse_args()

if args.command == 'code-quality':
    commands = [
        'isort --check-only --diff -rc admin/ dev.py',
        'flake8 admin/ dev.py',
        'python -Wd admin/manage.py check',
    ]

    for cmd in commands:
        print('+', cmd)
        try:
            subprocess.check_call(shlex.split(cmd))
        except subprocess.CalledProcessError as e:
            sys.exit(e.returncode)
