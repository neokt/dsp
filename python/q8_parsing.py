# The football.csv file contains the results from the English Premier League. 
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in 'for' and 'against' goals.

# Solution assumes that the 'smallest difference' between 'for' and 'against is calculated as the
# absolute value of the difference

import pandas as pd

fb = pd.read_csv('football.csv')
fb['Diff'] = abs(fb['Goals'] - fb['Goals Allowed'])
findAbsMin = fb.query('Diff == Diff.min()')
print findAbsMin.iloc[0, 0]