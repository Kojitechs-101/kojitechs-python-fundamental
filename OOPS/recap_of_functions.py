## parameters
## arguments 

"""
def addition(x,y):
    print(x + y)
    return None


x = 2
y = 4
addition(x=x,y=y)


"""

## Type of functions
## print func && return function 

# PRINT FUNCTION
"""
def sending_email(name):
    print(f"Hello guys my name is {name}\nI'm a happilly married man with 40 kids")

sending_email("Baca")
"""

# RETURN FUNCTION

"""
def sending_email(name):
    return  f"Hello guys my name is {name}\nI'm a happilly married man with 40 kids"

email = sending_email("Baca")
print(email)

"""

## our args and kwargs in python
# *args non-key/positional arguments 
# **kwargs = for keyworded arguments.

## get_even_numbers

"""
def get_even_numbers(*args):
    
    for number in args:
        if number %2 == 0:
            print(f"Hey found and even number: ", number)
    return None        

get_even_numbers(1,2,3,4,5,6,7,8)
"""


## **kwargs
"""
def team(*args, **kwargs):
    
    for number in args:
        print(number)

    for k,v in kwargs.items():
        print(f"Hi my team name is: {k}\nAnd the best player is :{v}")

    return   None  

team(1,3,4, Ansernal="Saka", Baca="Pedri")
"""



## importing a func from one script to another. 



def addition():
    print("Hi i'm in addition!")
    x = 23


def subtraction():
    print("Hi i'm in subtraction!")
    print(x)


def multiplication():
   print("Hi i'm in multiplication!")


def division():
    print("Hi i'm in division!")


# entrypoint
def function_handler():
    addition()




if __name__ == "__main__":
    function_handler()