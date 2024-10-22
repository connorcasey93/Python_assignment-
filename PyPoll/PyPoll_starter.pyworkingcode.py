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

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}
# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    # Skip the header row
    header = next(reader)
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


    # Loop through the candidates to determine vote percentages and identify the winner
for candidate, vote_count in candidate_votes.items():
            percentage = (vote_count / total_votes) * 100
            print(f'{candidate}: {percentage:.3f}% ({vote_count})')

        # Get the vote count and calculate the percentage

            percentage = (vote_count / total_votes) * 100
            
        # Update the winning candidate if this one has more votes

winner = max(candidate_votes, key=candidate_votes.get)     
        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary
with open(file_to_output, "w") as txt_file:
    print(f'Total Votes: {total_votes}')
    print(f'{candidate}: {percentage:.3f}% ({vote_count})')
    print(f'Winner: {winner}')

    # Save the winning candidate summary to the text file


    
        # Print a loading indicator (for large datasets)
print(". ", end="")

 # Increment the total vote count for each row
       
       
       
    
    #Canidate name and number of votes
       
    
           
                           
             #
# Open a text file to save the output


    # Print the total vote count (to terminal)
   
