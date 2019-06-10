import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)
    
    row = next(csvreader, None)
    max_m = row[0]
    min_m = row[0]
    profit = float(row[1])
    row_counter = 1
    total = float(row[1])
    change_total = 0
    max_p = 0
    min_p = 0
    prev_profit = profit
    
    for row in csvreader:
        row_counter = row_counter + 1
        total = total + float(row[1])
        
        profit = float(row[1])
        change = profit - prev_profit
        change_total = change_total + change
        
        if change > max_p:
            max_m = row[0]
            max_p = change
        
        if change < min_p:
            min_m = row[0]
            min_p = change
            
        prev_profit = profit
        
    average = round(change_total / (row_counter - 1))
    
        
    print("Financial Analysis")
    print("-------------------------")
    print(f'Total months: {row_counter}')
    print(f'Total: {total}')
    print(f'Average Change: $-{average}')
    print(f'Greatest increase in profits: {max_m} (${max_p})')
    print(f'Greatest increase in profits: {min_m} (${min_p})')
    
file = open("pybank_output.txt", "w")

file.write("Financial Analysis \n-------------------------\n")
file.write(f'Total months: {row_counter}\n')
file.write(f'Total: {total}\n')
file.write(f'Average Change: $-{average}\n')
file.write(f'Greatest increase in profit: {max_m} ({max_p})\n')
file.write(f'Greatest decrease in profit: {min_m} ({min_p})\n')
file.close()