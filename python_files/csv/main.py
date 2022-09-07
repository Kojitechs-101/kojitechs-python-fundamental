# what's the meaning of csv

# comma, sep, value
# UserName, Access_Key, Secret_key, console_link

import csv,json

path = "/Users/kojibello/Downloads/kojitechs-101/kojitechs-python-fundamental/python_files/csv/main.csv"

# READ csv
"""
with open(path) as file:
    csv_data = csv.reader(file)
    for each_row in csv_data:
        print(each_row)
"""

# WRITE TO A csv FILE

"""
header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albania', '28748', 'AL', 'ALB'],
    ['Algeria', '2381741', 'DZ', 'DZA'],
    ['American Samoa', '199', 'AS', 'ASM']
]

with open("address.csv", "w") as file:
    csv_writer = csv.writer(file)

    # To Create Header
    csv_writer.writerow(header)
    csv_writer.writerows(data)

"""

header = ['Name', 'age', 'Programmin_Language', 'Nationality']

data = "/Users/kojibello/Downloads/kojitechs-101/kojitechs-python-fundamental/python_files/json/loaduser_object.json"
with open(data) as file:
    json_object= json.load(file)

with open("koji_bello.csv", "w") as file:
    csv_writer = csv.DictWriter(file,fieldnames=header)

    csv_writer.writeheader()
    csv_writer.writerows(json_object)

  
