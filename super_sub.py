animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark'
           'Cat'
           }
birds = {'Robin', 'Swallow', 'Wren'}
# using methods:
# return true if is a subset and superset
print(f'birds is a subset of aminals: {birds.issubset(animals)}')
print(f'animals is a superset of birds: {animals.issuperset(birds)}')
print(f'birds is a superset of animals: {birds.issuperset(animals)}')

# using operators:
print(birds <= animals)
print(animals > birds)
print(birds > animals)

print('*' * 80)

garden_birds = {'Swallow', 'Wren', 'Robin'}
print(garden_birds == birds) # checks if sets are equal

# but garden birds are not a SUPERSET of birds:
print(garden_birds <= birds) # checks if a subset
print(garden_birds < birds) # checks if a superset

print('*' * 80)

more_birds = {'Wren', 'Budgie', 'Swallow'}
print(garden_birds >= more_birds)
