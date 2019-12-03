import os
import csv
from collections import Counter

# Init stuff 
voteCount = 0
votes = []
candidates = []
results = []
winner = 'undetermined'

# Print results after running
def output():
    candOut = f"""
    Election Results
    -----------------------------------
    Total Votes: {voteCount}
    ----------------------------------- """
    for i in range(len(candidates)):
        candOut += f"\n    {candidates[i]}: {candPercents[i]}%  {candResults[i]}"
    candOut += f"""
    -----------------------------------
    Winner: {winner}
        """
    return candOut

# Open and read csv
with open('election_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Store/Skip headers
    header = next(csvreader)
   
    # Loop through csv/add up votes
    for rows in csvreader:
        voteCount += 1
        candidateVote = rows[2]
        votes.append(candidateVote)


    # Calculate/store candidate results
    candidates = list(Counter(votes).keys()) 
    candResults = list(Counter(votes).values()) 
    candPercents = [round((num/voteCount) * 100) for num in candResults]
    resultsDict = Counter(votes)
    winner = max(resultsDict, key=resultsDict.get)

    print(output())

# Set variable for output file
output_file = 'results.txt'

#  Open the output file
with open(output_file, "w") as datafile:
    datafile.write(output())
    