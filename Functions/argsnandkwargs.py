def sum_numbers(*args):
    print(sum(args)/ len(args))
    
sum_numbers(2,12,23,34,45) 

def student_list(name, orgnames, *listofnames,):
    print(name,orgnames,listofnames)
    
student_list("paul","Baca","koji","bello") 

def phone_shop(**kwargs):
    #print(kwargs.values())
    for k,v in kwargs.items():
        print(k,v)
    
    
phone_shop(Samsung=1234,iphone=1000,Techno=2000,motorola=50000) 

def phone_shop(**kwargs):
    #print(kwargs.values())
    for k,v in kwargs.items():
        print(k)
    
    
phone_shop(Samsung=1234,iphone=1000,Techno=2000,motorola=50000) 

def phone_shop(**kwargs):
    #print(kwargs.values())
    for k,v in kwargs.items():
        print(v)
    
    
phone_shop(Samsung=1234,iphone=1000,Techno=2000,motorola=50000) 

def printing_data(codeName, *args, **kwargs):
    # working simple parameter : codeName
    print(f"I'm learning {codeName}")
    
    # working with args 
    for arg in args:
        print("i AM",arg)
        
    ## working with kwargs

    for keyword in kwargs.items():
        print('I am kwargs',keyword)