## Using python let's generate a csv report 
import csv
import json
## Abdu
"""
header = ['Num','Name','Hire_Date','Salary','Sick_Days_Remaining']
data = [
    ['0','Graham Chapman','03/15/14','50000.0','10'],
    ['1','John Cleese','06/01/15','65000.0','8'],
    ['2','Eric Idle','05/12/14','45000.0','10'],
    ['3','Terry Jones','11/01/13','70000.0','3'],
    ['4','Terry Gilliam','08/12/14','48000.0','7'],
    ['5','Michael Palin','05/23/13','66000.0','8']
]

with open("exercise.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)


"""
## 
# Philo
##

"""
header = ['name', 'Hire_Date', 'Salary', 'Sick_Days_emaining']
data = [
    {"Name": "Graham Chapman",
     "Hire_Date": "03/15/14", 
     "Salary": 50000.0, 
     "Sick_Days_emaining": 10
     },
    {'Name': 'John Cleese', 
    'Hire_Date': "06/01/15", 
    'Salary': 65000.0 ,
    'Sick_Days_emaining':  8
    },
    {'Name': 'Eric Idle', 
    'Hire_Date': 5/12/14,
    'Salary': 45000.0 ,
    'Sick_Days_emaining': 10
    }
]

with open("invoice.csv", "w") as file:
    writer_csv = csv.DictWriter(file, fieldnames=header)
    writer_csv.writeheader()
    writer_csv.writerows(data)    

"""

###
"""

import csv 
 
fields = ['Num , Name, Hire_Date, Salary, Sick_Days_emaining'] 
rows = [ 
    ['0',  'Graham Chapman'  '03/15/14',  '50000.0', '10'], 
    ['1', 'John Cleese',  '06/01/15',  '65000.0' , '8'], 
    ['2', 'Eric Idle', '05/12/14', '45000.0', '10'], 
    ['3', 'Terry Jones', '11/01/13', '70000.0', '3'], 
    ['4', 'Terry Gilliam','08/12/14','48000.0','7'], 
    ['5 ', 'Michael Palin','05/23/13','66000.0','8']
]    

with open("employee_records.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)
"""
