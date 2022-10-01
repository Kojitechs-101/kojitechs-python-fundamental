print("Calling scrip2:", __name__)
from scrip1 import addition, subtraction

"""
# import scrip1

scrip1.addition(x,y)
scrip1.subtraction(y,x)
"""

"""
# from scrip1 import addition
addition(x,y)
subtraction(x,y)
"""

def multiply(x,y):
    print("-"*88)
    print(f"The multiplication of {x} and {y} is: {x * y}")
    print("-"*88)
    return None

def lambda_handler():
    x = eval(input("Enter number for x: "))
    y = eval(input("Enter number for y: "))
    multiply(x,y)

    addition(x,y)
    return None

"""
x = 20
y = 30
multiply(x,y)

"""    

"""
lambda_handler() 
"""


if __name__ == "__main__":
   lambda_handler() 
   




