import numpy as np
import pandas as pd

df = pd.read_csv("Resources/election_data.csv")

total_vote = df.shape[0]

votes = df.Candidate.value_counts()
percent0 = round(votes[0] / total_vote * 100)
percent1 = round(votes[1] / total_vote *100)
percent2 = round(votes[2] / total_vote *100)
percent3 = round(votes[3] / total_vote *100)

winner = votes.idxmax()

print("Election Results\n.........................")
print(f'Total Votes: {total_vote}')
print("..........................")
print(f'{votes.index[0]}: {percent0}%')
print(f'{votes.index[1]}: {percent1}%')
print(f'{votes.index[2]}: {percent2}%')
print(f'{votes.index[3]}: {percent3}%')
print("..........................")
print(f'Winner: {winner}')
print("..........................")

file = open("pypoll_output.txt", "w")

file.write("Election Results\n.........................\n")
file.write(f'Total Votes: {total_vote}\n')
file.write("..........................\n")
file.write(f'{votes.index[0]}: {percent0}%\n')
file.write(f'{votes.index[1]}: {percent1}%\n')
file.write(f'{votes.index[2]}: {percent2}%\n')
file.write(f'{votes.index[3]}: {percent3}%\n')
file.write("..........................\n")
file.write(f'Winner: {winner}\n')
file.write("..........................\n")

file.close()