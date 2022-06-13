# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Read and Write Paths
file_to_load = os.path.join('Resources', 'election_results.csv')

file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Variable, Constants, Lists, and Dictionaries
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ''
winning_count = 0
winning_percentage = 0



# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read in the header.
    headers = next(file_reader)

    # Print each row in CSV file and total.
    for row in file_reader:
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Checks against candidate list.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list and insert key values into dictionary.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Increments vote tally per candidate by 1.
        candidate_votes[candidate_name] += 1

# Write to text file for final report.
with open (file_to_save, 'w') as txt_file:

    election_results = (
        
        f'\nElection Results\n'
        f'--------------------------------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'--------------------------------------------------\n')
    
    
    print(election_results, end='')

    # Write to Election Text file.

    txt_file.write(election_results)

    # Loops through candidate votes and tallies percentaged, then prints and writes to text results.
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes) / float(total_votes)) * 100
        candidate_results = (f'{candidate_name}: received {vote_percentage: .1f}% of the vote. ({votes:,})\n')
        print(candidate_results)
        txt_file.write(candidate_results)


        # Todo: Print out each candidate's name, vote count, and the percentage of votes to terminal 

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Wining candidate summary print to terminal and to text results.
    
    winning_candidate_summary = (
        f'--------------------------------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage: .1f}%\n'
        f'--------------------------------------------------\n')

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
