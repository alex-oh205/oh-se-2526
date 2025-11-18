"""
Name: Alex Oh
Date: 11/18/25

File: oh_stats.py

Purpose: This program calculates the mean and standard deviation of a list of numbers provided by the user.
"""

def getInputs(): # Gets the list of numbers from the user
    numbers = input("Enter a list of numbers separated by spaces: ")
    return [float(n) for n in numbers.split()] # Convert input string to list of floats

def xBar(values): # Calculates the mean of the list of numbers
    mean = sum(values) / len(values) # Divide sum by count
    return mean

def stdDev(values): # Calculates the standard deviation of the list of numbers
    mean = xBar(values) # Get the mean

    # Sample standard deviation formula (sqrt of sum of squared differences from mean divided by n-1)
    return (sum((x - mean) ** 2 for x in values) / (len(values) - 1)) ** 0.5

def main():
    values = getInputs()        # Get user inputs
    mean = xBar(values)         # Calculate mean
    deviation = stdDev(values)  # Calculate standard deviation
    
    # Display results
    print(f"Mean: {mean:.3f}")
    print(f"Standard Deviation: {deviation:.3f}")

if __name__ == "__main__":
    main()