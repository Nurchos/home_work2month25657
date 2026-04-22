class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, "
              f"по профессии {self.occupation}, высшего образования {education}.")


# Создание экземпляров
person1 = Person("Алексей", "1995-03-12", "программист", True)
person2 = Person("Мария", "2000-07-25", "дизайнер", False)
person3 = Person("Иван", "1988-11-03", "инженер", True)

# Вывод атрибутов
for person in [person1, person2, person3]:
    print("Имя:", person.name)
    print("Дата рождения:", person.birth_date)
    print("Профессия:", person.occupation)
    print("Высшее образование:", person.higher_education)
    print()

# Вызов метода introduce
person1.introduce()
person2.introduce()
person3.introduce()