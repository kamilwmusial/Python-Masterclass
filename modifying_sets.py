# Empty sequence within curly braces creates a dict:
numbers = {}

print(numbers, type(numbers))

# Empty sequence within parentheses following a word `set` creates a set:
numbers = set()
print(numbers, type(numbers))

# Adding to a set
# numbers.add(1)
# print(numbers)

# Adding to a set through user input:
# - this code loops around untill 4 unique numbers are entered by the user

# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)

# Using set to remove duplicate values
data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from list:
unique_data = set(data)
print(unique_data)

# Sort the set in alhpabetoc order (creates a list)
unique_data = sorted(set(data))
print(unique_data)

# Keep the list in the original order (as simple set will randomly distribute the items)
# dict.fromkeys() creates a dictionary
unique_data = list(dict.fromkeys(data))
print(unique_data)