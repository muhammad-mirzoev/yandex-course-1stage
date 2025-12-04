import sys


def count_comments(lines):
    return sum(1 for line in lines if line.strip().startswith('#'))


lines = sys.stdin.read().splitlines()
print(count_comments(lines))
