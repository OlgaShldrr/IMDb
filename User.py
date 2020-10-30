#Define user with name and age
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if int(age)>=18:
            print("Welcome ", name, "! Thanks for providing your age (", age,"). You are above the legal age, so your movie recommendation will be adjusted accordingly")
        else:
            print("Welcome ", name, "! Thanks for providing your age (", age, "). You are below the legal age, so your movie recommendation will be adjusted accordingly")