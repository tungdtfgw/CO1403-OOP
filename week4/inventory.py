from item import Item

class Inventory:
    def __init__(self):
        self.__items = []

    def add(self, item):
        # validate unique id
        for it in self.__items:
            if it.id == item.id:
                print(f"Item with id {item.id} already exists. Cannot add.")
                return
        
        self.__items.append(item)
        print(f"Item {item.name} added to inventory.")

    def __search(self, item_id):
        for it in self.__items:
            if it.id == item_id:
                return it
        return None

    def remove(self, item_id):
        item = self.__search(item_id)
        if item is None:
            print(f"Item with id {item_id} not found. Cannot remove.")
            return
        
        self.__items.remove(item)
        print(f"Item {item.name} removed from inventory.")

    def add_quantity(self, item_id, amount):
        # validate item exists
        item = self.__search(item_id)
        if item is None:
            print(f"Item with id {item_id} not found. Cannot add quantity.")
            return
        
        item.add(amount)
        print(f"Added {amount} to item {item.name}. New quantity: {item.quantity}")

    def decrease_quantity(self, item_id, amount):
        # validate item exists
        item = self.__search(item_id)
        if item is None:
            print(f"Item with id {item_id} not found. Cannot decrease quantity.")
            return
        
        item.decrease(amount)
        print(f"Decreased {amount} from item {item.name}. New quantity: {item.quantity}")

    def most_expensive(self):
        if len(self.__items) == 0:
            print("Inventory is empty.")
            return None
        
        expensive_item = self.__items[0]
        for it in self.__items:
            if it.price > expensive_item.price:
                expensive_item = it

        return expensive_item
    
    def storage(self):
        total_quantities = 0
        for it in self.__items:
            total_quantities += it.quantity

        return total_quantities
    
    def show_all(self):
        if len(self.__items) == 0:
            print("Inventory is empty.")
            return
        
        for it in self.__items:
            it.show()       # print(it)

if __name__ == "__main__":
    laptop = Item(1, "Laptop", 999.99, 10)
    phone = Item(2, "Phone", 499.99, 20)
    tablet = Item(3, "Tablet", 299.99, 15)

    inventory = Inventory()
    inventory.add(laptop)
    inventory.add(phone)
    inventory.add(tablet)

    inventory.show_all()

    print(f"Most expensive item: {inventory.most_expensive()}")
    print(f"Total quantities in storage: {inventory.storage()}")