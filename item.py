# Program to experiment with classes in Python
# Contains an "Item" class for listing items
# for sale.
# Peter Menchu 2023
class Item(object):
    # constructor
    def __init__(self, name, descr, price, quantity):
        self.name = name
        self.descr = descr
        self.price = price
        self.quantity = int(quantity)

    def sell(self, number):
        if (self.quantity - int(number)) >= 0:
            self.quantity -= int(number)
            print(number, " sold of ", self.name + ".")
            print(self.quantity, "remain.")
        else:
            print("Not enough of ", self.name, " remaining.")


name = input("Enter item name: ")
descr = input("Enter item description: ")
price = input("Enter price: ")
quantity = input("Quantity available: ")

newItem = Item(name, descr, price, quantity)

print(newItem.name, newItem.descr, newItem.price, quantity)

number = input("Enter the amount of " + name + " to sell: ")

newItem.sell(number)

# Peter Menchu 2023
