# import dependancies
import os
import csv

# create variable for filepath of budget csv data
budget_csv = os.path.join('Resources', 'budget_data.csv')

# create empty lists for each variable 
months = []
revenue = []
revenue_change = []

# open the csv file
with open(budget_csv, newline='') as csvfile:
    
    # read the csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    # store the header as a variable
    csvheader = next(csvreader)

    # create a loop for each row
    for row in csvreader:
        
        # add the month values to the months list
        months.append(row[0])
        # add the revenues to the revenue list as integers
        revenue.append(int(row[1]))

    # print the analysis results title and seperator
    print("Financial Analysis")
    print("-----------------------------")

    # print the length of the months list
    print("Total Months: " + str(len(months)))

    # print the sum of the revenue list
    print("Total: $" + str(sum(revenue)))
    
    # create a loop for the length of the revenue list minus one
    for i in range(len(revenue)-1):

        # append the revenue_change list with the difference in values between the next revenue value and the current value
        revenue_change.append(revenue[i+1] - revenue[i])
    
        # find the month corresponding to the max and min values of the revenue_change list
        # used user Escualo's code at url :(https://stackoverflow.com/questions/6193498/pythonic-way-to-find-maximum-value-and-its-index-in-a-list)
        max_value = max(revenue_change)
        max_index = revenue_change.index(max_value)

        min_value = min(revenue_change)
        min_index = revenue_change.index(min_value)

    # print the mean of the revenue_change list (sum of list / length of list)
    print("Average Change: $" + str(round(sum(revenue_change)/len(revenue_change),2)))

    # print the maximum value in the revenue_change list and the corresponding index from the months list
    print("Greatest Increase in Profits: " + str(months[max_index + 1]) + " ($" + str(max(revenue_change)) + ")")

    # print the minimum value in the revenue_change list and the corresponding index from the months list
    print("Greatest Decrease in Profits: " + str(months[min_index + 1]) + " ($" + str(min(revenue_change)) + ")")

#create a variable for the text file path
file_path = os.path.join('analysis', 'main.txt')

# open the text file
file1 = open(file_path, "w")

# write to the text file
# (https://www.geeksforgeeks.org/reading-writing-text-files-python/)
L = ["Financial Analysis \n",
"----------------------------- \n",
f"Total Months: {str(len(months))} \n", 
f"Total: $ {str(sum(revenue))} \n",
f"Average Change: ${str(round(sum(revenue_change)/len(revenue_change),2))} \n",
f"Greatest Increase in Profits: {str(months[max_index + 1])} (${str(max(revenue_change))}) \n",
f"Greatest Decrease in Profits: {str(months[min_index + 1])} (${str(min(revenue_change))}) \n"]

file1.writelines(L)



