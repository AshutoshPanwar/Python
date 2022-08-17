# Simple program to
# find annual return


#! /usr/bin/python3

# Function Define
def invest(amout, rate,years):
    inc = (amout * rate)/100
    for year in range(int(years)):
        amout = amout+inc
        print(f"year {year+1}: ${amout:.2f}")

# Function call
invest(100, 5, 4)