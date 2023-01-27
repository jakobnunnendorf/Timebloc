const logs = false; // set to true to enable console logs

// We use the ical-generator library to generate the ics file
const ical = require('ical-generator'); // imports the ical-generator library

const calendar = ical({name: 'Apple Calendar'}); //creates a new calendar

/* Now we want to specify the date, start and end time of our event
In Javascript the Date object can be initialized with the following parameters:
new Date(year, month, day, hours, minutes, seconds, milliseconds) */

// 1) date
const input_year = 2001; // input the year of the event in the format YYYY
const input_month = 09; // input the month of the event in the format MM
const input_day = 20; // input the day of the event in the format DD
// 2) start time
const input_start_hour = 13; // input the start hour of the event in the format HH
const input_start_minute = 00; // input the start minute of the event in the format MM
// 3) end time
const input_duration_MM = 30; // input the duration of the event in the format MM
function minutes_to_milliseconds(minutes) {
    return minutes * 60000;
}

// Now we can create the Date Object
const event_date = new Date(input_year, input_month-1, input_day, input_start_hour, input_start_minute); //Jan = 0 & Dec = 11
const event_end_date = new Date(event_date.getTime() + minutes_to_milliseconds(input_duration_MM));


// Now we can add the event to the calendar
calendar.createEvent({
    start: event_date,
    end: event_end_date,
    summary: 'Birthday',
    description: '',
    location: '',
    url: '',
});

if(logs) console.log(calendar.toString());