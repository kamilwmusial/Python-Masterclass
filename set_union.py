# Animals sets:
farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
pet_animals = {"dog", "cat", "fish", "bird", "horse"}

# Combine two sets
all_animals_1 = farm_animals.union(wild_animals)
all_animals_2 = wild_animals.union(farm_animals)
all_animals_3 = wild_animals | farm_animals
# Combine all three sets:
all_animals_4 = wild_animals | farm_animals | pet_animals
all_animals_5 = farm_animals.union(wild_animals).union(pet_animals)

print(all_animals_1)
print(all_animals_2)
print(all_animals_3)
print(all_animals_4)
print(all_animals_5)

