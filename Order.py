# Sample product data
products = [
    {"name": "Laptop", "price": 999.99, "rating": 4.5},
    {"name": "Smartphone", "price": 599.99, "rating": 4.2},
    {"name": "Tablet", "price": 399.99, "rating": 4.7},
    {"name": "Headphones", "price": 199.99, "rating": 4.8},
    {"name": "Smartwatch", "price": 249.99, "rating": 4.3}
]

# Function to order products by a specific attribute
def order_products(products, by="price", reverse=False):
    return sorted(products, key=lambda x: x[by], reverse=reverse)

# Display the menu to the user
def display_menu():
    print("Welcome to the Product Ordering App!")
    print("1. Order by Price (Ascending)")
    print("2. Order by Price (Descending)")
    print("3. Order by Rating (Ascending)")
    print("4. Order by Rating (Descending)")
    print("5. Order by Name (Alphabetically)")
    print("0. Exit")
    choice = input("Enter your choice (0-5): ")
    return choice

# Function to print the ordered list of products
def print_products(ordered_products):
    print("\nOrdered Products:")
    for product in ordered_products:
        print(f"{product['name']} - ${product['price']} - Rating: {product['rating']}")

# Main App Loop
def run_app():
    while True:
        choice = display_menu()

        if choice == '1':
            ordered_products = order_products(products, by="price", reverse=False)
            print_products(ordered_products)
        elif choice == '2':
            ordered_products = order_products(products, by="price", reverse=True)
            print_products(ordered_products)
        elif choice == '3':
            ordered_products = order_products(products, by="rating", reverse=False)
            print_products(ordered_products)
        elif choice == '4':
            ordered_products = order_products(products, by="rating", reverse=True)
            print_products(ordered_products)
        elif choice == '5':
            ordered_products = order_products(products, by="name", reverse=False)
            print_products(ordered_products)
        elif choice == '0':
            print("Exiting the app. Thank you!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the app
if __name__ == "__main__":
    run_app()
