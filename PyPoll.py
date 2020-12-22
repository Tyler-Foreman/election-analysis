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

# Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes +=1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

print(total_votes)
print(candidate_options)



# Using the open() function with the 'w' mode we will write data to the file
with open(file_to_save, 'w') as txt_file:
    txt_file.write("Counties in the Election\n" + ("-" * 25)+"\nArapahoe\nDenver\nJefferson")


