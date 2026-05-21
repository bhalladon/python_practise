class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("The name is", self.name, "and age is", self.age)

s1 = Student("rajiv", 20)
s1.display()

class Average:

    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def get_average(self):
        total_marks = 0
        for i in range(len(self.marks)):
            total_marks += self.marks[i]
        average = total_marks / len(self.marks)
        return average

    def display(self):
        print("The average of", self.name, "'s marks is", self.get_average())

s1 = Average("Rajiv", [90, 95, 98, 97, 99])
s1.display()

