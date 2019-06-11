import numpy as np
import pandas as pd

df = pd.read_csv("Resources/election_data.csv")

total_vote = df.shape[0]

votes = df.Candidate.value_counts()

percents = []

for count in range(len(votes)):
    vote_percent = round(votes[count] / total_vote * 100)
    percents.append(vote_percent)

winner = votes.idxmax()

print("Election Results\n.........................")
print(f'Total Votes: {total_vote}')
print("..........................")
for i in range(len(votes)):
        print(f"{votes.index[i]}: {percents[i]}% ({votes[i]})")
print("..........................")
print(f'Winner: {winner}')
print("..........................")

file = open("pypoll_output.txt", "w")

file.write("Election Results\n.........................\n")
file.write(f'Total Votes: {total_vote}\n')
file.write("..........................\n")
for i in range(len(votes)):
        file.write(f"{votes.index[i]}: {percents[i]}% ({votes[i]})\n")
file.write("..........................\n")
file.write(f'Winner: {winner}\n')
file.write("..........................\n")

file.close()