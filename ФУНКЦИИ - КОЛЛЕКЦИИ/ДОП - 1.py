import sys


def check_quality():
    for batch in sys.stdin:
        batch = batch.strip()

        if not batch:
            continue

        items = list(map(int, batch.split("; ")))

        if all(item % 5 == 0 for item in items):
            print("FAIL")
            return

    print("OK")


check_quality()
