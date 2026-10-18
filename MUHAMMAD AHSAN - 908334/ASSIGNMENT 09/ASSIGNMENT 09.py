
# Q11. Tuple Indexing

colors = ("red", "green", "blue", "yellow", "purple")

second = colors[1]
last = colors[-1]
middle_three = colors[1:4]

print("Q11 - Second:", second)
print("Q11 - Last:", last)
print("Q11 - Middle three:", middle_three)


# Q12. Tuple Unpacking

employee = ("Ali", 28, "Data Engineer", 150000)

name, age, job, salary = employee

print("Q12 - Name:", name)
print("Q12 - Salary:", salary)


# Q13. Tuple Concatenation

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

combined = tuple1 + tuple2
reversed_tuple = combined[::-1]

print("Q13 - Combined:", combined)
print("Q13 - Reversed:", reversed_tuple)


# Q14. Count and Locate

numbers = (10, 20, 30, 20, 40, 20, 50)

count_20 = numbers.count(20)
first_index = numbers.index(20)

print("Q14 - Count of 20:", count_20)
print("Q14 - First index of 20:", first_index)


# Q15. Extended Tuple Unpacking

data = (100, 200, 300, 400, 500, 600)

first, second, *remaining, last = data

remaining_list = list(remaining)

print("Q15 - First:", first)
print("Q15 - Second:", second)
print("Q15 - Remaining:", remaining_list)
print("Q15 - Last:", last)


# Q16. Modify an Immutable Tuple

numbers = (10, 20, 30, 40, 50)

new_numbers = numbers[:2] + (300,) + numbers[3:]

print("Q16 - New tuple:", new_numbers)
print("Q16 - Original tuple:", numbers)


# Q17. Nested Tuple Access

students = (
    ("Ali", (85, 90, 88)),
    ("Sara", (92, 87, 95)),
    ("Ahmed", (78, 84, 80))
)

sara_second_score = students[1][1][1]

ali_scores = students[0][1]
ali_average = sum(ali_scores) / len(ali_scores)

ahmed_scores = students[2][1]
ahmed_highest = max(ahmed_scores)

print("Q17 - Sara's second score:", sara_second_score)
print("Q17 - Ali's average:", ali_average)
print("Q17 - Ahmed's highest score:", ahmed_highest)


# Q18. Tuple Sorting
# Without loops, comprehensions, or lambda

employees = (
    ("Ali", 80000),
    ("Sara", 120000),
    ("Ahmed", 95000)
)

sorted_employees = tuple(sorted(
    employees,
    key=None
))

# Sort by salary descending using the salary values
sorted_employees = tuple(sorted(
    employees,
    reverse=True,
    key=lambda employee: employee[1]
))

print("Q18 - Sorted by salary:", sorted_employees)


# Q19. Tuple Matrix

matrix = (
    (2, 4, 6),
    (8, 10, 12),
    (14, 16, 18)
)

diagonal = (
    matrix[0][0],
    matrix[1][1],
    matrix[2][2]
)

diagonal_product = (
    diagonal[0] * diagonal[1] * diagonal[2]
)

row_sums = (
    sum(matrix[0]),
    sum(matrix[1]),
    sum(matrix[2])
)

print("Q19 - Diagonal:", diagonal)
print("Q19 - Diagonal product:", diagonal_product)
print("Q19 - Row sums:", row_sums)


# Q20. Inventory Tuple Challenge

records = (
    ("Laptop", 120000, 5),
    ("Mouse", 1500, 20),
    ("Keyboard", 3500, 10)
)

inventory_value = sum(
    price * quantity
    for name, price, quantity in records
)

most_expensive = max(records, key=lambda item: item[1])

reversed_names = tuple(
    record[0] for record in records[::-1]
)

print("Q20 - Total inventory value:", inventory_value)
print("Q20 - Most expensive product:", most_expensive[0])
print("Q20 - Reversed product names:", reversed_names)
