class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

        # getter name

    def get_name(self):
        return self.__name

    # setter name
    def set_name(self, name):
        self.__name = name

    # getter age
    def get_age(self):
        return self.__age

    # setter age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Возраст должен быть больше 0")

    def make_sound(self):
        return "Some sound"


class Dog(Animal):
    def make_sound(self):
        return "Гав-гав"


class Cat(Animal):
    def make_sound(self):
        return "Мяу"


dog = Dog("Бобик", 3)
cat = Cat("Мурка", 1)

print(dog.get_name(), dog.get_age(), dog.make_sound())
print(cat.get_name(), cat.get_age(), cat.make_sound())

cat.set_age(2)
print(cat.get_age())
