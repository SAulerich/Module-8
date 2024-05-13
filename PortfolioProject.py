input('Welcome to the Portfolio Milestone, please press the "Enter" key to move forward to the first second: The First Portfolio Milestone (Steps 1-3)')

print("\nOnline Shopping Cart\n")

class ItemToPurchase:
    def __init__(self):
        self.item_Name = "none"
        self.item_Price = 0.00
        self.item_Quantity = 0
    def print_Item_Cost(self):
        print(f"{self.item_Name} {self.item_Quantity} @ ${self.item_Price} = ${self.item_Price * self.item_Quantity}")
if __name__ == "__main__":
    print("Item 1")
    name = input("Enter the item name: ")
    price = int(input("Enter the item price: $"))
    quantity = int(input("Enter the item quantity: "))
    item1 = ItemToPurchase()
    item1.item_Name = name
    item1.item_Price = price
    item1.item_Quantity = quantity
    print("\nItem 2")
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: $"))
    quantity = int(input("Enter the item quantity: "))
    item2 = ItemToPurchase()
    item2.item_Name = name
    item2.item_Price = price
    item2.item_Quantity = quantity
    print("\nTOTAL COST")
    item1.print_Item_Cost()
    item2.print_Item_Cost()
    total = item1.item_Price * item1.item_Quantity + item2.item_Price * item2.item_Quantity
    print(f"Total: ${total:.2f}")

input(f"\n\nThe First Portfolio Milestone is now complete, please press the 'Enter' key to move to the next section: The Second Portfolio Milestone (Steps 4-6).")

import datetime

class ItemToPurchase:
    def __init__(self, name = "none", price = 0, quantity = 0, description = "none"):
        self.item_Name = name
        self.item_Price = price
        self.item_Quantity = quantity
        self.item_Description = description
class Cart:
    def __init__(self, customer_Name = "none"):
        self.customer_Name = customer_Name
        self.current_Date = datetime.datetime.now().strftime("%B %d, %Y")
        self.cart_Items = []
    def add_Item(self, item):
        self.cart_Items.append(item)
        print(f"{item.item_Name} has been added to your cart")
    def remove_Item(self, item_Name):
        for item in self.cart_Items:
            if item.item_Name == item_Name:
                self.cart_Items.remove(item)
                print(f"{item_Name} has been removed from your cart")
                return
        print("Item can not be found in your cart, so nothing has been removed")
    def modify_Item(self, item_Name, new_Quantity):
        for item in self.cart_Items:
            if item.item_Name == item_Name:
                item.item_Quantity = new_Quantity
                print(f"Update: {item_Name} now has {new_Quantity} in your cart")
                return
        print("This item was not found in your cart, so nothing has been modified")
    def get_Num_Items_In_Cart(self):
        return sum(item.item_Quantity for item in self.cart_Items)
    def get_Cost_Of_Cart(self):
        return sum(item.item_Price * item.item_Quantity for item in self.cart_Items)
    def print_Total(self):
        if not self.cart_Items:
            print("Your Shopping cart is now empty")
            return
        print(f"{self.customer_Name}'s Shopping Cart ({self.current_Date})")
        print("Number of Items:", self.get_Num_Items_In_Cart())
        for item in self.cart_Items:
            print(f"{item.item_Quantity} of the {item.item_Name} for ${item.item_Price} each = ${item.item_Quantity * item.item_Price}")
        print("Total: $", self.get_Cost_Of_Cart())
    def print_Descriptions(self):
        if not self.cart_Items:
            print("Your shopping cart is now empty")
            return
        print(f"{self.customer_Name}'s Shopping Cart ({self.current_Date})")
        print("Item Descriptions:")
        for item in self.cart_Items:
            print(f"{item.item_Name}: {item.item_Description}")
def print_Menu(shopping_Cart):
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
def main():
    customer_Name = input("Enter your name: ")
    shopping_Cart = Cart(customer_Name)
    print_Menu(shopping_Cart)
    while True:
        choice = input("\nPlease, choose an option: ")
        if choice == "a":
            item_Name = input("Item name: ")
            item_Description = input("Item description: ")
            item_Price = float(input("Item price: $"))
            item_Quantity = int(input("Item quantity: "))
            item = ItemToPurchase(item_Name, item_Price, item_Quantity, item_Description)
            shopping_Cart.add_Item(item)
        elif choice == "r":
            item_Name = input("Enter the name of the item to remove: ")
            shopping_Cart.remove_Item(item_Name)
        elif choice == "c":
            item_Name = input("Enter the name of the item to modify: ")
            new_Quantity = int(input("Enter the new quantity of the item to modify: "))
            shopping_Cart.modify_Item(item_Name, new_Quantity)
        elif choice == "i":
            shopping_Cart.print_Descriptions()
        elif choice == "o":
            shopping_Cart.print_Total()
        elif choice == "q":
            print("Program Completed")
            break
        else:
            print("Invalid choice. Please, choose another.")
