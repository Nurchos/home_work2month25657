from datetime import datetime


class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self._birth_date = birth_date  # приватный (по заданию)
        self._occupation = occupation  # приватный
        self._higher_education = higher_education  # приватный

    @property
    def occupation(self):
        return self._occupation

    @property
    def higher_education(self):
        return self._higher_education

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def age(self):
        birth = datetime.strptime(self._birth_date, "%d.%m.%Y")
        today = datetime.today()
        return today.year - birth.year - (
                (today.month, today.day) < (birth.month, birth.day)
        )

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. {edu_text}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Я учился с Айсулуу в группе {self.group}. "
            f"{edu_text}."
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Мое хобби {self.hobby}. "
            f"{edu_text}."
        )


cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()

print(fr1.age)
