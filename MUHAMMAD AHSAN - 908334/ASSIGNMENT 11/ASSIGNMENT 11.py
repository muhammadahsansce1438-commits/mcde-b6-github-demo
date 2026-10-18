
# Q31. Dictionary Access

student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}

print("Q31 - Name:", student["name"])
print("Q31 - Marks:", student["marks"])
print("Q31 - City:", student.get("city", "Karachi"))


# Q32. Update Dictionary

employee = {"name": "Sara", "salary": 100000, "department": "IT"}

employee["salary"] = employee["salary"] * 1.20
employee["bonus"] = 15000
employee["department"] = "Data Engineering"

print("\nQ32 - Updated employee:", employee)


# Q33. Dictionary Methods

product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}

print("\nQ33 - Keys:", product.keys())
print("Q33 - Values:", product.values())
print("Q33 - Items:", product.items())

removed_stock = product.pop("stock")
print("Q33 - Removed stock value:", removed_stock)
print("Q33 - Updated product:", product)


# Q34. Merge Dictionaries

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 50, "d": 40}

merged = {**dict1, **dict2}

print("\nQ34 - Merged dictionary:", merged)


# Q35. Student Marks

marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}

highest = max(marks.values())
lowest = min(marks.values())
average = sum(marks.values()) / len(marks)
top_student = max(marks, key=marks.get)

print("\nQ35 - Highest marks:", highest)
print("Q35 - Lowest marks:", lowest)
print("Q35 - Average marks:", average)
print("Q35 - Top student:", top_student)


# Q36. Nested Employee Records

employees = {
    "E101": {"name": "Ali", "salary": 80000},
    "E102": {"name": "Sara", "salary": 120000},
    "E103": {"name": "Ahmed", "salary": 95000}
}

print("\nQ36 - Sara salary:", employees["E102"]["salary"])

employees["E101"]["salary"] *= 1.15

total_payroll = (
    employees["E101"]["salary"]
    + employees["E102"]["salary"]
    + employees["E103"]["salary"]
)

print("Q36 - Ali's updated salary:", employees["E101"]["salary"])
print("Q36 - Total payroll:", total_payroll)


# Q37. Dictionary Inversion
# No loops or comprehensions

data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}

inverse = {
    data["Python"]: "Python",
    data["SQL"]: "SQL",
    data["AWS"]: "AWS"
}

print("\nQ37 - Inverse dictionary:", inverse)


# Q38. Order Calculation

order = {
    "laptop": {"price": 120000, "quantity": 2},
    "mouse": {"price": 1500, "quantity": 5},
    "keyboard": {"price": 3500, "quantity": 3}
}

laptop_subtotal = order["laptop"]["price"] * order["laptop"]["quantity"]
mouse_subtotal = order["mouse"]["price"] * order["mouse"]["quantity"]
keyboard_subtotal = order["keyboard"]["price"] * order["keyboard"]["quantity"]

grand_total = laptop_subtotal + mouse_subtotal + keyboard_subtotal
discount = grand_total * 0.10
final_amount = grand_total - discount

print("\nQ38 - Laptop subtotal:", laptop_subtotal)
print("Q38 - Mouse subtotal:", mouse_subtotal)
print("Q38 - Keyboard subtotal:", keyboard_subtotal)
print("Q38 - Grand total:", grand_total)
print("Q38 - Discount:", discount)
print("Q38 - Amount after discount:", final_amount)


# Q39. Employee Performance

employees = {
    "Ali": {"python": 90, "sql": 85, "aws": 88},
    "Sara": {"python": 95, "sql": 92, "aws": 90},
    "Ahmed": {"python": 80, "sql": 87, "aws": 84}
}

ali_average = (
    employees["Ali"]["python"]
    + employees["Ali"]["sql"]
    + employees["Ali"]["aws"]
) / 3

sara_average = (
    employees["Sara"]["python"]
    + employees["Sara"]["sql"]
    + employees["Sara"]["aws"]
) / 3

ahmed_average = (
    employees["Ahmed"]["python"]
    + employees["Ahmed"]["sql"]
    + employees["Ahmed"]["aws"]
) / 3

averages = {
    "Ali": ali_average,
    "Sara": sara_average,
    "Ahmed": ahmed_average
}

top_performer = max(averages, key=averages.get)

highest_sql_score = max(
    employees["Ali"]["sql"],
    employees["Sara"]["sql"],
    employees["Ahmed"]["sql"]
)

print("\nQ39 - Employee averages:", averages)
print("Q39 - Top performer:", top_performer)
print("Q39 - Highest SQL score:", highest_sql_score)


# Q40. Inventory Management

inventory = {
    "P101": {"name": "Laptop", "price": 120000, "stock": 5},
    "P102": {"name": "Mouse", "price": 1500, "stock": 20},
    "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
}

laptop_value = inventory["P101"]["price"] * inventory["P101"]["stock"]
mouse_value = inventory["P102"]["price"] * inventory["P102"]["stock"]
keyboard_value = inventory["P103"]["price"] * inventory["P103"]["stock"]

total_value = laptop_value + mouse_value + keyboard_value

item_values = {
    "Laptop": laptop_value,
    "Mouse": mouse_value,
    "Keyboard": keyboard_value
}

most_valuable_item = max(item_values, key=item_values.get)

inventory["P101"]["stock"] -= 2
inventory["P102"]["stock"] -= 5

print("\nQ40 - Total inventory value:", total_value)
print("Q40 - Most valuable item:", most_valuable_item)
print("Q40 - Updated inventory:", inventory)
