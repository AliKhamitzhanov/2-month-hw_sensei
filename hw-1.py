class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Имя: {self.fullname}\n"
              f"Возраст: {self.age}\n"
              f"Женат/Замужем: {self.is_married}")


class Student(Person):
    def __init__(self, fullname, age, is_married, **marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average(self):
        print(sum(self.marks) // len(self.marks))


class Teacher(Person):
    salary = 55000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def get_salary(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary/100*5) * (self.experience-3))
            return new_salary


def create_students():
    eren = Student('Amanturov Eren', 17, False, geo=5, geom=5, physics=5, OBJ=4)
    ali = Student('Khamitzhanov Ali', 17, True, geo=5, geom=2, physics=2, OBJ=5)
    zhora = Student('Zhora', 30, True, geo=5, geom=5, physics=5, OBJ=4)
    return [eren, ali, zhora]


students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Name: {i.fullname}\n"
          f"Age: {i.age}\n"
          f"Married: {i.is_married}\n"
          f"Average marks: {sum(list)/len(list)}\n")

