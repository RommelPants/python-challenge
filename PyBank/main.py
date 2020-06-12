#!/usr/bin/env python
# coding: utf-8

# In[115]:


import pandas as pd

#locating file path and opening file
budget_file = "./resources/budget_data.csv" 
budget_file_pd = pd.read_csv(budget_file)

budget_file_pd['Change'] = budget_file_pd['Profit/Losses'].shift(-1) - budget_file_pd['Profit/Losses']

budget_file_pd['Change'] = budget_file_pd['Change'].shift(1)

budget_file_pd
budget_file_pd.to_csv("./resources/budget_data.csv", header=True, index=False)

#descriptive dataset analysis to determine profits/losses over accoutning period
months = str(budget_file_pd["Date"].count())
budget_file_pd.set_index('Date', inplace = True)
total = str(budget_file_pd["Profit/Losses"].sum())   
average = str(budget_file_pd["Change"].mean())
maxprofit_month = str(budget_file_pd["Change"].idxmax())
maxprofit_amount = str(budget_file_pd["Change"].max())
maxloss_month = str(budget_file_pd["Change"].idxmin())
maxloss_amount = str(budget_file_pd["Change"].min())

#print to terminal
print('Financial Analysis')
print('-------------------------')
print(f'Total Months: ' + months)
print(f'Total: $' + total)
print(f'Average Change: $' + average)
print(f'Greatest Increase in Profits: ' + maxprofit_month + ' ($' + maxprofit_amount + ')')
print(f'Greatest Decrease in Profits: ' + maxloss_month + ' ($' + maxloss_amount + ')')


# Print summary to output text file
# Passing the 'w' argument here to
# overwrite any previously saved content
print('Financial Analysis', file = open('./analysis/output.txt', 'w'))
print('-------------------------', file = open('./analysis/output.txt', 'a'))
print(f'Total Months: ' + months, file = open('./analysis/output.txt', 'a'))
print(f'Total: $' + total, file = open('./analysis/output.txt', 'a'))
print(f'Average Change: $' + average, file = open('./analysis/output.txt', 'a'))
print(f'Greatest Increase in Profits: ' + maxprofit_month + ' ($' + maxprofit_amount + ')', file = open('./analysis/output.txt', 'a'))
print(f'Greatest Decrease in Profits: ' + maxloss_month + ' ($' + maxloss_amount + ')' , file = open('./analysis/output.txt', 'a'))



# In[ ]:




