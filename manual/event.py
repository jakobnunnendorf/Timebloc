from random_string import generate_uid
from timezone import return_current_timezone
import datetime
import pytz
# example:

# SUMMARY:TB10
# TRANSP:OPAQUE
# UID:e91d0910-d0ea-4594-bc4b-20c258dab88d@e91d.org
# END:VEVENT
# BEGIN:VEVENT
# DTEND;TZID=Africa/Johannesburg:20230226T201000
# DTSTAMP:20230226T093135Z
# DTSTART;TZID=Africa/Johannesburg:20230226T194500
# LAST-MODIFIED:20230226T093055Z
# SEQUENCE:1

# example variables
# summary_str = "TB10"
# TZID_str = "Africa/Johannesburg"
# DTEND_str = "20230226T201000"
# DTSTAMP_str = "20230226T093135Z"
# DTSTART_str = "20230226T194500"
# LAST_MODIFIED_str = "20230226T093055Z"
# UID_str = generate_uid(summary_str, DTSTAMP_str)

# template = "SUMMARY:" + summary_str+ "\nTRANSP:OPAQUE\nUID:" + UID_str + "\nEND:VEVENT\nBEGIN:VEVENT\nDTEND;TZID=" + TZID_str + ":" + DTEND_str + "\nDTSTAMP:" + DTSTAMP_str + "\nDTSTART;TZID=" + TZID_str + ":" + DTSTART_str + "\nLAST-MODIFIED:" + LAST_MODIFIED_str + "\nSEQUENCE:1"

# create_event takes summary_str (title of the event), end time (YYYYMMDDTHHMMSS) and start time (YYYYMMDDTHHMMSS)

def create_event(summary_str, DTSTART_str, DTEND_str):
    current_UTC = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ") #returns the current time in UTC in the format YYYYMMDDTHHMMSSZ
    DTSTAMP_str = current_UTC
    LAST_MODIFIED_str = current_UTC
    UID_str = generate_uid(summary_str) # generate a unique identifier from the summary and the current time
    TZID_str = return_current_timezone() # get the current time zone

    # create event with the variables
    line1 = "BEGIN:VEVENT\n"
    line2 = "CREATED:"+current_UTC+"\n"
    dtend = "DTEND;TZID=" + TZID_str + ":" + DTEND_str + "\n" # current time zone and input end time (YYYYMMDDTHHMMSS)
    dtstamp = "DTSTAMP:" + DTSTAMP_str + "\n" # current time in UTC in the format YYYYMMDDTHHMMSSZ
    dtstart = "DTSTART;TZID=" + TZID_str + ":" + DTSTART_str + "\n" # current time zone and input start time (YYYYMMDDTHHMMSS)
    last_modified = "LAST-MODIFIED:" + LAST_MODIFIED_str + "\n" # current time in UTC in the format YYYYMMDDTHHMMSSZ
    sequence = "SEQUENCE:0\n"
    summary = "SUMMARY:" + summary_str + "\n" # input title of event
    transp = "TRANSP:OPAQUE\n"
    uid = "UID:" + UID_str + "\n" # input unique identifier (randomly generated)
    line10 = "BEGIN:VALARM\n"
    line11 = "ACTION:NONE\n"
    line12 = "TRIGGER;VALUE=DATE-TIME:19760401T005545Z\n"
    line13 = "END:VALARM\n"
    line14 = "END:VEVENT\n"

    event = line1 + line2 + dtend + dtstamp + dtstart + last_modified + sequence + summary + transp + uid + line10 + line11 + line12 + line13 + line14
    return event

# example call
# print(create_event("TB10", "20230226T201000", "20230226T194500"))