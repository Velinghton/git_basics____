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
    def __init__(self, owner:Owner, name):
        self.name = name
        self.owner = owner
        self.all_pets.append(self.__class__.__name__)

    def __repr__(self):
        return f"{self.owner} - має {self.__class__.__name__} по імені : {self.name}"

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
    #Створення тварин
    cat = Dog("Le", "sharik")
    dog = Cat("Ro","myrzik")
    cow = Cow("Lia", "milka")
    dog = Dog("Rita", "tor")
    print(cow)
    print(cat)
    print(dog)
    #Створення власника який має тварину
    roma = Owner("Roma", "cat", "ziza")
    print(roma)
    #Збираємо всіх тварин в один контейнер(рet)
    pet = Pet(cat, dog)
    print(pet)
    #Перевірка чи є певнай тип тварини у контейнері(рet)(__contains__)
    print(cow in pet)
    print(cat in pet)
    #Перевіряємо кількіть тварин у контейнері(__len__)
    print(len(pet))
    #виклик з контейнера по індексу (__getitem__)
    print(pet[0])
    #Заміна тварини в контейнері за індексом (__setitem__)
    pet[0]=Dog("Le", "bim")
    print(pet[0])
    #Список тварин які  було створено
    print(cat.all_pets)
    #Cкільки тварин одного типу (приклад Dog) було створено
    print(cat.all_pets.count("Dog"))








