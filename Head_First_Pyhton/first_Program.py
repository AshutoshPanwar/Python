from datetime import datetime


from datetime import datetime
from turtle import right

odds = [x for x in range(60) if x % 2 != 0]

right_this_min = datetime.today().minute

if right_this_min in odds:
    print("This min seems a little odd!")
else:
    print("Not an odd min!")