class Animal:
    def __init__(self, name, age, legs, species, status):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")

class Cat(Animal):
    def __init__(self, name, age, status):
        super().__init__(name, age, 4, 'cat', status)
    
    def introduce(self):
        return super().introduce() + " Meow meow!"


class Dog(Animal):
    def __init__(self, name, age, status, owner):
        super().__init__(name, age, 4, 'dog', status)
        self.owner = owner
    
    def greet_owner(self):
        return f"Hi {self.owner}! Woof! Woof!"
    
    def introduce(self):
        return super().introduce() + " Woof! Woof!"


dog = Dog("Bobo", 9, "hungry", "Daddy")
expected = ("Hello, my name is Bobo and I am 9 years old "
            "and hungry. Woof! Woof!")
print(dog.introduce() == expected)                  # True
print(dog.greet_owner() == "Hi Daddy! Woof! Woof!") # True