import platform 
import os

# Linux commands
"""
ls, ls -al, pwd, mkdir, touch, cat, grep, awk ===> (scanning). sed, chmod, chown, rmdir, man, watch 
"""

# windows commands
"""
dir, cls, mkdir, cd , net, reboot, restart, notepad, new-files, calls, watch 
"""

"""
if platform.system() == "Windows":
    print(f"This is {platform.system()} os\n{os.system('cls')}")
else:
    print(f"This is {platform.system()}  os\n{os.system('clear')}")
"""

# use user inputs
"""
cmd = input("Please Enter your desired command: ")
run_command = os.system(cmd)

if platform.system() == "Windows":
    print(f"This is {platform.system()} os\n{run_command}")
else:
    print(f"This is {platform.system()}  os\n{run_command}")
"""

# x = 23 
# y = 35 

# x,y = 23,35
# print(y)

# list 

# fruits = ["apple","pear", "pawpaw","mango","plum","cherry"]

# first, second, third, *fourth = fruits
# print(second)

# dict 


student_info = {"Name": "Koji Bello","Age": 24,"Language": "python","Nationality": "Cameroonian"}
l_1 = []
for k,v in student_info.items():
    l_1.append(v)
print(l_1)    

# tuple
# x = [('Name', 'Koji Bello'), ('Age', 24), ('Language', 'python'), ('Nationality', 'Cameroonian')]

# for k,v in x:
#     print(k,v)