import csv
from ics import Calendar, Event
from datetime import datetime, timedelta
from pytz import timezone
# Create a new calendar
c = Calendar()
current_year = datetime.now().year

# Open the CSV file
with open('running_plan.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    # For each row in the CSV file
    for row in reader:
        # Get the week start date
        week_start = datetime.strptime(row[0], '%b %d')
        if week_start.month == 1 and week_start.replace(year=current_year) < datetime.now():
            current_year += 1
        week_start = week_start.replace(year=current_year)

        # For each day in the week
        for i in range(1, 8):
            # If there is a run scheduled for that day
            if row[i]:
                # Create a new event
                e = Event()
                e.name = row[i].strip('"')+ " mile run"
                # Set the event start time to 6:30am New York time on that day
                e.begin = week_start.replace(hour=6, minute=30, tzinfo=timezone('America/New_York'))
                # Set the event end time based on the number of miles to run
                e.end = e.begin + timedelta(minutes=10 * float(row[i].strip('"')))
                # Add the event to the calendar
                c.events.add(e)
            # Move to the next day
            week_start += timedelta(days=1)
# Write the calendar to an .ics file
with open('running_plan.ics', 'w') as f:
    f.writelines(c)
