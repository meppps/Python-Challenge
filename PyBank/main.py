import os
import csv
import statistics
from collections import Counter

# Init lists
months = []
profit = []
diff = []


def output():

    return f"""
        Financial Analysis
        ---------------------------
        Total Months: {len(months)}
        Total: ${total}
        Average Change: ${avgChange}
        Greatest Increase in Profits : {maxMonth} ${maxChange}
        Greatest Decrease in Profits : {minMonth} ${minChange}
        """
        

# Open and read csv
with open('budget_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip/Store headers
    header = next(csvreader)

    # Loop through csv / Fill lists for months and profits/losses
    for rows in csvreader:
        months.append(rows[0])
        prof = float(rows[1])
        profit.append(prof)

        
    total = sum(profit)
    
    
    # Calculate differences(prof/loss changes) and output to list
    length = len(profit)
    diff = [profit[i] - profit[i-1] for i in range(length)]
   
    
    # First value is invalid but removing will 
    # offset the index, so I set it to the median first
    # to prevent it from being selected as min/max, as long as theres three or more values in the changes, this works
    
    diff[0] = statistics.median(diff)

    maxChange = round(max(diff))
    maxIndex = diff.index(max(diff)) 
    maxMonth = months[maxIndex]
    
    minChange = round(min(diff))
    minIndex = diff.index(min(diff)) 
    minMonth = months[minIndex]
    
    # Remove first value from list of changes since it's invalid, it distrupts our avg calculation
    diff.pop(0)
    avgChange = round(statistics.mean(diff),2)
   
    print(output())

    
# Set variable for output file
output_file = 'budget.txt'

#  Open the output file
with open(output_file, "w") as datafile:
    datafile.write(output())

    

