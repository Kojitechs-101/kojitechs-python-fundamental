import os 
path = input("Enter path: ")


if os.path.exists(path): 
    if os.path.isdir(path): 
        for r,d,f in os.walk(path,topdown=True):
            if len(f) !=0:
                for each_file in f:
                    print(os.path.join(r,each_file))
    else:     
        print(f"{path} is a file, Provide a valid directory")           
else:
    print(f"Sorry invalid path {path}")                
           



