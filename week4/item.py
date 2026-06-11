class Item:
    def __init__(self, id, name, price, quantity):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @property
    def quantity(self):
        return self.__quantity
    
    @name.setter
    def name(self, value):
        if value == '':
            print("Name cannot be empty.")
        else:
            self.__name = value

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Price must be a positive number.")
        else:
            self.__price = value
        
    def add(self, amount):
        if amount <= 0:
            print("Amount to add must be a positive number.")
        else:
            self.__quantity += amount

    def decrease(self, amount):
        if amount <= 0:
            print("Amount to decrease must be a positive number.")
        elif amount > self.__quantity:
            print("Cannot decrease more than the current quantity.")
        else:
            self.__quantity -= amount

    def show(self):
        print(f'{self.__id} {self.__name}: ${self.__price:.2f}, Quantity: {self.__quantity}')

    def __str__(self):
        return f'{self.__id} {self.__name}: ${self.__price:.2f}, Quantity: {self.__quantity}'

if __name__ == "__main__":
    item1 = Item(1, "Laptop", 999.99, 10)
    item1.show()

    item1.name = "Gaming Laptop"
    item1.price = 1299.99
    item1.add(5)
    item1.decrease(3)
    item1.show()

    print(item1) # => print(item1.__str__())