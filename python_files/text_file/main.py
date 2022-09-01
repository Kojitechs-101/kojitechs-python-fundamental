import os 
import time 


# HOW DO READ A FILE USING PYTHON. 
path = '/Users/kojibello/Downloads/kojitechs-101/kojitechs-python-fundamental/Lambda/today.sh'

# TRADITIONAL WAY OF READING FILES
"""
file = open(path)
print(file.readlines())
file.close()

"""

# NEW APPROACH 


"""
with open(path) as file:
    objects = file.readlines()
    print(objects)
"""

if os.path.exists(path):
    if os.path.isfile(path):
        with open(path) as file:
            objects = file.readlines()
            for each_line in objects:
                print(each_line) # SINCE THIS IS A LIST WE CAN ITERATE

    else:
        print("Please provide a file instead") 
else:
    print(f"{path} doesn't exists") 




# HOW DO WE WRITE TO A FILE?
"""
with open(path, "w") as file:
    for i in range(1, 10):
        file.write(f"python writing line {i}\n")
        file.write("python writing line ")
    time.sleep(5)
"""

# HOW DO WE APPEND TO A FILE?

"""
with open(path, "a") as file:
    for i in range(1, 10):
        file.write(f"python writing line {i}\n")
        file.write("python writing line ")
    time.sleep(5)
"""

