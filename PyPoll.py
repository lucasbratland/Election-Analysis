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

# #Open the results file and read file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    #print header row. 
    headers = next(file_reader)
    print(headers)

    #Print each rpw in the CSV file
    # for row in file_reader:
    #         print(row)




# using the open() function with the "w" mode to write data to file
# outfile = open(file_to_save, "w")

# #openb using with statement
# with open(file_to_save, "w") as txt_file:

    # #write some data in file
    # txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")

#write data to file
# outfile.write("Hello World")

# #close file
# # outfile.close()
# txt_file.close