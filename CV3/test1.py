class Dog:
    species = "Domestic"

    def __init__(self, name):
        self.name = name  # instance attribute

if __name__ == "__main__":
    dog1 = Dog("Daisy")
    dog2 = Dog("Odin")

    dog1.species = "test"
    print(dog1.species)
    print(dog2.species)