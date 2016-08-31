from datetime import datetime as dt

date_start = '01-02-2013'
date_stop = '07-28-2015'   

date_start = dt.strptime(date_start, '%m-%d-%Y')
date_stop = dt.strptime(date_stop, '%m-%d-%Y')
delta = date_stop - date_start
print 'a)', delta.days

date_start = '12312013'
date_stop = '05282015'

date_start = dt.strptime(date_start, '%m%d%Y')
date_stop = dt.strptime(date_stop, '%m%d%Y')
delta = date_stop - date_start
print 'b)', delta.days

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

date_start = dt.strptime(date_start, '%d-%b-%Y')
date_stop = dt.strptime(date_stop, '%d-%b-%Y')
delta = date_stop - date_start
print 'c)', delta.days
