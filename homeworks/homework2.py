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


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник/одногруппник, "
              f"учусь в группе {self.group_name}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг, мое хобби — {self.hobby}.")


classmate1 = Classmate("Бектур", "2005-05-10", "студент", False, "IT-101")
classmate2 = Classmate("Алина", "2004-09-22", "студент", True, "IT-102")

friend1 = Friend("Алмаз", "2003-03-15", "дизайнер", False, "рисование")
friend2 = Friend("Данияр", "2002-12-01", "программист", True, "игры")

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()
