import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)
    
    row_counter = 0
    total = 0
    total2 = 0
    change = 0
    
    for row in csvreader:
        row_counter = row_counter + 1
        total = total + int(row[1])
        
    for i, row in csvreader:
        change = int(row[i+1, 1]) - int(row[i, 1])
        total2 = total2 + change
    average = total2 / row_counter
        
    print("Financial Analysis")
    print("-------------------------")
    print(f'Total months: {row_counter}')
    print(f'Total: {total}')
    print(f'Average Change: $-{average}')
    