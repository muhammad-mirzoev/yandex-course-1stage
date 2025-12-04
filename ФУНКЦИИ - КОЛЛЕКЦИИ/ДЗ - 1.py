import sys

print(any('0' in row.split() for row in sys.stdin))
