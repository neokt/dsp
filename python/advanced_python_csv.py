from pandas import DataFrame
# importing from advanced_python_regex prints its output, which can be ignored
from advanced_python_regex import emails

email_csv = DataFrame(emails)
email_csv.to_csv('emails.csv', header = False, index = False)