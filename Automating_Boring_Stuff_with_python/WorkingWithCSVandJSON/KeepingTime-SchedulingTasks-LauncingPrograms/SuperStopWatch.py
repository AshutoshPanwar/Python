#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press ENTER to begin. \nAfterward, press Enter to "click" the stopwatch.\nPress Ctrl-C to quit.')
input()     # Press Enter to begin
print('Started....')
startTime = time.time()     # Get first lap starting time
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    # Handle the Ctrl-C exception.
    print('\nDone.')