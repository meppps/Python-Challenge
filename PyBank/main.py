import os
import csv
from collections import Counter
import statistics

# Init lists
months = []
profit = []
diff = []


def output():

    print(
        f"""
        Financial Analysis
        ---------------------------
        Total Months: {len(months)}
        Total: ${total}
        Average Change: 
        Greatest Increase in Profits : {maxMonth} ${maxChange}
        Greatest Decrease in Profits : {minMonth} ${minChange}
        """
        )

# Open and read csv
with open('budget_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    budget_data = 'budget_data.csv'
    # Skip/Store headers
    header = next(csvreader)

    # Loop through csv
    for rows in csvreader:
        months.append(rows[0])
        change = float(rows[1])
        profit.append(change)

        # print(change)
        # changeDiff = change - previousNum
        # previousNum = change
        # changes.append(change)
    # for i to len

    # print(statistics.mean(changes))

    total = sum(profit)
    
    # print(profit)
    
    length = len(profit)
    diff = [profit[i] - profit[i-1] for i in range(length)]
    # for i in range(length):
    #     if i == 1:
    #         next 
    #     diff.append(profit[i] - profit[i-1])
    
    
    # ! IGNORE !
    # for increase in profit:
    #     if increase > 0:
    #         increases.append(increase)


    print(f"profit mean:{statistics.mean(profit)}")
    print(f"diff mean: {statistics.mean(diff)}")



    # Find greatest increase/decrease in profits
    # Find the matching index to get the month
    maxChange = round(max(diff))
    maxIndex = diff.index(max(diff))
    maxMonth = months[maxIndex]
    
    minChange = round(min(diff))
    minIndex = diff.index(min(diff))
    minMonth = months[minIndex]
    
    
    # print(maxProfit)
    # output()

   
    
    
    