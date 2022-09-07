import json
import os
from pprint import pprint

path = "/Users/kojibello/Downloads/kojitechs-101/kojitechs-python-fundamental/python_files/json/parameter.json"
path_1 = "/Users/kojibello/Downloads/kojitechs-101/kojitechs-python-fundamental/python_files/json/loaduser_object.json"
# user_input = r"C:\Users\totim\OneDrive\Documents\python-class\python-fundamental-101\Python\text-file\json\parameter.json"

"""
if os.path.exists(path):
    if os.path.isfile(path):
        with open(path) as file:
            object = file.read()
    else:
         print(f"please enter file only!")  
else:
     print(f"Your path {path} doesn't exists!!")
"""

data = {"Nam": "Koji Bello", "age": 24, "Programmin_Language": "Python", "Nationality": "N9ja"}

"""
with open(path_1, "w") as file:
    json.dump(data, file, indent=4)
"""

"""
if os.path.exists(path):
    if os.path.isfile(path):
        with open(path) as file:
            object = file.read()
            # json.load(object)
    else:
         print(f"please enter file only!")  
else:
     print(f"Your path {path} doesn't exists!!")    

with open(path_1, "w") as file:
    json.dump(object, file)     
"""

path = "/Users/algalabe/Downloads/github_python/kojitechs-python-fundamental/loaduser_object.json"

if os.path.exists(path_1):
    if os.path.isfile(path_1):
        with open(path_1) as file:
            json_object= json.load(file)
    else:
        print(f"path {path_1} is not a file")
else:
    print(f"path {path_1} does not exist")

for object in json_object:
    print(object.get('Nationality'))