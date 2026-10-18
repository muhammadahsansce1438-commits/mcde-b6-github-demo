
# Q21. Unique Values

numbers = [10, 20, 10, 30, 40, 20, 50]

unique_numbers = set(numbers)

print("Q21 - Unique values:", unique_numbers)
print("Q21 - Count:", len(unique_numbers))


# Q22. Set Operations

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("Q22 - Union:", a | b)
print("Q22 - Intersection:", a & b)
print("Q22 - a - b:", a - b)
print("Q22 - Symmetric difference:", a ^ b)


# Q23. Add and Remove

skills = {"Python", "SQL", "AWS"}

skills.add("Snowflake")
skills.add("Databricks")
skills.discard("AWS")

print("Q23 - Updated skills:", skills)


# Q24. Common Students

python_students = {"Ali", "Sara", "Ahmed", "Zain"}
sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}

both_courses = python_students & sql_students
exactly_one_course = python_students ^ sql_students

print("Q24 - Both courses:", both_courses)
print("Q24 - Exactly one course:", exactly_one_course)


# Q25. Subset and Superset

required_skills = {"Python", "SQL"}
candidate_skills = {"Python", "SQL", "AWS", "Snowflake"}

print("Q25 - Required is subset:", required_skills.issubset(candidate_skills))
print("Q25 - Candidate is superset:", candidate_skills.issuperset(required_skills))


# Q26. Missing Numbers

numbers = {1, 2, 4, 6, 8, 10}

all_numbers = set(range(1, 11))
missing_numbers = all_numbers - numbers

print("Q26 - Missing numbers:", missing_numbers)


# Q27. Three-Set Analysis

python = {"Ali", "Sara", "Ahmed", "Zain"}
sql = {"Sara", "Ahmed", "Hamza"}
aws = {"Ahmed", "Zain", "Hamza"}

all_three = python & sql & aws
python_sql_only = (python & sql) - aws

at_least_two = (
    (python & sql)
    | (python & aws)
    | (sql & aws)
)

print("Q27 - All three:", all_three)
print("Q27 - Python and SQL only:", python_sql_only)
print("Q27 - At least two:", at_least_two)


# Q28. Transaction Analysis

day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}
day3 = {104, 106, 107, 108}

all_days = day1 & day2 & day3

exactly_one_day = (
    (day1 - day2 - day3)
    | (day2 - day1 - day3)
    | (day3 - day1 - day2)
)

at_least_two_days = (
    (day1 & day2)
    | (day1 & day3)
    | (day2 & day3)
)

print("Q28 - All days:", all_days)
print("Q28 - Exactly one day:", exactly_one_day)
print("Q28 - At least two days:", at_least_two_days)


# Q29. Access Control

required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write", "delete"}

missing_permissions = required_permissions - user_permissions
extra_permissions = user_permissions - required_permissions
fully_authorized = required_permissions.issubset(user_permissions)

print("Q29 - Missing permissions:", missing_permissions)
print("Q29 - Extra permissions:", extra_permissions)
print("Q29 - Fully authorized:", fully_authorized)


# Q30. Customer Segmentation

website = {"C1", "C2", "C3", "C4", "C5"}
mobile = {"C3", "C4", "C6", "C7"}
store = {"C2", "C4", "C7", "C8"}

exactly_one = (
    (website - mobile - store)
    | (mobile - website - store)
    | (store - website - mobile)
)

exactly_two = (
    ((website & mobile) - store)
    | ((website & store) - mobile)
    | ((mobile & store) - website)
)

all_three = website & mobile & store

print("Q30 - Exactly one platform:", exactly_one)
print("Q30 - Exactly two platforms:", exactly_two)
print("Q30 - All three platforms:", all_three)
