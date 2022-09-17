# Variable scope in python

x = "Hello World"       # Global Variable

def func():
    x = 10      # Local Vaiable
    print(x)

print(x)        # Hello World
func()      # 10
print(x)        # Hello World