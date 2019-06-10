import numpy as np
import pandas as pd

df = pd.read_csv("Resources/budget_data.csv")

count_row = df.shape[0]

total = df["Profit/Losses"].sum()

difference = df["Profit/Losses"].diff()

average = round(difference.sum() / (count_row - 1), 2)

maximum = difference.max()

minimum = difference.min()

for row in range(difference.shape[0]):
    if difference.get_value(row) == maximum:
                 max_place = row
                 break
for row in range(difference.shape[0]):
    if difference.get_value(row) == minimum:
                 min_place = row
                 break

max_name = df.iloc[max_place, 0]
min_name = df.iloc[min_place, 0]

print("Financial Analysis \n-------------------------")
print(f'Total months: {count_row}')
print(f'Total: {total}')
print(f'Average Change: $-{average}')
print(f'Greatest increase in profit: {max_name} ({maximum})')
print(f'Greatest decrease in profit: {min_name} ({minimum})')

file = open("pybank_output.txt", "w")
file.write("Financial Analysis \n-------------------------\n")
file.write(f'Total months: {count_row}\n')
file.write(f'Total: {total}\n')
file.write(f'Average Change: $-{average}\n')
file.write(f'Greatest increase in profit: {max_name} ({maximum})\n')
file.write(f'Greatest decrease in profit: {min_name} ({minimum})\n')
file.close()