#encapsulation in python
class BankAccount:
    def __init__(self, balance=100):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance is {self.__balance}.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")

    def get_balance(self):
        return self.__balance
# Example usage:
account = BankAccount()
account.deposit(50)  # Deposited 50. New balance is 150.
account.withdraw(30)  # Withdrew 30. New balance is 120.
print(f"Current balance is {account.get_balance()}.")  # Current balance is 120.
account.withdraw(200)  # Insufficient balance.
account.__balance = 1000  # Attempt to modify private attribute (will not affect actual balance)
print(f"Current balance is {account.get_balance()}.")  # Current balance is