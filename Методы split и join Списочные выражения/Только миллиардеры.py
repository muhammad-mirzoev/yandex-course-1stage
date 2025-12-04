input_data = input()

result = [
    ','.join([str(amount) for amount in map(int, journal.split(',')) if amount >= 10**9])
    for journal in input_data.split(';')
]

print("\n".join(result))
