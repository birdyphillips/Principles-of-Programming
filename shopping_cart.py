import sys

class ItemToPurchase:
    # Constructor with default values for name, price, and quantity
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Method to print the cost of the item in the required format
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total)}")

def print_shopping_cart(cart):
    print("\nCurrent Shopping Cart:")
    for item in cart:
        item.print_item_cost()
    total_cost = sum(item.item_price * item.item_quantity for item in cart)
    print(f"Cart Total: ${int(total_cost)}\n")

if __name__ == "__main__":
    print("Welcome to BirdyPhillips Store!")
    print("Thank you for shopping with us!\n")
    while True:
        shopping_cart = []

        # Prompt user for first item's details
        print("\nItem 1")
        name1 = input("Enter the item name:\n")
        price1 = float(input("Enter the item price:\n"))
        quantity1 = int(input("Enter the item quantity:\n"))
        item1 = ItemToPurchase(name1, price1, quantity1)
        shopping_cart.append(item1)
        print_shopping_cart(shopping_cart)  # Print cart after first item

        # Prompt user for second item's details
        print("\nItem 2")
        name2 = input("Enter the item name:\n")
        price2 = float(input("Enter the item price:\n"))
        quantity2 = int(input("Enter the item quantity:\n"))
        item2 = ItemToPurchase(name2, price2, quantity2)
        shopping_cart.append(item2)
        print_shopping_cart(shopping_cart)  # Print cart after second item

        # Print the total cost for both items
        print("\nTOTAL COST")
        for item in shopping_cart:
            item.print_item_cost()
        total_cost = sum(item.item_price * item.item_quantity for item in shopping_cart)
        print(f"\nTotal: ${int(total_cost)}")

        # Ask user if they want to exit or continue
        exit_choice = input("\nType 'exit' to quit or press Enter to add more items: ")
        if exit_choice.lower() == "exit":
            print("Thank you for using the Birdy Phillips Store Shopping Cart Program!")
