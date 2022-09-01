
from datetime import datetime 
from pprint import pprint 
import time

tim = datetime.now()

#print(dir(tim))

print(tim.minute)
print(tim.year)
print(tim.second)

# 2022-08-31 17:27:14.354373
# 
print(tim.strftime("%Y-%m-%d")) # JUST THE YEAR

# THE MINUTE
print(tim.strftime("%Y-%m-%d %H:%m")) 



for i in range(1, 10):
    print(f"I love python {i}")
    time.sleep(5)
