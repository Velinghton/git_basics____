class Person:
    def __init__(self,name, *args):
        self.name = name
        self.pets = args
class Owner(Person):
    ...
class OwnedPets(Owner):

    def show_pets(self):
        return self.__dict__
    def add_new_pet(self):
        list_of_pets.append(self.__dict__)
        return list_of_pets
    def union_pets(*args):
        res = {}
        for i in args:
            for k, v in i.__dict__.items():
                res[k]=res.get(k, []) + [v]
        return res



class Animal:
    names = []
    def __init__(self, pets, age, color):
        self.pets = pets
        self.age = age
        self.color = color
        self.names.append(pets)

class Pet(Animal, OwnedPets):
    ...

class Cat(Pet):
    ...
class Dog(Pet):
    ...
class Cow(Pet):
    ...

if __name__ == '__main__':
    list_of_pets = []
    #відображення домашніх улюбленців що є у власника
    bob = OwnedPets("Bob", "cat", "dog", "cow")
    liza = OwnedPets("Liza", "rabbit", "mouse", "cow")
    for i in(bob, liza):
        print(f'{i.name} має таких тварин: {i.pets}')
        print(i.show_pets())
        print()

    # Обєднання тварин
    print(f'Обєднання тварин двох власників: \n{OwnedPets.union_pets(bob, liza)}')
    print()

    #Додавання нової тварини
    cat = Cat('cat', 55, 'red')
    dog = Dog("dog", 100, 'black')
    cow = Cow("cow", 77, 'green')
    cow1 = Cow("cow1", 40, 'yellow')
    cow2 = Cow("cow2", 10, "brown")
    for i in (cat, dog, cow, cow1):
        i.add_new_pet()
    print(f'Список доданих тварин: {list_of_pets}')
    print(f"Список доданих тварин: {cat.names}")
    print()

