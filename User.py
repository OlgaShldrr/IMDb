#Define user with name and age
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Welcome ", name, "! Thanks for providing your age (", age, ") Your movie recommendation will be adjusted accordingly")