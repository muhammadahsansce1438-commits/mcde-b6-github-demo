
# Q41 Student Performance System

students = [
    {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
    {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
    {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
]

print("\nQ41")

averages = {}

for student in students:
    avg = sum(student["marks"]) / len(student["marks"])
    averages[student["name"]] = avg
    print(student["name"], "Average:", avg)

print("Top Student:", max(averages, key=averages.get))
print("Names:", tuple(s["name"] for s in students))
print("Unique Marks:", set(m for s in students for m in s["marks"]))


# Q42 Employee Skills

employees = {
    "Ali": {"Python", "SQL", "AWS"},
    "Sara": {"Python", "Databricks", "SQL"},
    "Ahmed": {"AWS", "Snowflake", "SQL"}
}

print("\nQ42")

print("Common Skills:", set.intersection(*employees.values()))
print("Ali Only:", employees["Ali"] - employees["Sara"] - employees["Ahmed"])

all_skills = set()
for skills in employees.values():
    all_skills.update(skills)

print("All Skills:", all_skills)

for name, skills in employees.items():
    if "Python" in skills and "SQL" in skills:
        print("Python + SQL:", name)


# Q43 Sales Data

sales = [
    ("Laptop", 120000, 2),
    ("Mouse", 1500, 5),
    ("Keyboard", 3500, 3)
]

print("\nQ43")

revenue = {}

for name, price, quantity in sales:
    revenue[name] = price * quantity

print("Revenue:", revenue)
print("Total Revenue:", sum(revenue.values()))
print("Top Product:", max(revenue, key=revenue.get))
print("Unique Prices:", {item[1] for item in sales})


# Q44 Customer Orders

customers = {
    "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
    "C102": {"name": "Sara", "orders": [3000, 4500]},
    "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
}

print("\nQ44")

totals = {}

for cid, data in customers.items():
    totals[cid] = sum(data["orders"])
    print(data["name"], "Spending:", totals[cid])

top_id = max(totals, key=totals.get)
print("Top Customer:", customers[top_id]["name"])
print("Totals Tuple:", tuple(totals[cid] for cid in sorted(totals)))


# Q45 Course Enrollment

courses = {
    "Python": {"Ali", "Sara", "Ahmed"},
    "SQL": {"Sara", "Ahmed", "Zain"},
    "AWS": {"Ali", "Ahmed", "Zain"}
}

print("\nQ45")

counts = {}

for students in courses.values():
    for name in students:
        counts[name] = counts.get(name, 0) + 1

print("Exactly Two:", [n for n in counts if counts[n] == 2])
print("All Three:", [n for n in counts if counts[n] == 3])
print("Exactly One:", [n for n in counts if counts[n] == 1])

unique_students = set()
for students in courses.values():
    unique_students.update(students)

print("Unique Students:", unique_students)
print("Count:", len(unique_students))


# Q46 E-Commerce Transactions

transactions = [
    {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
    {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
    {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
]

print("\nQ46")

total_revenue = 0
ali_spending = 0
transaction_totals = {}
products = set()

for transaction in transactions:
    total = 0

    for name, price, quantity in transaction["items"]:
        total += price * quantity
        products.add(name)

    transaction_totals[transaction["id"]] = total
    total_revenue += total

    if transaction["customer"] == "Ali":
        ali_spending += total

print("Total Revenue:", total_revenue)
print("Ali Spending:", ali_spending)
print("Largest Transaction:", max(transaction_totals, key=transaction_totals.get))
print("Products:", products)


# Q47 Pipeline Monitoring

pipelines = {
    "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
    "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
    "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
}

print("\nQ47")

pipeline_totals = {}

for name, data in pipelines.items():
    total = sum(data["records"])
    pipeline_totals[name] = total
    print(name, "Total:", total)
    print("Average:", total / len(data["records"]))

print("Total Processed:", sum(pipeline_totals.values()))
print("Failed:", [n for n in pipelines if pipelines[n]["status"] == "failed"])
print("Largest Pipeline:", max(pipeline_totals, key=pipeline_totals.get))


# Q48 Banking Transactions

accounts = {
    "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
    "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
    "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
}

print("\nQ48")

balances = {}

for aid, data in accounts.items():
    balances[aid] = sum(data["transactions"])
    print(data["holder"], "Balance:", balances[aid])

withdrawals = sum(
    abs(t)
    for data in accounts.values()
    for t in data["transactions"] if t < 0
)

deposits = [
    t for data in accounts.values()
    for t in data["transactions"] if t > 0
]

top_account = max(balances, key=balances.get)

print("Highest Balance:", accounts[top_account]["holder"], balances[top_account])
print("Total Withdrawals:", withdrawals)
print("Largest Deposit:", max(deposits))


# Q49 Product Recommendations

users = {
    "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
    "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
    "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
}

print("\nQ49")

purchase_counts = {}

for data in users.values():
    for product in data["purchased"]:
        purchase_counts[product] = purchase_counts.get(product, 0) + 1

print("Bought by at Least Two:", [p for p in purchase_counts if purchase_counts[p] >= 2])
print("Ali Wishlist Minus Purchases:", users["Ali"]["wishlist"] - users["Ali"]["purchased"])

shared_wishlist = set.intersection(
    *(data["wishlist"] for data in users.values())
)
print("Shared Wishlist:", shared_wishlist)

all_products = set()
for data in users.values():
    all_products.update(data["purchased"])
    all_products.update(data["wishlist"])

print("All Products:", all_products)


# Q50 Final Company Analysis

company = {
    "departments": {
        "Engineering": {
            "employees": [
                ("Ali", 120000, {"Python", "AWS", "SQL"}),
                ("Sara", 150000, {"Python", "Databricks", "SQL"})
            ],
            "budget": 500000
        },
        "Analytics": {
            "employees": [
                ("Ahmed", 100000, {"SQL", "Power BI"}),
                ("Zain", 130000, {"Python", "SQL", "Tableau"})
            ],
            "budget": 400000
        }
    }
}

print("\nQ50")

departments = company["departments"]
payroll = {}
all_employees = []
department_skills = {}

for dept, data in departments.items():
    payroll[dept] = 0
    department_skills[dept] = set()

    for employee in data["employees"]:
        name, salary, skills = employee
        payroll[dept] += salary
        all_employees.append(employee)
        department_skills[dept].update(skills)

    print(dept, "Payroll:", payroll[dept])
    print("Remaining Budget:", data["budget"] - payroll[dept])

company_payroll = sum(payroll.values())
highest_paid = max(all_employees, key=lambda e: e[1])

shared_skills = set.intersection(*department_skills.values())
engineering_only = department_skills["Engineering"] - department_skills["Analytics"]

averages = {
    dept: payroll[dept] / len(data["employees"])
    for dept, data in departments.items()
}

name_salary = {name: salary for name, salary, skills in all_employees}

all_skills = set()
for skills in department_skills.values():
    all_skills.update(skills)

combined_budget = sum(data["budget"] for data in departments.values())

print("Company Payroll:", company_payroll)
print("Highest Paid:", highest_paid[0], highest_paid[1])
print("Shared Skills:", shared_skills)
print("Engineering-Only Skills:", engineering_only)
print("Average Salaries:", averages)
print("Higher Average Salary:", max(averages, key=averages.get))
print("Name-to-Salary:", name_salary)
print("All Unique Skills:", all_skills)
print("Combined Budget:", combined_budget)
print("Budget Sufficient:", combined_budget >= company_payroll)
