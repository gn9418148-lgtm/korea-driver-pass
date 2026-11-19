#!/usr/bin/env python3
"""Generate valid KP180-XXXXXX-CC 180-day access codes for Kmong buyers / device recovery."""
import random
import string
import sys

def make_code():
    body = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    h = 0x5A
    for ch in body:
        h = ((h * 33) ^ ord(ch) ^ 0xA7) & 0xFF
    return f"KP180-{body}-{h:02X}"

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    for _ in range(n):
        print(make_code())
