
import os 
import platform

#path = input("Provide user name: ")
path = "/Users/kojibello/Downloads/kojitechs-101/kojitechs-python-fundamental"
desire_ext = input("Enter desire extension: ")

if os.path.exists(path):
    if os.path.isdir(path):
        print(f"{path} is a directory")
        for r,d,f in os.walk(path):
            if len(f) !=0:
                for each_file in f:
                    if each_file.endswith(desire_ext):
                        print(os.path.join(r,each_file))
    else:
        print("Please provide a directory instead")            
else:
    print(f"{path} doesn't exists")

