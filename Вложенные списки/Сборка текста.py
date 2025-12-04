numbers = list(map(int, input().split()))
words = input().split()

result = [words[num - 1] for num in numbers]

result_str = " ".join(result).capitalize()

print(result_str)
