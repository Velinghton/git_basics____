class Person:
    ...

class Owner(Person):
    def __init__(self, *args):
        self.pets = args

class OwnedPets(Owner):
    

class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


class Pet(Animal):
    ...

class Cat(Animal):
    ...

class Dog(Animal):
    ...

class Cow(Animal):
    ...
