import os #standard library
import csv
from collections import Counter
#!/usr/bin/env python

__author__ = "Brennan Copp"
__credits__ = ""
__version__ = "3.8"

# import the cvs file of raw data
FilePath= os.path.join("Resources", "election_data.csv")

with open(FilePath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    Votes = [row[2] for row in csvreader]
    VoteCount = Counter(Votes) # Charles should have 85213 votes

print(VoteCount)

# sum of total all votes 
TotalVotes = sum(VoteCount.values())
print(TotalVotes)

# list of candidates who received votes
CandidateList = []
for candidates in Votes:
   if candidates not in CandidateList:
        CandidateList.append(candidates)

print(CandidateList)

# percentage of votes for each candidate
CCSVotes = round((VoteCount["Charles Casper Stockham"]/TotalVotes * 100), 3)
DDVotes = round((VoteCount["Diana DeGette"]/TotalVotes * 100), 3)
RADVotes = round((VoteCount["Raymon Anthony Doane"]/TotalVotes * 100), 3)

# winner based on popular vote
MostVotes = max(VoteCount.values())
Winner = [i for i in VoteCount.keys() if VoteCount[i] == MostVotes]
print(Winner)

# Summary output
# \ indicated new line in python
print(
    "Election Results \n Total Votes: {TotalVotes} \n Charles Casper Stockham: {CCSVotes}% \n Diana DeGette: {DDVotes}% \n Raymon Anthony Doane: {RADVotes}% \n Winner: {Winner}")


with open("CompleteAssignPyPoll.txt", "w", newline="") as textfile:
    textfile.write(f"Election Results \n Total Votes: {TotalVotes} \n Charles Casper Stockham: {CCSVotes}% \n Diana DeGette: {DDVotes}% \n Raymon Anthony Doane: {RADVotes}% \n Winner: {Winner}")


# NOTE: Analysis should show up in the terminal and exported to a text file
# NOTE: repo needs to have detailed 'README.md' file
