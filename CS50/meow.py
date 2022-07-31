# Simple program to
# print meow no of
# times user want


# Function declaration
def main():
    n = int(input("No of time to speak: "))
    meow(n)         # Function meow() call

# Function declaration
def meow(n):
    for i in range(n):
        print("meow!")

# Program start to exiecute from here
main()