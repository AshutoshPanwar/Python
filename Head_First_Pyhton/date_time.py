# Import standard library
import datetime

Date = datetime.date.today()        # Today's Date
print(Date)

# Different parts of today date
print()
print("Different parts of today date:")
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)

# Now whats time
import time
print()
print("Right now time is:")
print(time.strftime("%H:%M"))       # Time right now!