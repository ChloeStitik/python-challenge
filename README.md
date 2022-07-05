# python-challenge

PyBank:

# start with your input
import os
import csv

# Specify the file path
fileLoad = os.path.join("Resources", "budget_data.csv")

#title to hold the output of information
outputFile = os.path.join("FinacialAnalysis.txt")

#variables 
totalMonths = 0
totalRevenue = 0 
monthlyChange = []
months = [] 

#open your budget data file
with open(fileLoad) as budget_data:
    csvreader = csv.reader(budget_data)

    #read the header row
    header = next(csvreader)

    #move to first row
    firstRow = next(csvreader)

    #increment the count of months
    totalMonths += 1

    #add on the total amount of revenue
        #revenue is in row 1
    totalRevenue += float(firstRow[1])
    
    #establish previous revenue
    previousRevenue = float(firstRow[1])

    #loop to find our analysis
    for row in csvreader:
    #increment the count of the total months
        totalMonths += 1

    #loop to find the total amount of revenue
        totalRevenue += float(row[1])

        # calculate the net change
        netChange = float(row[1]) - previousRevenue
    #add on to the list of average change
        monthlyChange.append(netChange)

    #add the first month that change occurred
        months.append(row[0])

    #update the previous revenue
        previousRevenue = float(row[1])

    #Calculate the average month change
    averageChange = sum(monthlyChange) / len(monthlyChange)

    greatestIncrease = [months[0], monthlyChange[0]]
    greatestDecrease = [months[0], monthlyChange[0]]

    #use this loop to calculate the index of the greatest and least monthly change
    for m in range(len(monthlyChange)):
        #calculate the greatest increase and decrease
        if(monthlyChange[m] > greatestIncrease[1]):
            #if the value us greater than the greatest increase, that value becomes new greatest increase
            greatestIncrease[1] = monthlyChange[m]
            #update the month
            greatestIncrease[0] = months[m]

        if(monthlyChange[m] < greatestDecrease[1]):
            #if the value us less than the greates increase, that value becomes new greatest decrease
            greatestDecrease[1] = monthlyChange[m]
            #update the month
            greatestDecrease[0] = months[m]
            
# start output
output = (
    f"Finacial Data Analysis\n"
    f"-------------------------\n"
    f"Total Months - {totalMonths} \n"
    f"Total Revenue: ${totalRevenue:,.2f}\n"
    f"Average Change: ${averageChange:.2f}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} ${greatestIncrease[1]:,.2f}\n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} ${greatestDecrease[1]:,.2f}\n"
)

print(output)

# print and export data to text file
with open(outputFile, "w") as textFile:
    textFile.write(output)


    --------------------------------------------------------------------------------------------------------------------


    PyPoll
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