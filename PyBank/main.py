import os
import csv

# Init Stuff
months = []
profit = []


def output():

    print(
        f"""
        Financial Analysis
        ---------------------------
        Total Months: {totalMonths}
        Total: ${total}
        """
        )

# Open and read csv
with open('budget_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip headers
    next(csvreader, None)

    # Loop through csv
    for rows in csvreader:
        months.append(1)
        change = float(rows[1])
        profit.append(change)
    
        


    totalMonths = len(months)
    total = sum(profit)
    output()
    
    
    