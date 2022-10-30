import boto3
from pprint import pprint
# create a resource object 
resource = boto3.session.Session().resource('ec2', 'us-east-1')
import csv 


def main(inventory_file):
    count = 1
    csv_hearder = ["S_NO", "instance-id", "instance-type", "public-ip", "subnet-id", "status", "creation-date"]
    with open(inventory_file, "w", newline='') as file:
        csv_w = csv.writer(file)
        csv_w.writerow(csv_hearder)
        print("Writting enventory data..!!")
        for ec2 in resource.instances.all():
            csv_w.writerow([count, ec2.id, ec2.instance_type,  ec2.public_ip_address, ec2.subnet_id,  ec2.state['Name'],  ec2.launch_time.strftime("%Y-%m-%d")])
            count +=1
        print("Done!!")


def lambda_handler():
    main("inventory-file.csv") 



if __name__ == "__main__":
    lambda_handler()