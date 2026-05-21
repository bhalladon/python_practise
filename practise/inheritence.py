'''
What is inheritence?
In inheritence we have a base class also known as Parent class
and a derived class also known as Child class.
The child class inherits the properties of the parent class.
So if parent class has a property name, and a method called display(),
then the child class will inherit these properties and methods.

We can override the methods of parent class in child class.
This is call method overloading.
'''

# Example of Inheritence

class Animal:
    def __init__(self, animal_type, age):
        self.animal_type = animal_type
        self._age = age # Single underscore at the start makes it a protected attribute.

    def get_type(self):
        return self.animal_type

    def get_age(self):
        return self._age

class Dog(Animal):
    def __init__(self, animal_type, age, breed):
        # self.animal_type = animal_type
        # self._age = age  # Single underscore at the start makes it a protected attribute.
        super().__init__(animal_type, age) # Super() calls the parent class constructor.
        self.breed = breed

    def wagTail(self):
        print("Dog wagging tail!")

animal_one = Dog('Dog', 5, "bulldog")
animal_one.wagTail()
print(animal_one.breed)
