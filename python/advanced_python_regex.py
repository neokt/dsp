import re
import pandas as pd
from collections import Counter

faculty = pd.read_csv('faculty.csv', skipinitialspace=True)

def df_finder(df, col, pattern, sep):
    '''
    Applies re.findall to find all occurrences of a pattern in all elements of a column in a dataframe.
    The sep argument is used to define a character to join the elements into a single string.
    '''
    # isolate column and turn series into a list of strings separated by spaces
    group = sep.join(df[col].tolist())
    # search within group using pattern
    return re.findall(pattern, group)

def unique_elements(elements):
    '''
    Uses Counter to print the frequencies of each element
    '''
    # create a counter object for the list
    c = Counter(elements)
    # print results
    print 'There are', len(c), 'unique elements and', sum(c.values()), 'elements in total.'
    print 'Unique elements:', sorted(list(c))
    print 'Frequencies:', c

def answer(col, pattern, sep, clean = None):
    '''
    Searches the dataframe for the specified pattern and applies an optional cleanup argument that removes all
    occurences of that argument from each result
    '''
    # use dataframe_finder function to return a list with all individual elements
    search = df_finder(faculty, col, pattern, sep)
    # remove clean argument from all list elements, if it is specified
    search = map(lambda x: re.sub(clean, '', x), search) if clean else search
    unique_elements(search)

def find_email():
    '''
    Returns emails found in the dataframe as a list
    '''
    return list(faculty.email)

def find_domain(emails, sep = '@'):
    '''
    Splits a list of e-mails and identifies unique domain names
    '''
    domains = [re.split(sep, e)[1] for e in emails]
    unique_elements(domains)

# in column 'degree', find all sequences of non-whitespace characters
# using a whitespace character to join each element, and removing all occurences of . from the result
print 'Q1:'
answer('degree', r'\S+', ' ', r'\.')

# in column 'title', find all sequences that exclude dash characters
# using a dash character to join each element, and removing all occurences of two letter words + Biostatistics
# from the result
print '\nQ2:'
answer('title', '[^-]+', '-', r' [a-z]{2} Biostatistics')

print '\nQ3:'
emails = find_email()
print emails

print '\nQ4:'
find_domain(emails)