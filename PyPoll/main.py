import os
import csv  
import pandas as pb
import numpy as np 

csvPath = os.path.join("..","Resources","election_data.csv")
data_output = os.path.join("output_poll_data.txt")

print("Election Results")
print("-----------------------------------------")


def total_voter():
    with open(csvPath,newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)
        total_vote = sum(1 for row in csvfile)


    candidate = []
    vote_count = []
    data = {}
    votes = 0
    percent_vote = {}
    with open(csvPath,newline="") as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")
        csv_header = next(csvreader)
        for row in csvreader:
            votes += 1
            if row[2] in data.keys():
                data[row[2]] = data[row[2]] + 1
            else:
                data[row[2]] = 1
    for key,value in data.items():
        candidate.append(key)
        vote_count.append(value)

    for key,value in data.items():
        percent_vote[key] = round((value/votes) * 100,3)
    
    winner=""
    winner_count = 0
    for key in data.keys():
        if data[key] > winner_count:
            winner = key
            winner_count = data[key]



    print(f'Total Votes: {total_vote}')
    print('-------------------------------------------')
    print(f'Khan: {list(percent_vote.values())[0]}%  ({vote_count[0]})')
    print(f'Correy: {list(percent_vote.values())[1]}%  ({vote_count[1]})')
    print(f'Li: {list(percent_vote.values())[2]}%  ({vote_count[2]})')
    print(f"O'Tooley: {list(percent_vote.values())[3]}%  ({vote_count[3]})")
    print('-------------------------------------------')
    print(f'Winner: {winner}')
    print('-------------------------------------------')

    data_output = open('output_poll_data.txt','w')
    data_output.write('Election Results\n')
    data_output.write('----------------------------------\n')
    data_output.writelines(f'Khan: {list(percent_vote.values())[0]}%  ({vote_count[0]})\n')
    data_output.writelines(f'Correy: {list(percent_vote.values())[1]}% ({vote_count[1]})\n')
    data_output.writelines(f'Li: {list(percent_vote.values())[2]}% ({vote_count[2]})\n')
    data_output.writelines(f"O'Tooley: {list(percent_vote.values())[3]}% ({vote_count[3]})\n")
    data_output.write('----------------------------------\n')
    data_output.write(f'Winner: {winner}\n')
    data_output.write('----------------------------------\n')
    


total_voter()



