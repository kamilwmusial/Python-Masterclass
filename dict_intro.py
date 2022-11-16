vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R110',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': "Ford Fiesta Ghia 1.4",
}

# Add item to the dictionary:
vehicles["starfighter"] = "Lockheed F104"
vehicles["learjet"] = "Bombardier Learjet 75"

# Challenge: add glider with key toy
vehicles["toy"] = "Glider"

# Change value of an item:
vehicles["virago"] = "Yamaha XV535"

# Deleting items from the list: - using del and specifying the key in the given dictionary
del vehicles["starfighter"]
#del vehicles["f1"] - creates error as key not in the dictionary
# .pop method with , None will not crash the program but if the key does not exist it return whatever is passed for default
result = vehicles.pop("f1", None)
print(result)
print()

plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()
# Methods of searching through dictionary:
# indexing method (faster but if key does not exist will crash program)
#my_car = vehicles['fiesta']
#print(my_car)

#commuter = vehicles['virago']
#print(commuter)

# .get method (slower but will return None if the key does not exist - use when unsure if key exists or not)
#learner = vehicles.get("er5")
#print(learner)

# for loop returning all items in the dictionary with the key separated by comma from the items
#for key in vehicles:
#    print(key, vehicles[key], sep=", ")

# more efficient way, iterating over items
for key, value in vehicles.items():
    print(key, value, sep=", ")