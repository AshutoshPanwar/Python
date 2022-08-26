def fibonachi():
    i = 0       # Initialize Variable
    num = int(input("Enter how many number's to generate: "))      # Take user input
    if num == 0:
        Fib = [0]
    elif num == 1:
        Fib = [1]
    elif num == 2:
        Fib = [1, 1]
    elif num > 2:
        Fib =[1,1]
        while i < (num - 1):
            Fib.append(Fib[i] + Fib[i-1])
            i += 1
    return Fib

# Print list here
print(fibonachi())