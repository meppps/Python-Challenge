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
    print(f"""
        Election Results
        -----------------------------------
        Total Votes: {voteCount}
        -----------------------------------
        {candidates[0]}: {candPercents[0]}%  {candResults[0]}
        {candidates[1]}: {candPercents[1]}%  {candResults[1]}
        {candidates[2]}: {candPercents[2]}%  {candResults[2]}
        {candidates[3]}: {candPercents[3]}%  {candResults[3]}
        -----------------------------------
        Winner: {winner}
        """
    )

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

    # Calculate candidate results
    candidates = list(Counter(votes).keys()) 
    candResults = list(Counter(votes).values()) 
    candPercents = [round((num/voteCount) * 100) for num in candResults]
    resultsDict = Counter(votes)
    winner = max(resultsDict, key=resultsDict.get)

    output()