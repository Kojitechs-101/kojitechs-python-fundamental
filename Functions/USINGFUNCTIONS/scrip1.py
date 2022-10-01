
def addition(x,y):
    print("-"*88)
    print(f"The addition of {x} and {y} is: {x + y}")
    print("-"*88)
    return None

def subtraction(x,y):
    print("-"*88)
    print(f"The subtraction of {x} and {y} is: {x - y}")
    print("-"*88)
    return None

"""
x = 20
y = 30
addition(x,y)
subtraction(x,y)
"""    

def main():
    x = 20
    y = 30
    addition(x,y)
    subtraction(x,y)
    return None

"""
main()
"""    

if __name__ == "__main__":
   main()
