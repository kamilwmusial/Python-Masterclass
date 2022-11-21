# Shallow copy Vs Deep Copy
# Shallow copy is just a copy of the reference to the given list
#
#

import copy    # imports the deep copy function

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}
# Perform a shallow copy:
# things = animals.copy()

# Perform a deep copy:
# things = copy.deepcopy(animals)

# under shallow copy the id will be the same, but different for deep copy
print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])