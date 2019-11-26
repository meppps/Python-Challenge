import os
import csv

# Init Stuff
months = []
total = 0.0
avgChange = []

positiveCash = []
negativeCash = []

def output():

    print(
        f"""
        Financial Analysis
        ------------------
        Total Months: {totalMonths}
        Total: ${total}
        """
        )

# Open and read csv
with open('budget_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for rows in csvreader:
        months.append(1)
        values = float(rows[1])
        print(values)
        total += values
        # if int(rows[1]) >= 0:
            # positiveCash.append(rows[1])
        # elif int(rows[1]) < 0:
            # negativeCash.append(rows[1])

    totalMonths = len(months)
    # totalCash = sum(total)
    # print(positiveCash)
    # print(negativeCash)
    # total = positiveCash + negativeCash
    # print(sum(positiveCash))
    #totalCash = sum(total)
    #print(totalCash)
    # output()
    print(totalMonths)
    print(total)
    