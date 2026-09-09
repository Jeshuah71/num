def sum_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

print(sum_even([1, 2, 3, 4, 5, 6]))  # Output: 12
print(sum_even([10, 15, 20, 25]))  # Output: 30
print(sum_even([-2, -1, 0, 1, 2]))  # Output: 0

