'''
Hailey King-Winterton
CSC 500 - Principles of Programming
Critical thinking - M5

Bookstore points:
    Input: number of books purchases
    Output: points earned from books purchased

Pseudocode:
    START
    
    Set valuds_input to false

    While valid_input is false
        prompt user for number of books purchased this month

        if user numner 0 or greater
            set valid_input to true

            otherwise
                display error message

    If number of books is 8 or more
        Award 60 points
    Otherwise, if 6 or more
        Award 30 points
    Otherwise, if 4 or more
        Award 15 points
    Otherwise, if 2 or more
        Award 5 points
    Otherwise
        Award 0 points
    If the number of books is valid
        Display total points awarded
        
    END
'''

# continue asking for number of books until user enters a valid input
while True:
    try:
        books_purchased = int(
            input("How many books did you purchasew this month? ")
        )
        
        if books_purchased >=0:
            break

        print("The number of books purchased must be a whole positive number.")
    except ValueError:
        print("Please enter a whole positive number.")

# Block for determining reward points earned
if books_purchased >=8:
    points_awarded = 60
elif books_purchased >= 6:
    points_awarded = 30
elif books_purchased >= 4:
    points_awarded = 15
elif books_purchased >= 2:
    points_awarded = 5
else:
    points_awarded = 0

# Display the points only when the input is valid.
if books_purchased >= 0:
    print(f"You earned {points_awarded} points this month!")