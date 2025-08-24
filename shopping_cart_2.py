# --- Shopping Cart Classes ---
# --- ItemToPurchase class: Represents an item in the shopping cart ---
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# --- ShoppingCart class: Manages the shopping cart and its operations ---
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
    # Adds an item to the cart
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # Removes an item by name from the cart and prints what was removed
        for i, item in enumerate(self.cart_items):
            if item.name == item_name:
                removed_item = self.cart_items.pop(i)
                print(f"Removed: {removed_item.name}")
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
    # Modifies an item's description, price, and/or quantity
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                if item.description != "none":
                    cart_item.description = item.description
                if item.price != 0:
                    cart_item.price = item.price
                if item.quantity != 0:
                    cart_item.quantity = item.quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
    # Returns the total quantity of all items in the cart
        return sum(item.quantity for item in self.cart_items)

    def get_cost_of_cart(self):
    # Returns the total cost of all items in the cart
        return sum(item.price * item.quantity for item in self.cart_items)

    def print_total(self):
    # Prints the shopping cart's total cost and item details
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(f"{item.name} {item.quantity} @ ${item.price} = ${item.price * item.quantity}")
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
    # Prints the descriptions of all items in the cart
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

# --- Menu Function ---
# --- print_menu function: Displays and processes the shopping cart menu ---
def print_menu(cart):
    menu = (
        "MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit"
    )
    while True:
        print("\n" + "*"*45)
        print("BirdyPhillips is dedicated to giving great customer service!")
        print("What would you like to buy today? Your cart, your choices!")
        print("*"*45 + "\n")
        print("\n" + "="*40)
        print(menu)
        print("="*40)
        choice = input("Choose an option: ").strip().lower()
        if choice == 'a':
            # Add item to cart
            print("ADD ITEM TO CART")
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            cart.add_item(ItemToPurchase(name, description, price, quantity))
        elif choice == 'r':
            # Remove item from cart
            print("REMOVE ITEM FROM CART")
            if not cart.cart_items:
                print("Cart is empty.")
            else:
                print("Items in cart:")
                for item in cart.cart_items:
                    print(f"- {item.name}")
                name = input("Enter name of item to remove: ")
                cart.remove_item(name)
        elif choice == 'c':
            # Change item quantity
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))
            cart.modify_item(ItemToPurchase(name, quantity=quantity))
        elif choice == 'i':
            # Output items' descriptions
            print("\nITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            # Output shopping cart
            print("Heres whats in your cart:")
            cart.print_total()
        elif choice == 'q':
            # Quit the menu
            break
        else:
            # Invalid option
            print("Invalid option, please try again.")

def main():
    print("\n" + "*"*45)
    print("Welcome to BirdyPhillips Store!")
    print("Where Shopping is a Breeze and Savings are Guaranteed!")
    print("*"*45 + "\n")
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print(f"Customer name: {cart.customer_name}")
    print(f"Today's date: {cart.current_date}")
    print_menu(cart)

if __name__ == "__main__":
    main()
