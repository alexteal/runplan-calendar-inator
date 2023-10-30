# Run Plan Gen

Built mostly using gpt.

# Usage

This assumes you run in the mornings, at 6:30 am US/EAST. Little bit of a jank
hardcoded segment, but if you can read python you can figure that out. I'll
add better support to this if I end up moving to a different time zone.

1. Generate a running plan from this website: [trainingplan.run](https://www.trainingplan.run/)
2. Download the output plan as a .csv
3. Rename the .csv to "running_plan.csv"
4. Move "running_plan.csv" to this project's root
5. `python3 -m venv venv; source venv/bin/activate; pip install ics; python3 ./cal_gen.py`
6. _et viola_. Import the output `./running_plan.ics` into your favorite calendar app.
7. AND, don't forget to `deactivate` your python env when done.
