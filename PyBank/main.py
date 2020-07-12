import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

months = []
revenue = []
revenue_change = []
month_max = []
month_min = []

with open(budget_csv, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:
        
        months.append(row[0])
        revenue.append(int(row[1]))

    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months: " + str(len(months)))
    print("Total: $" + str(sum(revenue)))
    

    for i in range(len(revenue)-1):
        revenue_change.append(revenue[i+1] - revenue[i])
    
        # find the month corresponding to max and min values 
        # (https://stackoverflow.com/questions/6193498/pythonic-way-to-find-maximum-value-and-its-index-in-a-list)
        max_value = max(revenue_change)
        max_index = revenue_change.index(max_value)

        min_value = min(revenue_change)
        min_index = revenue_change.index(min_value)

    print("Average Change: $" + str(round(sum(revenue_change)/len(revenue_change),2)))

    print("Greatest Increase in Profits: " + str(months[max_index + 1]) + " ($" + str(max(revenue_change)) + ")")

    print("Greatest Decrease in Profits: " + str(months[min_index + 1]) + " ($" + str(min(revenue_change)) + ")")