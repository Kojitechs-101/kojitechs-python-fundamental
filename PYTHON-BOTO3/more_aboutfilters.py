# import boto3
# resource = boto3.session.Session().resource('ec2', 'us-east-1')


# ## .all(), .limit(), .Filter()

# # variable 
# # fliter instance by instance-state
# by_instance_state = [{'Name': 'instance-state-name', 'Values': ['stopped']}] 

# # fliter instance by instance-type
# by_instance_type = [{"Name": "instance-type", "Values": ["t2.large"]}]


# # fliter instance by instance-tags
# by_instance_tags = [{"Name": "tags:Env", "Values":["SBX"]}]

# def main_func(params):
#     ## filter all instances whose state-name shows running....
#     response = resource.instances.filter(
#         Filters= params
#     )
#     for instance in response.all():
#         print(instance.id, instance.state['Name'], instance.instance_type)
    
    
# def lambda_handler():
#     main_func(by_instance_state)
 


# if __name__ == "__main__": 
#     lambda_handler()

# > session 
# > client 
# > resource #  
# > waiter 
# > meta ()
from pprint import pprint

import boto3 

client = boto3.session.Session().client('ec2', 'us-east-1')
resource = boto3.session.Session().resource('ec2', 'us-east-1')

def get_available_regions():
    # we must not use client
    regions = []
    response = client.describe_regions()['Regions']
    
    for region in response:
        regions.append(region['RegionName'])
    print(regions, len(regions) )    
        
    
    
def using_meta_object():
    regions = []
    response = resource.meta.client.describe_regions()['Regions']
    for region in response:
        regions.append(region['RegionName'])
    print(len(regions), regions)
    
    



