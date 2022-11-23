farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

# Sets are unordered, and will appear in different order each time the program is run
# Python recognises the sequence as a set, as for a dictionary each item would have a key and a value and be separated by a colon
# If the sequence would be in parethesis or no brackers, it would be a tuple,
# if the sequence would be in square brackets it would be a list

# it is possible to iterate over a set, but becuase sets are unordered, the result is different each time
for animal in farm_animals:
    print(animal)

# it also not possible to index (OR SLICE) a set
# you can index a list:
print()
print("Indexing a sequence")
animals_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animals_list[3]
print(goat)

# but not a set: - results in 'set' objet is not subsciptable error
print()
# print("Indexing a set is not possible")
# goat = farm_animals[3]

# Python considers two sets to be equal if they contain the same items, even if they are in a different order
# this is different from lists and tuples, which will consider the sequence to be the same if it is in same order
more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
if more_animals == farm_animals:
    print('The sets are equal')
else:
    print('The sets are different')
