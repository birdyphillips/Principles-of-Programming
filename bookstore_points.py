"""
The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. 
The points are awarded as follows:

If a customer purchases 0 books, they earn 0 points.
If a customer purchases 2 books, they earn 5 points.
If a customer purchases 4 books, they earn 15 points.
If a customer purchases 6 books, they earn 30 points.
If a customer purchases 8 or more books, they earn 60 points.
Write a program that asks the user to enter the number of books that they have purchased this month and then displays the number of points awarded.
"""

print("Welcome to the CSU Global Bookstore Points Calculator!")
while True:
    user_input = input("Enter the number of books purchased this month (or type 'exit' to quit): ").strip().lower()
    if user_input == "exit":
        print("Thank you for using the Bookstore Points Calculator. Goodbye!")
        break
    try:
        number_of_books = int(user_input)
    except ValueError:
        print("Error. Please enter a valid number or type 'exit' to quit.")
        continue
    message = ""
    if number_of_books < 0:
        message = "Error. Enter a positive number.\nRe-run program and try again."
    else:
        message = "You are awarded "
        if number_of_books <= 1:
            message += "0 "
        elif number_of_books <= 3:
            message += "5 "
        elif number_of_books <= 5:
            message += "15 "
        elif number_of_books <= 7:
            message += "30 "
        else:
            message += "60 "
        message += "points."
    print(message)
