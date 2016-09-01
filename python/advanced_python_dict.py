import re
import pandas as pd
from collections import defaultdict

faculty = pd.read_csv('faculty.csv', skipinitialspace=True)

# creation of firstname/lastname columns and cleanup of title column
faculty['firstname'] = faculty['name'].str.split(' ').apply(lambda x: x[0], 1)
faculty['lastname'] = faculty['name'].str.split(' ').apply(lambda x: x[-1], 1)
faculty['title'] = faculty['title'].apply(lambda x: re.sub(r' [a-z]{2} Biostatistics', '', x), 1)

# initialize faculty dataframe as list
faculty_list = faculty.values.tolist()

# initialize defaultdict
d = defaultdict(list)
for k in faculty_list:
    d[k[5]].append(k[1:4])
faculty_dict = dict(d)

# re-initialize defaultdict
d = defaultdict(list)
for k in faculty_list:
    d[(k[4], k[5])] = k[1:4]
professor_dict = dict(d)

print 'Q6: Printing as tuple key-value pairs'
print sorted(faculty_dict.items(), key = lambda x: x[0])[:3]

print '\nQ6 Alternative: Printing as dictionary'
faculty_dict_sorted = {k: faculty_dict[k] for k in sorted(faculty_dict.keys())[:3]}
print faculty_dict_sorted

print '\nQ6 Alternative: Unsorted solution'
faculty_dict_sample = {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}
print faculty_dict_sample

print '\nQ7: Printing as tuple key-value pairs'
print sorted(professor_dict.items(), key = lambda x: x[0])[:3]

print '\nQ7 Alternative: Printing as dictionary'
professor_dict_sorted = {k: professor_dict[k] for k in sorted(professor_dict.keys())[:3]}
print professor_dict_sorted

print '\nQ7 Alternative: Unsorted solution'
professor_dict_sample = {k: professor_dict[k] for k in professor_dict.keys()[:3]}
print professor_dict_sample

print '\nQ8: Printing as tuple key-value pairs'
print sorted(professor_dict.items(), key = lambda x: x[0][1])