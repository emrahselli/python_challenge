import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)
    
    candidates = []
    vote_count = []
    total_vote = 0
    
    for row in csvreader:
        total_vote = total_vote + 1
        
        candidate = row[2]
        
        if candidate in candidates:
            cand_idx = candidates.index(candidate)
            vote_count[cand_idx] = vote_count[cand_idx] + 1
            
        else:
            candidates.append(candidate)
            vote_count.append(1)
    
    percents = []
    winner_votes = vote_count[0]
    winner_index = 0

    for count in range(len(candidates)):
        vote_percent = vote_count[count] / total_vote * 100
        percents.append(vote_percent)
        if vote_count[count] > winner_votes:
            winner_votes = vote_count[count]
            winner_index = count
            
    winner = candidates[winner_index]

    percents = [round(i, 2) for i in percents]

    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_vote}")
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {percents[i]}% ({vote_count[i]})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")

    file = open("pypoll_output.txt", "w")
    
    file.write("Election Results\n--------------------------\n")
    file.write(f"Total Votes: {total_vote}\n")
    for i in range(len(candidates)):
        file.write(f"{candidates[i]}: {percents[i]}% ({vote_count[i]})\n")
    file.write("---------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("---------------------------\n")
    file.close()