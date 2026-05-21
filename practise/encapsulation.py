'''
What is Encapsulation?
binding the code and the data together.
A python class is an example of encapsulation
'''

class bankAccount:
    def __init__(self, account_holder, balance):
        self.accont_holder = account_holder
        self.__balance = balance # Double underscore at the start makes it a private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

# Create a account

account = bankAccount("Rajiv Bhalla", 1000)
account.deposit(500)
print(account.get_balance())
print(account.__balance)
