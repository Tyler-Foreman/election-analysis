# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of cotes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import package dependencies
import csv
import os

# Set variable for election_results.csv file
file_to_load = os.path.join("Resources" , "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0
# Create an empty list for candidate options
candidate_options = []
# Create an empty candidate dictionary
candidate_votes = {}
# Create a variable for winning candidate
winning_candidate = ""
# Create a variable for winning count
winning_count = 0
# Create a variable for winning percentage
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes +=1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to each candidate's count
        candidate_votes[candidate_name] += 1

    # Iterate through the candidate list
    for candidate_name in candidate_options:
        
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = (float(votes) / float(total_votes)) * 100
        # Print the candidate name and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}%  ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If the following statements are both true, 
            # set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning candidate equal to the candidates name
            winning_candidate = candidate_name

    winning_candidate_summary = (
            f"----------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"----------------------\n")
    print(winning_candidate_summary)


        
       

