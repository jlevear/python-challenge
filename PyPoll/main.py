# import dependancies
import os
import csv

# create variable for filepath of election csv data
election_csv = os.path.join('Resources', 'election_data.csv')

# create empty lists for each variable 
voter_id = []
candidate = []

# create list of candidates from line 34
candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]

# open the csv file
with open(election_csv, newline='') as csvfile:
    
    # read the csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    # store the header as a variable
    csvheader = next(csvreader)

    # create a loop for each row
    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])

    # calculate the total votes
    total_votes = len(voter_id) 

    # find the candidate choices
    candidate_set = set(candidate)
    # print(candidate_set)

    # calculate the percentage and count of votes for each candidate
    candidate1_votes = candidate.count(candidate_list[0])
    candidate1_percent = round(candidate1_votes / total_votes * 100)

    candidate2_votes = candidate.count(candidate_list[1])
    candidate2_percent = round(candidate2_votes / total_votes * 100)

    candidate3_votes = candidate.count(candidate_list[2])
    candidate3_percent = round(candidate3_votes / total_votes * 100)

    candidate4_votes = candidate.count(candidate_list[3])
    candidate4_percent = round(candidate4_votes / total_votes * 100)

    # determine the winning candidate
    # https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
    winner = max(set(candidate), key=candidate.count)

# print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidate_list[0]}: {candidate1_percent}% ({candidate1_votes})")
print(f"{candidate_list[1]}: {candidate2_percent}% ({candidate2_votes})")
print(f"{candidate_list[2]}: {candidate3_percent}% ({candidate3_votes})")
print(f"{candidate_list[3]}: {candidate4_percent}% ({candidate4_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#create a variable for the text file path
file_path = os.path.join('analysis', 'main.txt')

# open the text file
file1 = open(file_path, "w")

# write to the text file
# (https://www.geeksforgeeks.org/reading-writing-text-files-python/)
L = ["Election Results \n"
"------------------------- \n",
f"Total Votes: {total_votes} \n",
"------------------------- \n",
f"{candidate_list[0]}: {candidate1_percent}% ({candidate1_votes}) \n",
f"{candidate_list[1]}: {candidate2_percent}% ({candidate2_votes}) \n",
f"{candidate_list[2]}: {candidate3_percent}% ({candidate3_votes}) \n",
f"{candidate_list[3]}: {candidate4_percent}% ({candidate4_votes}) \n",
"------------------------- \n",
f"Winner: {winner} \n",
"------------------------- \n"]

file1.writelines(L)