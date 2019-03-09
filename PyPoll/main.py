import os
import csv
import numpy as np

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    
    
    total = 0
    row_count = 0
    vote_list = []
    khan_count = 0
    correy_count = 0
    li_count = 0
    Otooley_count = 0
    for row in csvreader:
        vote_list.append(row)
        if row[2] == "Khan":
            khan_count = khan_count + 1
        if row[2] == "Correy":
            correy_count = correy_count + 1
        if row[2] == "Li":
            li_count = li_count + 1
        if row[2] == "O'Tooley":
            Otooley_count = Otooley_count + 1
        #print(row[2])
        
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(len(vote_list)))
    k_total = khan_count / len(vote_list)
    print("Khan: " + "{:.1%}".format(k_total) +" (" + str(khan_count) + ")")
    c_total = correy_count / len(vote_list)
    print("Correy: " + "{:.1%}".format(c_total) +" (" + str(correy_count) + ")")
    l_total = li_count / len(vote_list)
    print("Li: " + "{:.1%}".format(l_total) +" (" + str(li_count) + ")")
    o_total = Otooley_count/ len(vote_list)
    print("O'Tooley: " + "{:.1%}".format(o_total) +" (" + str(Otooley_count) + ")")
    print("----------------------------")
    if khan_count > correy_count and li_count and Otooley_count:
        print("Winner: Khan")
    elif correy_count > khan_count and li_count and Otooley_count:
        print("Winner: Correy")
    elif li_count > correy_count and khan_count and Otooley_count:    
        print("Winner: Li")
    else:
        print("Winner: O'tooley")
