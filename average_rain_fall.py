"""
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for the number of years.
The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
"""
def average_rainfall():
    print("\nWelcome to the Average Rainfall Calculator!")
    while True:
        years_input = input('Please enter the number of years (or type "exit" to quit): ')
        if years_input.strip().lower() == "exit":
            print("\nThank you for using the Average Rainfall Calculator. Goodbye!")
            exit()
        try:
            years = int(years_input)
            if years < 1:
                print("  Please enter a positive number of years.")
                continue
            break
        except ValueError:
            print("  Invalid input. Please enter a valid number.")
    month_rainfall = 0
    for i in range(1, years + 1):
        print(f"\nYear {i}:")
        for m in range(1, 13):
            while True:
                rainfall_input = input(f'  Enter the inches of rainfall for month {m} (or type "exit" to quit): ')
                if rainfall_input.strip().lower() == "exit":
                    print("\nThank you for using the Average Rainfall Calculator. Goodbye!")
                    exit()
                try:
                    rainfall_inch = float(rainfall_input)
                    if rainfall_inch < 0:
                        print("    Please enter a non-negative value.")
                        continue
                    break
                except ValueError:
                    print("    Invalid input. Please enter a valid number.")
            month_rainfall += rainfall_inch
    months = years * 12
    print('\nSummary:')
    print('  The number of months is', months)
    print('  The total inches of rainfall is', month_rainfall)
    print('  The average rainfall per month for the entire period is', format(month_rainfall / months, '.2f'))

while True:
    print("\nHello! This program calculates the average rainfall over a period of years.")
    average_rainfall()
    again = input("\nWould you like to calculate again? (yes to continue, type 'exit' to quit): ").strip().lower()
    if again == "exit":
        print("\nThank you for using the Average Rainfall Calculator. Goodbye!")
        break
    if again != "yes":
        print("\nThank you for using the Average Rainfall Calculator. Goodbye!")
        break

