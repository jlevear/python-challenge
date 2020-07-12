import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

months = []
revenue = []

with open(budget_csv, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader:
        
        months.append(row[0])
        revenue.append(int(row[1]))

    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months: " + str(len(months)))
    print("Total: $" + str(sum(revenue)))
    print("Average Change: $")