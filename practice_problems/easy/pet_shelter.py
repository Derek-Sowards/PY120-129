class Shelter:
    def __init__(self):
        self.adoptions = {}

    def adopt(self, owner_name, pet_name):
        owner_name.all_pets.append(pet_name)
        self.adoptions[owner_name] = []
        self.adoptions[owner_name].append(pet_name)
    
    def print_adoptions(self):
        for object in self.adoptions:
            print()
            print(f"{object.owner_name} has adopted the following pets:")
            object.print_pets()

class Owner:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.all_pets = []
    
    @property
    def name(self):
        return self.owner_name
    
    def number_of_pets(self):
        return len(self.all_pets)
    
    def print_pets(self):
        for pet in self.all_pets:
            print(f'A {pet.species} named {pet.name}')

class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name


cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)


shelter.print_adoptions()
print()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")




# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.