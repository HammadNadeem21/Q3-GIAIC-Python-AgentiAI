# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_of_numbers(numbers):

    total = 0

    for num in numbers:
        total += num

    return total

numbers_list = [1, 2, 3, 4, 5, 6]
result = sum_of_numbers(numbers_list)
print(f"Sum: {result}")
