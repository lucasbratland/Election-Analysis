# Retreieve the data
#1. The total number of votes cast
#2. A complete list of cadidates who got a vote
#3. Percentage of vote each candidate got
#4. The total number of votes each candidate got
#5. The winner based on vote count

#Import needed modules



import csv

import os


#Assign a variable to the file to load 
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize vote counter
total_votes = 0
#candidate list
candidate_options = []
#declare vote counting dictionary
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# #Open the results file and read file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    #print header row. 
    headers = next(file_reader)
    # print(headers)

    #Print each rpw in the CSV file
    for row in file_reader:
            #Add to total vote count
            total_votes += 1
            #print candidates name
            candidate_name = row[2]
            #see if candidate name in candidate list already
            if candidate_name not in candidate_options:
                #add it to the list
                candidate_options.append(candidate_name)
                
                #BEGIN TRACKING THAT CANDIdATES VOTE
                candidate_votes[candidate_name] = 0

            #Add a vote to the candidate
            candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------------\n"
        f"Total Votes {total_votes:,}\n"
        f"-------------------------------\n")
    print(election_results, end="")

    #save the final vote count to text file
    txt_file.write(election_results)

    #iterate through candidates names
    for candidate_name in candidate_votes:
        #retrieve cote count
        votes = candidate_votes[candidate_name]
        #calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #is vote count greate than winning count? 

        #print each candidates votes
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes >= winning_count) and (vote_percentage > winning_percentage):
            #if ture set winning to current
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    

    winning_candidate_summary = (
        f"-------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"-------------------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

   