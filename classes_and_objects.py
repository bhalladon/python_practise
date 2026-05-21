class Sector46c:
    def __init__(self):
        self.house_number = int(input("Enter your house number: "))
        self.name = input("Enter your name: ")

    def put_data(self):
        print("The house number ", self.house_number, "is occupied by ", self.name)

# a = Sector46c()
# a.put_data()

class Sector47c:
    def __init__(self, house_number, name):
        self.house_number = house_number
        self.name = name

    def put_data(self):
        print("The house number ", self.house_number, "is occupied by ", self.name)

b = Sector47c(name="Rajiv Bhalla", house_number=3197).put_data()