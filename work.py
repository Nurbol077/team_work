class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


stud = Student("Asan", 26)

print("Аты:", stud.name)
print("Жашы:", stud.age)

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand