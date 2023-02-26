from datetime import *
from months import months
from time import gmtime, strftime

year = datetime.now().year # Get the current year
input_date = "03-04"#input("Enter the date (DD-MM): ") # let user input date
day = input_date.split("-")[0]
month = months[int(input_date.split("-")[1])-1]
date = day + " " + month + " " + str(year) # date in correct format

current_date_obj = datetime.strptime(date + " 23:30", '%d %B %Y %H:%M') # convert to datetime object
print(current_date_obj)

bucket = ""

def create_daily_summary(date_obj):
    content = ""
    for i in range(0, 5):
        day_of_year = date_obj.timetuple().tm_yday
        entry_title = "Day" + str(day_of_year) + " Summary"
        entry_date = date_obj.strftime("%d %B %Y")
        entry_time = "11:59:00 PM SGT"
        first_line = "Date:    " + entry_date + " at " + entry_time + "\n"
        content = entry_title + "\n" + "TLDR:\n\nResults:\n\nComments:\n\n"
        entry_template = first_line + "\n" + "\n" + content + "\n" + "\n"
        entry_template
        date_obj += timedelta(days=1)
    return content

print(create_daily_summary(current_date_obj))