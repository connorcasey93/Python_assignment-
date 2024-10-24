# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
winning_count = 0
winner=""
# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
# Skip the header row
    header = next(reader)
#Create list in data set
    votes =list(reader)
# Loop through each row of the dataset and process it
for row in votes[0:]:
#Total votes count

        total_votes += 1
        
#Votes for each canidate
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 1
        else : candidate_votes[row[2]] += 1 
        
 # Write the total vote count to the text file
print ("Election Results")
print("--------------------------")
print(f'Total Votes: {total_votes}')    
print("--------------------------")
output= f""" Election Results
--------------------------
Total Votes:{total_votes}
--------------------------"""
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    
 # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, vote_count in candidate_votes.items():
        votes = candidate_votes[candidate]
        if votes > winning_count:
            winning_count = votes
            winner = candidate
 # Get the vote count and calculate the percentage
        vote_percentage = (vote_count / total_votes) * 100
#Print canidates, vote count, and percentage
        #print(f'{candidate}: {vote_percentage:.3f}% ({vote_count})')
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({vote_count})\n"
        print(voter_output, end="")
        txt_file.write(voter_output)


#print(f'Winner: {winner}')
# Save the winning candidate summary to the text file


    winner_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(winner_summary)
    txt_file.write(winner_summary)
    
    
# Print a loading indicator (for large datasets)
print(". ", end="")


       
    
           
                           
             

   
