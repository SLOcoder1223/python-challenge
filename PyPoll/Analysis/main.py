import os 
import csv
from collections import Counter

# import the cvs file for analysis
csvpath= os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    votes = [row[2] for row in csvreader]
    # went with counter function found from stackover flow
    numberofvotes = Counter(votes) 

print(numberofvotes)

# sum of total number of votes
votetotal = sum(numberofvotes.values())
print(votetotal)

# creating list of candidates
listofcandidates = []
for candidates in votes:
   if candidates not in listofcandidates:
        listofcandidates.append(candidates)

print(listofcandidates)

# percentage of votes for each candidate
charlesvotes = round((numberofvotes["Charles Casper Stockham"]/votetotal * 100), 3)
dianavotes = round((numberofvotes["Diana DeGette"]/votetotal * 100), 3)
raymonvotes = round((numberofvotes["Raymon Anthony Doane"]/votetotal * 100), 3)

# totalling votes by individual candidate
# using key function to return 
popularvote = max(numberofvotes.values())
winningcandidate = [i for i in numberofvotes.keys() if numberofvotes[i] == popularvote]
print(', '.join(winningcandidate))

# Summary output
print(f"""
Election Results
-------------------     
Total Votes: {votetotal}
-------------------
Charles Casper Stockham: {charlesvotes}% ({numberofvotes['Charles Casper Stockham']})
Diana DeGette: {dianavotes}% ({numberofvotes["Diana DeGette"]})
Raymon Anthony Doane: {raymonvotes}% ({numberofvotes["Raymon Anthony Doane"]})
-------------------
Winner: {', '.join(winningcandidate)}
-------------------
""")


with open("PyPollAnalysis.txt", "w", newline="") as textfile:
    textfile.write(f"""
    
Election Results
-------------------
Total Votes: {votetotal}
-------------------
Charles Casper Stockham: {charlesvotes}% ({numberofvotes['Charles Casper Stockham']})
Diana DeGette: {dianavotes}% ({numberofvotes["Diana DeGette"]})
Raymon Anthony Doane: {raymonvotes}% ({numberofvotes["Raymon Anthony Doane"]})
-------------------
Winner: {', '.join(winningcandidate)}
-------------------
""")
