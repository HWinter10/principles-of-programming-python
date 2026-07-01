"""
Hailey King-Winterton
CSC 500 - Principles of Programming
Portfolio Milestone - M4

Shopping Cart Initialization
    Input: name, price, quantity
    Output: item data, total monetary value

Pseudocode:
    START
        Create ItemToPurchase class
            Set item name, price, quantity
            Print item cost

        Main function
            Create empty cart list

            WHILE user has not entered 'quit'
                Prompt user: name
            
                if item name = 'quit'
                    stop adding items
        
                ELSE
                Prompt user: price, quantity
                Create item object
                Store name, price, quantiy in object
                Add item to cart list

            Set total cost to zero

            Display total cost heading

            FOR each item in cart list
                Print item cost
                Add item cost to total cost
            
            Display final total

        Run main function
    END
"""

# class for one item to be added to cart
class ItemToPurchase:

    # constructor
    def __intit__(self):
        self.item_name: str = "none"        # python type hints
        self.item_price: float = 0.0        # help clearly define
        self.item_quantity: int = 0         # data types

    #print one item's cost
    def print_item_cost(self):
        item_total = self.item_price * self.item_quantity
        print(
            self.item_name,
            self.item_quantity,
            "@ $" + format(self.item_price, ".1f"),
            "= $" + format(item_total, ".1f")
        )
# main program function
def main():

    #create empty cart list
    cart_items = []

    print("Enter item information")
    print("Enter 'quit' as the item name when finished.")

    # while user has not entered quit
    while True:

        # prompt user for item name
        print()
        item_name = input("Item name: ")

        # if item name is quit, stop adding items
        if item_name.lower() == "quit":
            break

        # prompt user foritem price and quantity
        item_price = float(input("Item price: "))
        item_quantity = int(input("Item quantity: "))

        # create item object
        item = ItemToPurchase()

        # store item name, price, quantity in object
        item.item_name = item_name
        item.item_price = item_price
        item.item_quantity = item_quantity

        # add item object to cart list
        cart_items.append(item)

    # set total cost to zero
    total_cost = 0.0

    # display total cost heading
    print()
    print("******************")
    print("TOTAL COST")

    # loops through each item in cart list
    for item in cart_items:

        # print item cost
        item.print_item_cost()

        # add item cost to total cost
        total_cost += item.item_price * item.item_quantity

    # display final total
    print("Total: $" + format(total_cost, ".1f"))

# run main function
if __name__ == "__main__":
    main()