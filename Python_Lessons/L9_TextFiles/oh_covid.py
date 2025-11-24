"""
Name: Alex Oh
Date: 11/19/25

File: oh_covid.py

Purpose: Reads a text file containing COVID-19 data and calculates
         the average number of COVID-19 cases per state.
"""

def main():

    # Read txt file and add contents to lists: states & COVID-19 cases
    with open("covid19_txt.txt", "r") as f:     # Open txt file for reading
                                                # and assign it to file object f
        
        states = []                             # States list
        cases = []                              # COVID-19 cases list
        for line in f:                          # Iterate through each line in file
            l = line.split(",")                 # Split each line at the comma
            states.append(l[0].strip())         # Strip ws and \n and append the month to months
            cases.append(l[1].strip())          # Strip ws and \n, convert to int, and append the cases to cases
        
        # Calculate average number of COVID-19 cases
        sumCases = sum([int(c) for c in cases[1:]], 1)  # Sum of all COVID-19 cases
        avgCases = sumCases / (len(cases) - 1)          # Number of states

        # Display results in a table
        print(f"{states[0]:^10}{cases[0]:^14}") # Table header
        
        for i in range(1, len(states)):         # Iterate through states and cases lists excluding first row
            print(f"{states[i]:^10}{cases[i]:^14}")
        
        print(f"The average number of cases is: {avgCases:.0f}")

if __name__ == "__main__":
    main()