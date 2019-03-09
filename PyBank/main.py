import os
import csv
import numpy as np

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    
    
    total = 0
    row_count = 0
    compare_list = []
    for row in csvreader:
        total= total + int(row[1])
        row_count = row_count + 1
        compare_list.append(row[1])
        difference = int(row[1])
       #print(compare_list)
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(row_count))
    print("Total: $" + str(total))
    
    row_count = 0
    total = 0
    difference_list = []
    for n in compare_list:
        difference = int(compare_list[row_count])-int(compare_list[row_count-1])
        difference_list.append(difference)
        if row_count == len(compare_list) - 1:
            break
        row_count = row_count + 1
        total = total + difference
        
        
    
    print("Average  Change: $" + str(total / row_count))
    print("Greatest Increase in Profits: " + str(max(difference_list)))
    print("Greatest Decrease in Profits: " + str(min(difference_list)))
