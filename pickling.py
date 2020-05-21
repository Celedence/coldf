import pickle


class Animal:
    def __init__(self, species):
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def sound(self, snd):
        print (f"A {self.species} says {snd}")

class Cat(Animal):
    def __init__(self, name, breed, species, toy):
        super().__init__(species="Cat")
        self.name = name
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


# blue = Cat("Chubs","orange","mammamal","string")

# with open("pets.pickle", "wb") as file:
#     pickle.dump(blue, file)

with open("pets.pickle", "rb")as file:
    zombie_blue = pickle.load(file)
    print(zombie_blue)