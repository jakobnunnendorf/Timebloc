    # create entry
            entry_title = "TB" + str(tb_counter)
            entry_date = date
            entry_time = current_time_obj.strftime("%I:%M:%S %p SGT")
            entry_path = "/Users/jakobnunnendorf/Github/DayOne-templates/test"
            create_entry(entry_title, entry_date, entry_time, entry_path)
            print("created entry: " + entry_title + " on " + entry_date + " at " + entry_time)
            tb_counter += 1
            # add block duration to current time
            current_time_obj = add_block_duration(current_time_obj, block_duration)
            # add short break
            current_time_obj = add_short_break(current_time_obj, short_break_duration)