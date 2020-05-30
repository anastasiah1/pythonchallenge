import os
import csv

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what candidate they would like to search for
    name_to_check = input("What candidate do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        if row[2] == "Khan": 

            khan_votes +=1

            elif row[2] == "Correy":

            correy_votes +=1

            elif row[2] == "Li": 

            li_votes +=1

            elif row[2] == "O'Tooley":

            otooley_votes +=1
# Print Election Results
print(f'Election Results')

#The total number of votes cast
print(f'Total Votes')

# Create a dictionary to hold the candidate's names.
candidates ={}

# Create a dictionary using the built-in Function.
candidates = dict {}

# A dictionary of an candidate.
candidate = {"name": "Li"}
print(f'{candidates["name"]})

#A complete list of candidates who received votes
# Loop through each candidate in the spring and
# and push to an array 
candidates_list = ["Khan" "Correy" "Li "O'Tooley"]
candidates =[]
print(f(candidates[name] = candidate_list'"Khan" "Correy" "Li 'O'Tooley')
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)
# print (total votes fo Candidates)
total votes =sum(candidate)
print(total votes)

or Total Votes for Candidates:
    Total_Votes []

#The percentage of votes each candidate won

import os
import csv

#The total number of votes each candidate won
total votes =sum(candidate)
print(total votes)
# Print a the summary of Votes for each candidate

khan_percent = (khan_votes/total_votes) *100

correy_percent = (correy_votes/total_votes) * 100

li_percent = (li_votes/total_votes)* 100

otooley_percent = (otooley_votes/total_votes) * 100

#The winner of the election based on popular vote.
pct_won = round( int(candidate,[3]) / total_candidates *100, 2 )

 print(f'{(election_data[3]}'{pct}% and   

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What candidate name are you looking for? ")

#Path to collect data from Resources folder
election_data_csv = os.path.join('Resources' , election_data.csv')

#Define function called print_percentages accept a list containing data for single candidate
def print_percentages(candidate_data):

# Loop through the data
    for row in csvreader:

        # If the candidate's in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)

print("Election Results")

print("-----------------------")

print(f"Total Votes: {total_votes}")

print(f"----------------------------")

print(f"Khan: {khan_percent:.3f}% ({khan_votes})")

print(f"Correy: {correy_percent:.3f}% ({correy_votes})")

print(f"Li: {li_percent:.3f}% ({li_votes})")

print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")

print(f"----------------------------")

print(f"Winner: {key}")

print(f"----------------------------")

