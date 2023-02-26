import datetime
import time

# Get the current year and let user input date
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
input_date = input("Enter the date (DD-MM): ")
day = str(int(input_date.split("-")[0]))
month = months[int(input_date.split("-")[1])-1]
year = datetime.datetime.now().year
date = day + " " + month + " " + str(year)

# Get the time
def convert_24_to_12(time_24):
    hour, minute = time_24.split(":")
    hour = int(hour)
    if hour == 0:
        hour = 12
        am_pm = "AM"
    elif hour < 12:
        am_pm = "AM"
    elif hour == 12:
        am_pm = "PM"
    else:
        hour -= 12
        am_pm = "PM"
    return f"{hour}:{minute}:00 {am_pm} SGT"

input_time = input("Enter time in 24 hour format (HH:MM): ")
time_12 = convert_24_to_12(input_time)
# print("Time in 12 hour format:", convert_24_to_12(time_24))

# create first line: "Date:	28 January 2023 at 1:48:56 PM SGT"
first_line = "    Date:    " + date + " at " + time_12 + "\n"
second_line = "    Location:	" + "\n" + "\n"
body = "TB1\n\nTLDR:\n\nResults:\n\nComments:\n\n"

# create the template
template = first_line + second_line + body

print(template)

text_file = open("/Users/jakobnunnendorf/Github/DayOne-templates/test/first_ouput.txt", "w")
 
#write string to file
text_file.write(template)
 
#close file
text_file.close()