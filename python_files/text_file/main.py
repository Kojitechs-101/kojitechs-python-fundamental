import os 
import time,json



# HOW DO READ A FILE USING PYTHON. 
path = '/Users/kojibello/Downloads/kojitechs-101/kojitechs-python-fundamental/Lambda/today.sh'
path_1 = '/Users/kojibello/Downloads/kojitechs-101/kojitechs-python-fundamental/python_files/json/loaduser_object.json'
# TRADITIONAL WAY OF READING FILES
"""
file = open(path)
print(file.readlines())
file.close()
"""

# # NEW APPROACH 


"""
with open(path) as file:
    objects = file.readlines()
    print(objects)
"""

if os.path.exists(path):
    if os.path.isfile(path):
        with open(path) as file:
            print( file.readlines())
            for each_line in file.readlines():
                pass
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

with open(path_1, 'r') as file:
    x = json.loads(file)

print(x)