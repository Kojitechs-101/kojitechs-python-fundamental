# what is module in python... 
from genericpath import isdir
import os
from pprint import pprint 

path = "/Users/kojibello/Downloads/scr"

"""
Modules are any file(libary) that ends with .py extention. 
and the main use of a module is for re-usability...........
"""
# methods available with the os module


# pprint(dir(os))
# if u want create directory using python use... 
"""
print(os.mkdir("folder1"))
"""

# remove dir
"""
print(os.removedirs("folder1"))
"""

# seperator 
"""
print(os.sep)
"""

# get present working directory.
"""
print(os.getcwd())
"""
pwd = os.getcwd()

# change directory ... 
"""
print(os.chdir('/Users/kojibello/Downloads'))
"""

## list directory
"""
for directory in os.listdir(path):
    print(directory)
"""
# create directoy
"""
print(os.mkdir("bello"))
"""

# create multiple directories
"""
print(os.makedirs(path))
"""

# remove multiple directories

"""
print(os.removedirs(path))
"""

# rename a directory

"""
print(os.rename(path, "/Users/kojibello/Downloads/scr/kojibello"))
"""

# manage environment variable with python 
"""
os.environ("GIT_TOKEN")
"""


## os.path is one of the most important sub module in os module
print("+++++++==============+++++++++++")

# pprint(dir(os.path))

# base direcorty
"""
print(os.path.basename(path))
"""

# directory name 

"""
print(os.path.dirname(path))
"""

# join two directory path 

path1 = "/Users/kojibello"

path2 = "scr"

"""
print(os.path.join(path1,path2)) # TAKE NOTE!!
"""

# split a directory path to get a list
"""
account_email = "arn:aws:sts::746445775:assumed-role/US-HIS_AWS6479988g98_Non_Privileged_Access/jimmy@mmm.com"

print(os.path.split(account_email)[0])
"""

# how to get the size of a directory
"""
print(os.path.getsize(path)) # size per bytes... 
"""

# if a directory is valid or if it exists
"""
print(os.path.exists(path))
"""

# if a user input/ path is a file... 
"""
print(os.path.isfile("/Users/kojibello/Downloads/kojitechs-101/kojitechs-python-fundamental/python_modules/koji.sh"))
"""


user_input = "/Users/kojibello/Downloads/sc"

if os.path.exists(user_input):
    print(f"The path for {user_input} is a valid")
    if os.path.isdir(user_input):
        print(f"The give path: {user_input} is a directory ")
        for each_dir in os.listdir(user_input):
            print(each_dir)
    else:
        print(f"please enter directory path only!")  
else:
    print(f"Your path {user_input} doesn't exists!!")



# elif os.path.isdir:
#     print(os.listdir(user_input))
# else: 
#     print(f"the path {user_input} is not valid")    

