# start with your input
import os
import csv

# Specify the file path
fileLoad = os.path.join("Resources", "election_data.csv")

#title to hold the output of information
outputFile = os.path.join("ElectionResults.txt")

#variables
totalVotes = 0
candidates = []
candidateVotes = {} 
winnerCount = 0
winner = ""

#read the election data file
with open(fileLoad) as election_data:
    csvreader = csv.reader(election_data)

    #read the header
    header = next(csvreader)

    # for each row
    for row in csvreader:
        #add on to the total votes
        totalVotes += 1

        #check to see if candidate is in list
        if row[2] not in candidates:
            candidates.append(row[2])

            #add the value to your dictionary
            candidateVotes[row[2]] = 1

        else:
            #candidate is already in list
            candidateVotes[row[2]] += 1

# print candidateVotes
voteOutput = ""

for candidates in candidateVotes:
    votes = candidateVotes.get(candidates)
    votePct = (float(votes) / float(totalVotes)) *100.00
    voteCount = (float(votes))
    
    voteOutput += f"\t{candidates}:  {votePct:.3f}% ({voteCount:.0f}) \n"

    if votes > winnerCount:
        winnerCount = votes
        winner = candidates

winnerOutput = f"Winner: {winner}\n-----------------------------"

# create your output
output = (
    f"Election Results\n"
    f"-----------------------------\n"
    f"Total Votes: {totalVotes:,}\n"
    f"-----------------------------\n"
    f"{voteOutput}\n"
    f"-----------------------------\n"
    f"Winner: {winner}\n-----------------------------"
)

print(output)

with open(outputFile, "w") as textFile:
    textFile.write(output)