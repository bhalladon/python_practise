class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee name is: {self.name}"

    def __call__(self, salary):
        return f"Employee salary is: {salary} and employee name is: {self.name}"

print(Employee("rajiv")(500))


class Salary(Employee):
    def __init__(self, salary, name):
        self.salary = salary
        super().__init__(name)

    def __str__(self):
        return f"Salary is: {self.salary} of employee {self.name}"


print(Salary(50000, "Raj"))


# Example with __call__
class Multiplier:

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor


print(Multiplier(5)(3))

# Examples of other dunder functions/methods like __repr__, __add__, __len__
