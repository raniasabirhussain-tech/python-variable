# Variables
name = "Lin"
country = "USA"
grade = 13
# -------------------------

# Method 1: Print variables individually
print(name)
print(country)
print(grade)

# Separator
print("______________")

# Method 2: Print using commas (Python automatically adds spaces and converts numbers)
print("My name is", name, "I live in", country, "and I study in", grade)

# Method 3: Print using f-strings (clean and modern way)
print(f"My name is {name}, I live in {country}, and I study in {grade}")

# Method 4: Print using concatenation (numbers must be converted to strings)
print("My name is " + name + " I live in " + country + " and I study in " + str(grade))
