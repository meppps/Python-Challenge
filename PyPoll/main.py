import os
import csv
from collections import Counter

# Init stuff 
voteCount = 0
votes = []
candidates = []
results = []
winner = 'undetermined'

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
        -------------------------
        Winner: {winner}
        """
    )

# Open and read csv
with open('election_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip headers
    next(csvreader, None)

    

    for rows in csvreader:
        voteCount += 1

        candidateVote = rows[2]
        votes.append(candidateVote)

        # if candidate not in candidates:
            # results[candidate] = candVotes
        # elif candidate in candidates:

        

    
    candidates = list(Counter(votes).keys()) # equals to list(set(votes))
    candResults = list(Counter(votes).values()) # counts the elements' frequency
    candPercents = [(num/voteCount) * 100 for num in candResults]
    winner = max(candidates)

    output()
    # print(Counter(votes))