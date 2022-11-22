data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]
# Print a unicode of a, b and z:
# print(ord("a"))
# print(ord("b"))
# print(ord("z"))

def simple_hash(s: str) -> int:
    """A very simple hash"""
    basic_hash = ord(s[0])
    return basic_hash % 10

# Testing the hash function:
# for key, value in data:
#     # Using simple hash function:
#     # h = simple_hash(key)
#     # Using Python's built in hash function:
#     h = hash(key)
#     print(key, h)


def get(k: str) -> str:
    """Return the value for a key, or None if the key does not exist"""
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    # h = hash(key)
    print(key,h)
    keys[h] = key
    values[h] = value

print(keys)
print(values)
print("---------------")
value = get("grape")
print(value)
