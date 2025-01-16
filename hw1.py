class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "женат" if self.is_married else "не женат"
        print(f"Привет! Меня зовут {self.full_name}. Мне {self.age} лет. Я {marital_status}.")

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def show_marks(self):
        print(f"Оценки студента {self.full_name}:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")

    def average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

class Teacher(Person):
    def __init__(self, full_name, age, is_married, experience, base_salary):
        super().__init__(full_name, age, is_married)
        self.experience = experience
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus = 0
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * self.base_salary
        return self.base_salary + bonus


def create_students():
    student1 = Student("Мухамадов Улукбек", 20, False, {"Математика": 5, "Физика": 5, "Химия": 5})
    student2 = Student("Мухамадов Бекболсун", 22, True, {"Математика": 4, "Физика": 5, "Химия": 3})
    student3 = Student("Мухамадов Нурдоолот", 18, False, {"Математика": 3, "Физика": 4, "Химия": 5})

    students = [student1, student2, student3]
    return students


teacher = Teacher("Каратаев Абдуламит", 46, True, 26, 50000)
teacher.introduce_myself()
print(f"Зарплата учителя: {teacher.calculate_salary()}")

students = create_students()

for student in students:
    student.introduce_myself()
    student.show_marks()
    print(f"Средняя оценка: {student.average_mark():.2f}\n")

print("End of program")