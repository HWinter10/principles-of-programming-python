"""
Hailey King-Winterton
CSC 500 - Principles of Programming
Portfolio Milestone - M6

Online Shopping Cart - Part 2
    Input: customer name, date, item name, description, price, quantity
    Output: cart menu, item descriptions, item totals, cart total

Pseudocode:
    START
        Create ItemToPurchase class
            Set item name, description, price, and quantity
            Print item cost

        Create ShoppingCart class
            Set customer name, current date, and cart items list
            Create methods for:
                Add item to cart
                Remove item from cart
                Modify item quantity
                Get number of items in cart
                Get cost of cart
                Print total
                Print item descriptions

        Create print menu logic
            Display menu options

            WHILE user has not entered 'q'
                Prompt user: menu option

                IF option = 'a'
                    Prompt user: item name, description, price, quantity
                    Create item object
                    Add item to cart

                ELSE IF option = 'r'
                    Prompt user: item name
                    Remove item from cart

                ELSE IF option = 'c'
                    Prompt user: item name and new quantity
                    Modify item quantity

                ELSE IF option = 'i'
                    Display item descriptions

                ELSE IF option = 'o'
                    Display shopping cart

                ELSE IF option = 'q'
                    Quit menu

                ELSE
                    Prompt user for valid option

        Main function
            Prompt user: customer name and date
            Create shopping cart object
            Run print menu function

        Run main function
    END
"""

# output formatting 
DIVIDER = "-----------------------" 
STAR_LINE = "***********************"

# class: adds one item to cart
class ItemToPurchase:

    # constructor
    def __init__(self):
        self.item_name: str = "none"
        self.item_description: str = "none"
        self.item_price: float = 0.0
        self.item_quantity: int = 0

    # print one item's cost
    def print_item_cost(self):
        item_total = self.item_price * self.item_quantity
        print(
            self.item_name,
            self.item_quantity,
            "@ $" + format(self.item_price, ".1f"),
            "= $" + format(item_total, ".1f")
        )


# class: manages shopping cart
class ShoppingCart:

    # constructor
    def __init__(self):
        self.customer_name: str = "none"
        self.current_date: str = "January 1, 2020"
        self.cart_items: list = []

    # class method: adds item to cart
    def add_item(self, item_to_add):
        self.cart_items.append(item_to_add)

    # class method: removes item from cart by name
    def remove_item(self, item_name):
        item_found = False

        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break

        if not item_found:
            print("Item not found in cart. Nothing removed.")

    # class method: modifies item quantity
    def modify_item(self, item_to_modify):
        item_found = False

        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                item.item_quantity = item_to_modify.item_quantity
                item_found = True
                break

        if not item_found:
            print("Item not found in cart. Nothing modified.")

    # class method: gets total number of items in cart
    def get_num_items_in_cart(self):
        total_items = 0

        for item in self.cart_items:
            total_items += item.item_quantity

        return total_items

    # class method: gets total cost of cart
    def get_cost_of_cart(self):
        total_cost = 0.0

        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity

        return total_cost

    # class method: prints shopping cart total
    def print_total(self):
        print()
        print(STAR_LINE)
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print(DIVIDER)
        print("Number of Items:", self.get_num_items_in_cart())
        print()

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print()
        print(DIVIDER)
        print("Total: $" + format(self.get_cost_of_cart(), ".1f"))
        print(STAR_LINE)

    # class method: prints item descriptions
    def print_descriptions(self):
        print()
        print(STAR_LINE)
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print(DIVIDER)
        print("Item Descriptions")
        print()

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(item.item_name + ": " + item.item_description)

        print(STAR_LINE)


# menu function
def print_menu(shopping_cart):

    menu_option = ""

    # loop: until user chooses q
    while menu_option != "q":
        print()
        print(STAR_LINE)
        print("MENU")
        print(DIVIDER)
        print("a - Add item")
        print("r - Remove item")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print(STAR_LINE)
        print()

        menu_option = input("Choose an option: ").lower()

        # loop: handles invalid menu input
        while menu_option not in ["a", "r", "c", "i", "o", "q"]:
            print("Invalid option.")
            menu_option = input("Choose an option: ").lower()

        # add item
        if menu_option == "a":
            print()
            print(DIVIDER)
            print("ADD ITEM TO CART")
            print(DIVIDER)

            item = ItemToPurchase()

            item.item_name = input("Item name: ")
            item.item_description = input("Item description: ")
            item.item_price = float(input("Item price: "))
            item.item_quantity = int(input("Item quantity: "))

            shopping_cart.add_item(item)

        # remove item
        elif menu_option == "r":
            print()
            print(DIVIDER)
            print("REMOVE ITEM FROM CART")
            print(DIVIDER)

            item_name = input("Enter name of item to remove: ")
            shopping_cart.remove_item(item_name)

        # change item quantity
        elif menu_option == "c":
            print()
            print(DIVIDER)
            print("CHANGE ITEM QUANTITY")
            print(DIVIDER)

            item = ItemToPurchase()

            item.item_name = input("Item name: ")
            item.item_quantity = int(input("New quantity: "))

            shopping_cart.modify_item(item)

        # output descriptions
        elif menu_option == "i":
            print()
            print("OUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()

        # output shopping cart
        elif menu_option == "o":
            print()
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()


# main program function
def main():

    # prompt for info
    customer_name = input("Customer name: ")
    current_date = input("Today's date: ")

    # create shopping cart object
    shopping_cart = ShoppingCart()

    # store customer info in shopping cart
    shopping_cart.customer_name = customer_name
    shopping_cart.current_date = current_date

    # run menu
    print_menu(shopping_cart)


# run main function
if __name__ == "__main__":
    main()