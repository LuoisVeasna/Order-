from collections import Counter

# Price dictionary
prices = {"Soap": 50, "Toothpaste": 25, "Shampoo": 45.50, "Toothbrush": 15.99}

# Function to generate bill
def generate_bill(cart):
    total = 0
    for item, qty in cart.items():
        if item in prices:
            cost = prices[item] * qty
            print(f"{item:10} {prices[item]:5} x {qty:2} = {cost:.2f}")
            total += cost
        else:
            print(f"Error: {item} not found in price list")
    print(f"\nTotal Amount: {total:.2f}")

# Shopping cart
Cart = {"Soap": 5, "Toothpaste": 1, "Shampoo": 2, "Toothbrush": 3}

# Call the function with the correct variable name
generate_bill(Cart)

