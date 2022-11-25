# range will be displayed in what appears to be order, but IS UNORDERED
small_ints = set(range(21))
print(small_ints)

# Clear items from the set
# small_ints.clear()
# print(small_ints)

# To remove individual items

small_ints.discard(10)
print(small_ints)
small_ints.remove(11)
print(small_ints)

# .remove will let us know if an item is not in the set, .discard will NOT
small_ints.discard(99)
print(small_ints)
small_ints.remove(99)
print(small_ints)
