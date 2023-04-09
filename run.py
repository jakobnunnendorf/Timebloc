from ics_calendar import *
from TB_WB_generator import *

with open("/Users/jakobnunnendorf/Desktop/timeblocks.ics", "w") as f:
    f.write(template)

with open("/Users/jakobnunnendorf/Desktop/dayone.txt", "w") as f:
    f.write(text_file)