import os
import csv
import pandas as pd 
import numpy as np 



csvPath = os.path.join("..","Resources","election_data.csv")
data_output = os.path.join("output_poll_data.txt")


print("Election Results")
print("-----------------------------------------")

def voter_count():
    with open(csvPath,newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)
        voter = sum(1 for row in csvfile)

    with open(csvPath,newline="") as csvfile:
        csvreader = pd.read_csv(csvfile)
        df = pd.DataFrame(csvreader)
        candidate_count = df["Candidate"].value_counts()
        candidate_1 = (candidate_count['Khan'])
        candidate_2 = (candidate_count['Correy'])
        candidate_3 = (candidate_count['Li'])
        candidate_4 = (candidate_count["O'Tooley"])
        
        winner = candidate_count.idxmax(axis=1)

        percent_1 = (candidate_1/voter) * 100
        round_percent_1 = format(percent_1,'.3f')
        percent_2 = (candidate_2/voter) * 100
        round_percent_2 = format(percent_2,'.3f')
        percent_3 = (candidate_3/voter) * 100
        round_percent_3 = format(percent_3,'.3f')
        percent_4 = (candidate_4/voter) * 100
        round_percent_4 = format(percent_4,'.3f')
        
        
    print(f'Total Votes: {voter}')
    print('-------------------------------------------')
    print(f'Khan: {round_percent_1}% ({candidate_1})')
    print(f'Correy: {round_percent_2}% ({candidate_2})')
    print(f'Li: {round_percent_3}% ({candidate_3})')
    print(f"O'Tooley: {round_percent_4}% ({candidate_4})")
    print('-------------------------------------------')
    print(f'Winner: {winner}')
    print('-------------------------------------------')

    data_output = open('output_poll_data.txt','w')
    data_output.write('Election Results\n')
    data_output.write('----------------------------------\n')
    data_output.writelines(f'Khan: {round_percent_1}% ({candidate_1})\n')
    data_output.writelines(f'Correy: {round_percent_2}% ({candidate_2})\n')
    data_output.writelines(f'Li: {round_percent_3}% ({candidate_3})\n')
    data_output.writelines(f"O'Tooley: {round_percent_4}% ({candidate_4})\n")
    data_output.write('----------------------------------\n')
    data_output.write(f'Winner: {winner}\n')
    data_output.write('----------------------------------\n')
voter_count()