if __name__ == "__main__":
    main()

input(f"\n\nThe Second Portfolio Milestone is now complete, please press the 'Enter' key to move to the last section: Additional Tasks for the Final Project Submission (Steps 7-10).\n\n")

class ItemToPurchase:
    def __init__(self, item_Name = "none", item_Price = 0, item_Quantity = 0,  description = "none"):
        self.item_Name = item_Name
        self.item_Price = item_Price
        self.item_Quantity = item_Quantity
        self.item_Description = description
    def print_Item_Cost(self):
        print(f"{self.item_Name} {self.item_Quantity} @ ${self.item_Price} = ${self.item_Quantity * self.item_Price}")
class ShoppingCart:
    def __init__(self, customer_Name="none", current_Date="January 1, 2020"):
        self.customer_Name = customer_Name
        self.current_Date = current_Date
        self.cart_Items = []
    def add_Item(self, item):
        self.cart_Items.append(item)
    def remove_Item(self, item_Name):
        found = False
        for item in self.cart_Items:
            if item.item_Name == item_Name:
                self.cart_Items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")
    def modify_Item(self, item_Name, new_Name=None, new_Price=None, new_Quantity=None, new_Description=None):
        found = False
        for item in self.cart_Items:
            if item.item_Name == item_Name:
                found = True
                if new_Name:
                    item.item_Name = new_Name
                if new_Price is not None:
                    item.item_Price = new_Price
                if new_Quantity is not None:
                    item.item_Quantity = new_Quantity
                if new_Description:
                    item.item_Description = new_Description
                print(f"Updated item '{item_Name}' details in your cart.")
                break
        if not found:
            print("Item not found in cart. Nothing modified.")
    def get_Num_Items_In_Cart(self):
        return sum(item.item_Quantity for item in self.cart_Items)
    def get_Cost_Of_Cart(self):
        return sum(item.item_Quantity * item.item_Price for item in self.cart_Items)
    def print_Total(self):
        total_Cost = self.get_Cost_Of_Cart()
        if len(self.cart_Items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_Name}'s Shopping Cart - {self.current_Date}")
        print("Number of Items:", self.get_Num_Items_In_Cart())
        for item in self.cart_Items:
            item.print_Item_Cost()
        print("Total: $" + str(total_Cost))
    def print_Descriptions(self):
        if len(self.cart_Items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_Name}'s Shopping Cart - {self.current_Date}")
        print("Item Descriptions:")
        for item in self.cart_Items:
            print(f"{item.item_Name}: {item.item_Description}")
def print_Menu(cart):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    while True:
        option = input("\nChoose an option: ")
        if option == 'q':
            break
        elif option == 'a':
            add_Item_To_Cart(cart)
        elif option == 'r':
            remove_Item_From_Cart(cart)
        elif option == 'c':
            modify_Item_In_Cart(cart)
        elif option == 'i':
            cart.print_Descriptions()
        elif option == 'o':
            cart.print_Total()
        else:
            print("Invalid option. Please choose again.")
def add_Item_To_Cart(cart):
    item_Name = input("Enter the item name: ")
    item_Price = float(input("Enter the item price: $"))
    item_Quantity = int(input("Enter the item quantity: "))
    item_Description = input("Enter the item description: ")
    item = ItemToPurchase(item_Name, item_Price, item_Quantity, item_Description)
    cart.add_Item(item)
    print(f"{item_Name} added to cart.")
def remove_Item_From_Cart(cart):
    item_Name = input("Enter the item name to remove: ")
    cart.remove_Item(item_Name)
def modify_Item_In_Cart(cart):
    item_Name = input("Enter the item name to modify: ")
    new_Name = input("Enter the new item name (or leave blank to keep current): ").strip()
    new_Name = new_Name if new_Name else None
    new_Price = input("Enter the new item price (or leave blank to keep current): $")
    new_Price = None if new_Price.strip() == "" else float(new_Price)
    new_Quantity = input("Enter the new item quantity (or leave blank to keep current): ")
    new_Quantity = None if new_Quantity.strip() == "" else int(new_Quantity)
    new_Description = input("Enter the new item description (or leave blank to keep current): ").strip()
    new_Description = new_Description if new_Description else None
    cart.modify_Item(item_Name, new_Name, new_Price, new_Quantity, new_Description)
def main():
    customer_Name = input("Enter customer's name: ")
    current_Date = input("Enter today's date: ")
    print(f"\nCustomer name: {customer_Name}\nToday's date: {current_Date}\n")
    cart = ShoppingCart(customer_Name, current_Date)
    print_Menu(cart)
if __name__ == "__main__":
    main()
    
input('\nCongradulations! All Milestones for the Portfolio Project are now complete. Please press the "Enter" key to terminate the program.')