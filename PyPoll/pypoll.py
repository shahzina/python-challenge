#PyPoll

import csv
import os

file = os.path.join('..', 'Resources', 'election_data.csv') #file_to_load
output_file = os.path.join('..', 'Resources', 'election_data.txt') #file_to_output

total_votes = 0

candidate_options = [] #empty list for candidate options
candidate_votes = {} #empty dictionary for votes

winning_candidate = ""
winning_count = 0

with open(file) as data: #data aka election_data
	reader = csv.reader(data)
	header = next(reader)
	print(header)

	for row in reader:
		###
		total_votes = total_votes + 1
		candidate_name = row[2]

		if candidate_name not in candidate_options:
			candidate_options.append(candidate_name)
			candidate_votes[candidate_name] = 0

		candidate_votes[candidate_name]=candidate_votes[candidate_name]+1


with open(output_file, "w") as text:
	election_results = print("Election Results: Total Votes: " + str(total_votes))
	print(election_results, end = "")

	text.write(str(election_results))

	for i in candidate_votes:
		votes = candidate_votes.get(i)
		vote_pct = float(votes)/float(total_votes) * 100

		if (votes > winning_count):
			winning_count = votes
			winning_candidate = i 

		voter_output = f"{i}:{vote_pct:.3f}% ({votes})"
		print(voter_output)

		text.write(voter_output)

	print("Winner is " + winning_candidate)
	text.write(winning_candidate)