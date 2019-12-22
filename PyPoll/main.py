import os
import csv

election_data = os.path.join('02-Homework','03-Python','Instructions','PyPoll', 'Resources', 'election_data.csv')
election_data_csv = "election_data.csv"

total_votes = 0
candidate_name = "" 
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""

with open(election_data, newline = "") as election_data_csv :
    election_data_csv_reader = csv.reader(election_data_csv, delimiter = ",")
    next(election_data_csv_reader)
    for row in election_data_csv_reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        else:
            candidate_votes[candidate_name] = 1

# percentage and winner
for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

dashline = "-------------------------"

# results
print("Election Results")
print(dashline)
print(f"Total Votes: {total_votes}")
print(dashline)
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percentages[person]} ({vote_count})")
print(dashline)
print(f"Winner: {winner}")
print(dashline)