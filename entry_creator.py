def create_entry(entry_title, entry_content, entry_path):
    # create template according to this format:
    #	Date:	28 January 2023 at 1:48:56 PM SGT
	#   Location:	Yale NUS College, Singapore

    # Example Header
    # Lorem ipsum
    
    # create the txt file:
    text_file = open(entry_path+"/"+entry_title+".txt", "w")

    #write string to file
    text_file.write(entry_content)
    
    #close file
    text_file.close()

# test
#create_entry("TB1", "28 January 2023", "1:48:56 PM SGT", "/Users/jakobnunnendorf/Github/DayOne-templates/test")