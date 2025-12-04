def refinement(numbers):
    if not hasattr(refinement, "all_numbers"):
        refinement.all_numbers = []
    refinement.all_numbers.extend(numbers)

    total_sum = sum(refinement.all_numbers)
    parity = total_sum % 2
    filtered_numbers = [num for num in refinement.all_numbers if num % 2 == parity]

    if filtered_numbers:
        return sum(filtered_numbers) / len(filtered_numbers)
    else:
        return 0


print(refinement([1, 2, 3]))  # 2.0
print(refinement([4, 5, 6, 7]))  # 4.0
print(refinement([1]))  # 3.4
