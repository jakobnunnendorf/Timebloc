import random
import datetime

def random_string(length):
    char_set = "abcdefghijklmnopqrstuvwxyz0123456789"
    rand_str = ""
    for i in range(length):
        rand_str += char_set[random.randint(0,len(char_set)-1)]
    return rand_str

# generate_uid takes a summary and a timestamp in UTC YYYYMMDDTHHMMSSZ and returns a unique identifier
def generate_uid(summary):
    DTSTAMP_str = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ") #returns the current time in UTC in the format YYYYMMDDTHHMMSSZ
    return summary+"-"+DTSTAMP_str+"@"+random_string(4)+"-"+random_string(4)+"-"+random_string(4)+"-"+random_string(4)