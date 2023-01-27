const readline = require('readline');

const fs = require('fs');
const load_path = require('path');

const path = load_path.join(process.cwd(), "Desktop/calBlocs.ics");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let icsString;

const ical = require('ical-generator');
// Create a new calendar
const cal = ical();

// Specify timezone
cal.timezone('Asia/Singapore');

// function that adds specified amount of minutes
const add_minutes = (time, minutes) => {
    let newtime = new Date(time.getTime());
    return new Date(newtime.setMinutes(newtime.getMinutes() + minutes));
}

// Specify timeframe
const year = new Date().getFullYear();
let target_date;
let wake_up;
let sleep;

// specify work pattern
let work_interval;
let short_break;
let long_break;
let work_blocks;
let target_start;
let target_end;

function addEvents(){
    const enableLoop = true;
    const enableLogs = false;

    let current_time = target_start
    let i=1;
    if (enableLoop) {
    while(current_time.valueOf() < target_end.valueOf()){
        let end_point = add_minutes(current_time, work_interval); // MANUALLY ADD END POINT
        if (i % 4 == 0 && i != 0) {
            current_time = add_minutes(current_time, long_break-short_break);
            if(enableLogs){
                console.log(`${long_break}min break`)
            }
        }
        if(enableLogs){console.log(`start time for TB${i}`)}
        if(enableLogs){console.log(current_time.toString())}
        if(enableLogs){
            console.log(`end time`)
            console.log(end_point.toString())}
        cal.createEvent({
            start: current_time,
            end: end_point,
            summary: `TB${i}`,
            description: 'Event Description'
        });
        current_time = add_minutes(end_point, short_break);
        if(enableLogs){console.log("----------------")}
        i++;
    }
    }
    icsString = cal.toString();
    fs.writeFileSync(path, icsString);
    console.log("Your Calendar has been generated and saved to your desktop. Yayyy!");
}

rl.question('What is the target date? (MM-DD): ', (target_date_input) => {
    target_date = target_date_input;
    rl.question('Do you want to use the default template? (y/n): ', (use_default) => {
        if (use_default === 'y') {
            // Specify timeframe
            wake_up = '06:00:00';
            sleep = '22:00:00';
            target_start = new Date(`${year}-${target_date_input}T${wake_up}`);
            target_end = new Date(`${year}-${target_date_input}T${sleep}`);

            // specify work pattern
            work_interval = 25;
            short_break = 5;
            long_break = 15;
            work_blocks = 4;

            // rest of the code
            addEvents();

        } else if (use_default === 'n') {
            rl.question('When does your day begin? (HH:MM): ', (wake_up_input) => {
                rl.question('What is your day end? (HH:MM): ', (sleep_input) => {
                    rl.question('What is your work interval duration? (minutes): ', (work_interval_input) => {
                        rl.question('What is your short break duration? (minutes): ', (short_break_input) => {
                            rl.question('What is your long break duration? (minutes): ', (long_break_input) => {
                                rl.question('After how many intervals do you want a long break?: ', (work_blocks_input) => {
                                    // Specify timeframe
                                    wake_up = wake_up_input + ":00";
                                    sleep = sleep_input + ":00";
                                    target_start = new Date(`${year}-${target_date_input}T${wake_up}`);
                                    target_end = new Date(`${year}-${target_date_input}T${sleep}`);

                                    // specify work pattern
                                    work_interval = work_interval_input;
                                    short_break = short_break_input;
                                    long_break = long_break_input;
                                    work_blocks = work_blocks_input;

                                    // rest of the code
                                    addEvents();

                                });
                            });
                        });
                    });
                });
            });
        }
    });
});
