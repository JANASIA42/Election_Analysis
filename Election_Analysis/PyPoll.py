# Add dependencies.
import csv
import os

# Assign a variable to load a file (direct path).
file_to_load = 'Resources/election_results.csv'

#Assign a variable to save the file to a path (direct path).
file_to_save = 'analysis/election_analysis.txt'

# Initialize a vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate doesn't match any existing candidate, add them to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # After opening the file, print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n")

    print(election_results, end="")
    
    # After printing the final vote count to the terminal, save the final vote count to the text file.
    txt_file.write(election_results)

    # Iterate through candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
    
        # Determine winning vote count, winning percentage and winning candidate.

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage 
            winning_candidate = candidate_name

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------\n")

    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)