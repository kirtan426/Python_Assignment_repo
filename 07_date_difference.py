# Use datetime.strptime() to parse input.
# Subtract and print .days.

from datetime import datetime

def date_diff(start, end):
    format = "%d-%m-%Y"
    start_date = datetime.strptime(start, format)
    end_date = datetime.strptime(end, format)
    diff = end_date - start_date
    return diff.days

birthdate = "01-01-2000"
today = "26-06-2025"
print(f"Days lived: {date_diff(birthdate, today)}")