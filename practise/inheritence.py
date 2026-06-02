# '''
# What is inheritence?
# In inheritence we have a base class also known as Parent class
# and a derived class also known as Child class.
# The child class inherits the properties of the parent class.
# So if parent class has a property name, and a method called display(),
# then the child class will inherit these properties and methods.
#
# We can override the methods of parent class in child class.
# This is call method overloading.
# '''
#
# # Example of Inheritence
#
# class Animal:
#     def __init__(self, animal_type, age):
#         self.animal_type = animal_type
#         self._age = age # Single underscore at the start makes it a protected attribute.
#
#     def get_type(self):
#         return self.animal_type
#
#     def get_age(self):
#         return self._age
#
# class Dog(Animal):
#     def __init__(self, animal_type, age, breed):
#         # self.animal_type = animal_type
#         # self._age = age  # Single underscore at the start makes it a protected attribute.
#         super().__init__(animal_type, age) # Super() calls the parent class constructor.
#         self.breed = breed
#
#     def wagTail(self):
#         print("Dog wagging tail!")
#
# animal_one = Dog('Dog', 5, "bulldog")
# animal_one.wagTail()
# print(animal_one.breed)

class Animal:
    def __init__(self, animal_name, age):
        self.animal_name = animal_name
        self.age = age

    def get_animal_name(self):
        print("Animal name is", self.animal_name)
        return self.animal_name

    def get_age(self):
        return self.age


class Dog(Animal):
    def __init__(self, animal_name, age, breed):
        super().__init__(animal_name, age)
        self.__breed = breed

    def wagTail(self):
        print(
            self.__breed)  # Double underscore at the start makes it a private attribute and cannot be accessed outside the class.
        # Only class objects can access private attributes.
        # like in this function we are printing it.
        # so whenever we call this function we should be able to access the private attribute "breed"

        print("Dog wagging Tail!")


animal_one = Dog(animal_name="Dog", age=12, breed="pamerian")
animal_one.wagTail()
f = animal_one.breed  # (This will not work because breed is a private attribute and here we are trying to access it outside the class
