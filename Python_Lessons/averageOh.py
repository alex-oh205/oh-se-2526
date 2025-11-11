# Alex Oh
# 11/11/25
# Test Score Average Calculator
# This program calculates the average of a specified amount of test scores inputted by the user.

n = int(input("Enter the number of test scores to average: "))  # Get number of scores
total = 0                                                       # Initialize total to 0
for i in range(n):                                              # Loop n times
    num = float(input(f"Enter test score {i + 1}: "))           # Get each score from user
    total += num                                                # Add score to total
average = total / n                                             # Calculate average
print(f"The average is: {average:.0f}")                         # Display average rounded to nearest integer