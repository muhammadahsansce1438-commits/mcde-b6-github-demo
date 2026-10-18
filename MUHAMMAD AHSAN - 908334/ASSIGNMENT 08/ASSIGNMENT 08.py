
# Q1. Accessing List Elements

numbers = [10, 20, 30, 40, 50, 60, 70]

first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]

print("Q1 - First:", first)
print("Q1 - Middle:", middle)
print("Q1 - Last:", last)


# Q2. List Slicing

numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

first_five = numbers[:5]
last_four = numbers[-4:]
every_second_reverse = numbers[::-2]

print("Q2 - First five:", first_five)
print("Q2 - Last four:", last_four)
print("Q2 - Every second in reverse:", every_second_reverse)


# Q3. List Modification

fruits = ["apple", "banana", "cherry", "mango"]

fruits[1] = "orange"
fruits.insert(2, "grapes")
fruits.remove("cherry")

print("Q3 - Modified fruits:", fruits)


# Q4. Reverse Without reverse()

numbers = [12, 45, 23, 67, 89, 34]

reversed_numbers = numbers[::-1]

print("Q4 - Reversed:", reversed_numbers)
print("Q4 - Original:", numbers)


# Q5. Second Largest Unique Number

numbers = [45, 12, 89, 34, 89, 67, 45, 23]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Q5 - Second largest:", unique_numbers[-2])


# Q6. Rotate a List

numbers = [10, 20, 30, 40, 50, 60]
k = 2

rotated = numbers[-k:] + numbers[:-k]

print("Q6 - Rotated:", rotated)


# Q7. Remove Duplicates, Preserve Order

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Q7 - Without duplicates:", unique_numbers)


# Q8. Flatten a Nested List

data = [[10, 20], [30, 40], [50, 60]]

flat_list = []

for sublist in data:
    flat_list.extend(sublist)

print("Q8 - Flattened list:", flat_list)


# Q9. Extract Data from a Matrix

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

main_diagonal = [matrix[0][0], matrix[1][1], matrix[2][2]]
secondary_diagonal = [matrix[0][2], matrix[1][1], matrix[2][0]]
middle_column = [matrix[0][1], matrix[1][1], matrix[2][1]]

print("Q9 - Main diagonal:", main_diagonal)
print("Q9 - Main diagonal sum:", sum(main_diagonal))

print("Q9 - Secondary diagonal:", secondary_diagonal)
print("Q9 - Secondary diagonal sum:", sum(secondary_diagonal))

print("Q9 - Middle column:", middle_column)
print("Q9 - Middle column sum:", sum(middle_column))


# Q10. List Transformation Challenge

data = [15, 5, 25, 10, 35, 20, 30]

unique_values = list(set(data))
unique_values.sort()

three_largest = unique_values[-3:]
two_smallest = unique_values[:2][::-1]

result = three_largest + two_smallest

print("Q10 - Final result:", result)
