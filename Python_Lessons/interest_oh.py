# Name:  Alex Oh
# Program:  interest_oh.py
# Compute and display an investment report for compound interest

def main():
    # Gather inputs
    startBalance = float(input("Enter the investment amount: "))  # float
    years = int(input("Enter the number of years: ")) # int
    rate = int(input("Enter the interest rate as a %: ")) # int

    # Convert the percent rate to a decimal
    rate = rate / 100

    # Initialize interest accumulator
    totalInterest = 0.0

    # Display the header for the table 
    print("{0:>4}{1:>18}{2:>10}{3:>16}".format("Year", "Starting Balance", "Interest", "Ending Balance"))

    # Compute and display the results for each year
    for year in range(1, years+1):
        interest = startBalance * rate  # Calculate interest
        endBalance = startBalance + interest  # Calculate endBalance
        print(f"{year:>4.2f}{startBalance:>18.2f}{interest:>10.2f}{endBalance:>16.2f}")  # print formatted results for each year 
        startBalance = endBalance  # Update startBalance for the next year
        totalInterest += interest  # Update totalInterest

    # Display Ending Balance
    print(f"\nEnding Balance: ${endBalance:.2f}")

    # Display Total Interest Earned
    print(f"Total interest earned: ${totalInterest:.2f}")

main()