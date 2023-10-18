class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        return self.price * self.quantity

    def add_items(self, quantity):
        if quantity > 0:
            self.quantity += quantity

    def remove_items(self, quantity):
        if 0 < quantity <= self.quantity:
            self.quantity -= quantity
        else:
            return "Invalid quantity or insufficient stock"

# Example usage of all three classes:
account = BankAccount("12345", 1000)
print(account.deposit(500))  # Deposited $500. New balance: $1500
print(account.withdraw(200))  # Withdrew $200. New balance: $1300

car = Car("Toyota", "Camry", 2022)
print(car.get_make())  # Toyota
car.set_model("Corolla")
print(car.get_model())  # Corolla

product = Product("Widget", 10.99, 50)
print(product.calculate_total_value())  # 549.5
product.add_items(20)
print(product.calculate_total_value())  # 769.5
product.remove_items(10)
print(product.calculate_total_value())  # 669.5
