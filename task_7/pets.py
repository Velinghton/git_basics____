class Person:
    def __init__(self,name):
        self.name = name
class Owner(Person):
    def __init__(self,name, pets, name_pets):
        self.name = name
        self.pets = pets
        self.name_pets = name_pets
    def __repr__(self):
        return f"{self.name} має {self.pets} по імені : {self.name_pets}"
class OwnedPets(Owner):
    ...
class Animal():
    all_pets = []
    def __init__(self, owner:Owner, name, say_somesing=None):
        self.name = name
        self.owner = owner
        self.say_somesing = say_somesing
        self.all_pets.append(self.__class__.__name__)

    def __repr__(self):
        return f"{self.owner} - має {self.__class__.__name__} по імені : {self.name}"
    def say_something(self):
        return  f"{self.__class__.__name__} може казати: {self.say_somesing.upper()} "


class Cat(Animal):
  ...

class Dog(Animal):
    ...
class Cow(Animal):
    ...
class Pet():
    def __init__(self, *animal:Animal):
        self.container = []
        self.container.extend(animal)
    def __repr__(self):
        return f"All {self.container}"
    def __contains__(self, item):
        return item in self.container
    def __len__(self):
        return len(self.container)
    def __getitem__(self, item):
        if item < 0 or item > len(self.container):
            raise f"IndexError - введіть вірний індекс в межах {len(self.container)}"
        return self.container[item]
    def __setitem__(self, key, value):
        if key < 0 or key > len(self.container):
            raise f"IndexError - введіть вірний індекс в межах {len(self.container)}"
        self.container[key] = value


if __name__ == '__main__':
    print('#Створення тварин')
    dog = Dog("Le", "sharik", "gawww")
    cat = Cat("Ro","myrzik", "muurrr")
    cow = Cow("Lia", "milka", "muuuuuuu")
    dog1 = Dog("Rita", "tor", "rrrrrr")
    print(cow)
    print(cat)
    print(dog)
    print()
    print("#Створення власника який має тварину")
    roma = Owner("Roma", "cat", "ziza")
    print(roma)
    print()
    print("#Збираємо  тварин в один контейнер(рet)")
    pet = Pet(cat, dog)
    print(pet)
    print()
    print("#Перевірка чи є певнай тип тварини у контейнері(рet)(__contains__)")
    print(f"cow in pet -  {cow in pet}")
    print(f"cow in pet -  {cat in pet}")
    print()
    print("#Перевіряємо кількіть тварин у контейнері(__len__)")
    print(len(pet))
    print()
    print("#виклик з контейнера по індексу (__getitem__)")
    print(pet[0])
    print()
    print("#Заміна тварини в контейнері за індексом (__setitem__)")
    pet[0]=Dog("Le", "bim")
    print(pet[0])
    print()
    print("#Список тварин які  було створено")
    print(cat.all_pets)
    print()
    print("#Cкільки тварин одного типу (приклад Dog) було створено")
    print(cat.all_pets.count("Dog"))
    print()
    print("#приклад які звуки робить пeвна тварина")
    print(dog.say_something())




