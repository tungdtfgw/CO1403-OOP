products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse']
prices = [1000, 200, 50, 25]

def product_manager():
    while True:
        print_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_product()
        elif choice == 2:
            view_products()
        elif choice == 3:
            update_product()
        elif choice == 4:
            delete_product()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def print_menu():
    print('Product Manager')
    print('1. Add Product')
    print('2. View Products')
    print('3. Update Product')
    print('4. Delete Product')
    print('5. Exit')

def add_product():
    print('Add a Product')
    product = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    products.append(product)   # add product to the list
    prices.append(price)       # add price to the list

    print(f'Product {product} added successfully')

def view_products():
    n_products = len(products)          # get the number of products
    for i in range(n_products):
        product = products[i]           # get product at index i
        price = prices[i]               # get price at index i
        print(f'Product: {product}, Price: ${price}')   # print product and price to the screen

def update_product():
    product = input("Enter the product name to update: ")
    if product not in products:
        print(f'Product {product} not found.')
        return
    
    found_pos = products.index(product)   # find the index of the product
    new_price = float(input("Enter the new price: "))
    prices[found_pos] = new_price         # update the price at the found index

    print(f'Product {product} updated successfully')

def delete_product():
    product = input('Enter product name: ')
    if product not in products:
        print(f'Product {product} not found.')
        return
    
    found_pos = products.index(product)   # find the index of the product
    del products[found_pos]               # delete the product from the list
    del prices[found_pos]                 # delete the price from the list too

    print(f'Product {product} deleted successfully')

if __name__ == "__main__":
    product_manager()