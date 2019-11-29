import os
import csv

# Init stuff 
voteCount = 0
votes = []
candidates = []
results = {}
results["iphone 5S"] = 2013

def output():
    print(f"""
        Election Results
        -------------------------
        Total Votes: {voteCount}
        Candidates :{results}
        -------------------------

        """
    ,width=1)

# Open and read csv
with open('election_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip headers
    next(csvreader, None)

    candVotes = []

    for rows in csvreader:
        voteCount += 1
        candidate = rows[2]
        votes.append(candidate)

        if candidate not in candidates:
            results[candidate] = candVotes
        elif candidate in candidates:
            results[candidate] = candVotes + 1

    # output()

    print(results)