# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of cotes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import packages
import csv
import os

# Set variable for election_results.csv file
file_to_load = os.path.join("Resources" , "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)
    print(headers)
    # To do: perform analysis



# Using the open() function with the 'w' mode we will write data to the file
with open(file_to_save, 'w') as txt_file:
    txt_file.write("Counties in the Election\n" + ("-" * 25)+"\nArapahoe\nDenver\nJefferson")


