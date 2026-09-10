
# This function returns the sum of even numbers in a list
def sum_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total


# this function returns the values in the list that are above the limit
def values_above(numbers,limit): 
    num_above = [] 
    for number in numbers: 
        if number > limit: 
            num_above.append(number) 
    return num_above


# this function returns the indices of the numbers in the list that are above the limit
def indices_above(numbers, limit):
    index = []
    for i in range(len(numbers)):
        number = numbers[i]
        if number > limit:
            index.append(i)
    return index

# This function returns the largest number in a list
def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


print(sum_even([1, 2, 3, 4, 5, 6]))  # Output: 12
print(sum_even([10, 15, 20, 25]))  # Output: 30
print(sum_even([-2, -1, 0, 1, 2]))  # Output: 0


print(values_above([1, 2, 3, 4, 5, 6], 3))  # Output: [4, 5, 6]
print(values_above([10, 15, 20, 25], 15))  # Output: [20, 25]
print(values_above([-2, -1, 0, 1, 2], 0))  # Output: [1, 2]


print(indices_above([4, 15, 8, 20], 10))  # [1, 3]
print(indices_above([20, 4, 15], 10))     # [0, 2]
print(indices_above([], 10))             # []

print(find_largest([8, 3, 12, 2]))  # 12
print(find_largest([-8, -3, -12]))  # -3
print(find_largest([5]))           # 5
