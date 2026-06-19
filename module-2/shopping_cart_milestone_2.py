"""
Hailey King-Winterton
CSC 500 - Principles of Programming
Portfolio Milestone - M2

Shopping Cart Initialization
    Input: name, date, item, price, quantity
    Output: name, date, item data, total monetary value

Pseudocode:
    START
        Prompt user: name and date
        Prompt user: item name, description, price, quantity
            Prompt user: add another item?

        Calculate total price for each entry
        Calculate price for all items combined
        Calculate 6% sales tax
        Calculate cart subtotal

        Display customer info, item info, totals
    END
"""
# constant tax rate
TAX_RATE = 0.06

# prompting for input
customer_name = input("Enter customer name: ")
current_date = input("Date: ")

# creating lists for item data
item_names = []
item_descriptions = []
item_prices = []
item_quantities = []
item_totals = []

# while loop condition
add_another_item = "y"

# loop for adding items
while add_another_item.lower() == "y":
    print()
    print("-Enter item information-")

    # prompting for input
    item_name = input("Name: ")
    item_description = input("Description: ")
    item_price = float(input("Price: "))  # convert input to float
    item_quantity = int(input("Quantity: "))  # convert input to int

    # calculate one item's total
    item_total = item_price * item_quantity

    # adding data into lists
    item_names.append(item_name)
    item_descriptions.append(item_description)
    item_prices.append(item_price)
    item_quantities.append(item_quantity)
    item_totals.append(item_total)

    # prompt for adding more items
    add_another_item = input("Add another item? Enter y or n: ")

# calculate cart totals
cart_subtotal = sum(item_totals)
sales_tax = cart_subtotal * TAX_RATE
cart_total = cart_subtotal + sales_tax
total_items = sum(item_quantities)

# printing output
print()
print("Shopping Cart Summary")
print("-----------------------")
print("Customer:", customer_name)
print("Date:", current_date)

# loop through and print each line
for index in range(len(item_names)):
    print()
    print("Item", index + 1)
    print("Name:", item_names[index])
    print("Description:", item_descriptions[index])
    print("Price: $" + format(item_prices[index], ".2f"))
    print("Quantity:", item_quantities[index])
    print("Item total: $" + format(item_totals[index], ".2f"))

print()
print("***********************")
print("Total items:", total_items)
print("Cart subtotal: $" + format(cart_subtotal, ".2f"))
print("Sales tax: $" + format(sales_tax, ".2f"))
print("Cart total: $" + format(cart_total, ".2f"))
print("-----------------------")