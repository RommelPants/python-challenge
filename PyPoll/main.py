#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

#locating file path and opening file
poll_file = "./Resources/election_data.csv" 
poll_file_pd = pd.read_csv(poll_file)

header = "Election Results"
line = "------------------------"

total_votes = str(poll_file_pd["Voter ID"].count())
candidate_vote_counts =  poll_file_pd["Candidate"].value_counts()  
winner = str(poll_file_pd.groupby('Candidate')['Voter ID'].count().to_frame().idxmax()[0])

# Create list of candidate names
candidates_names = []
for name in poll_file_pd.Candidate.unique():
    candidates_names.append(name)
    
# Creates a list of vote counts by candidate 
vote_counts = []
for count in candidate_vote_counts:
    vote_counts.append(count)

# Create list of vote percentage by candidate 
vote_percentage = []
for count in candidate_vote_counts:
    vote_percentage.append(float(count) / int(total_votes) * 100)

# Zip lists together, iterate through each row,
# and print each line of our analysis (minus a few things)

print('Election Results')
print('-------------------------')
for row in zip(candidates_names, vote_counts, vote_percentage):
    print(f'{row[0]}: {row[2]:.3f}% ({row[1]})\n')
print('-------------------------')
print(f'Winner: ' + winner)
print('-------------------------')

# Print summary to output text file
# Passing the 'w' argument here to
# overwrite any previously saved content
print('Election Results', file = open('./analysis/output.txt', 'w'))
print('-------------------------', file = open('./analysis/output.txt', 'a'))
print(f'Total Votes: ' + total_votes, file = open('./analysis/output.txt', 'a'))
print('-------------------------\n', file = open('./analysis/output.txt', 'a'))
for row in zip(candidates_names, vote_counts, vote_percentage):
    print(f'{row[0]}: {row[2]:.3f}% ({row[1]})\n', file = open('./analysis/output.txt', 'a'))
print('-------------------------', file = open('./analysis/output.txt', 'a'))
print(f'Winner: ' + winner, file = open('./analysis/output.txt', 'a'))
print('-------------------------', file = open('./analysis/output.txt', 'a'))


# In[ ]:




