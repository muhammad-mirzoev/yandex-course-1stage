import sys


def is_tomato(num):
    return '0' not in str(num)


def evaluate_field(field):
    rows = [list(map(int, row.split())) for row in field]
    return "ALUMINUM CUCUMBERS" if any(
        sum(1 for num in row if not is_tomato(num)) > len(row) // 2
        for row in rows
    ) else "EVERGREEN TOMATOES"


field = sys.stdin.read().strip().split('\n')

print(evaluate_field(field))
