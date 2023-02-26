from entry_creator import create_entry #creates txt files, input title, date, time, path
from time_convert import convert_24_to_12
from datetime import *
from gather_input import *
from timezone import *

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

text_file = ""
n = 1
while current_time + interval_duration <= end_time:
    entry = ""
    entry += "Date:    " + current_time.strftime("%-d %B %Y at %I:%M:%S %p") + " GMT" + return_current_timezone_utc().replace("0","") + "\n\n\n"
    entry += "TB" + str(n) + "\n"
    entry += "TLDR:\n<br>\nResults:\n<br>\nComments:\n<br>\n\n"

    current_time += interval_duration + short_break_duration
    if n % long_break_interval == 0:
        entry += "Date:    " + current_time.strftime("%-d %B %Y at %I:%M:%S %p") + " GMT" + return_current_timezone_utc().replace("0","") + "\n\n\n"
        entry += "WB" + str(int(n/4)) + "\n"
        entry += "TLDR:\n<br>\n<br>\nResults:\n<br>\n<br>\nComments:\n<br>\n<br>\n\n\n"
        current_time += long_break_duration
    n += 1
    text_file += entry

print(text_file)

