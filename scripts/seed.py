#!/usr/bin/env python3
"""Print a random seed string for design inspiration (String Seed of Thought).

Usage: python3 scripts/seed.py [length] [count]
"""
import secrets
import string
import sys

length = int(sys.argv[1]) if len(sys.argv) > 1 else 48
count = int(sys.argv[2]) if len(sys.argv) > 2 else 1
alphabet = string.ascii_letters + string.digits
for _ in range(count):
    print("".join(secrets.choice(alphabet) for _ in range(length)))
