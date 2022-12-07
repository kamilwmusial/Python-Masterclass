data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]
# 1 - print to a file: print performs various conversions on data such as include line breaks and separators
plants_filename = "flowers_print.txt"

with open(plants_filename, "w") as plants:
    for plant in data:
        print(plant, file=plants)

# 2 - save data to the list:
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
# print(new_list)

# 3 - write data to the file: sends exactly what you specify to the file
# plants_filename = "flowers_write.txt"
#
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         plants.write(plant)
#
# print(data)
# string_representation = data.__str__()
# print(type(string_representation))

# writing numerical values to a file #1: (print method automatically adds new line)
filename = "test_numbers.txt"
with open(filename, "w") as test:
    for i in range(10):
        print(i, file=test)

# write method throws a warning when trying to write numbers to the text file, use str function
with open(filename, "w") as test:
    for i in range(10):
        test.write(str(i) + "\n")



















