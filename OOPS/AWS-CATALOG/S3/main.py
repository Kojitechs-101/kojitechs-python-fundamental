import sys
import boto3
from botocore.exceptions import ClientError

"""
The purpose of this Demo
Is to create, list and delete buckets in Amazon S3.
"""

def list_my_buckets(resource):
    """
    Param: resource(str)
    """
    
    print('Buckets:\n\t', *[b.name for b in resource.buckets.all()], sep="\n\t")
    return None

def create_and_delete_my_buckets(resource, bucket_name, keep_bucket):
    list_my_buckets(resource) 

    try:
        print(f"\nCreating new bucket: {bucket_name}")
        bucket = resource.create_bucket(
            Bucket= bucket_name
        )
    except ClientError as e:
        print(f"Couldn't create bucket Here's why: {e.response['Error']['Message']}")
        raise
    bucket.wait_until_exists()
    list_my_buckets(resource) 

    if not keep_bucket:
        print(f"\nDeleting bucket:, {bucket_name}")
        bucket.delete()

        bucket.wait_until_not_exists()
        list_my_buckets(resource) 
    else:
        print(f"\nKeeping bucket:, {bucket_name}")    


def main():
    import argparse

    parser = argparse.ArgumentParser()
    # parser.add_argument('bucket_name', help='The name of the bucket to create.')
    # parser.add_argument('region', help='The region in which to create your bucket.')
    # parser.add_argument('--keep_bucket', help='Keeps the created bucket. When not ' 'specified, the bucket is deleted ' 'at the end of the demo.', action='store_true')

    args = parser.parse_args()
    resource = boto3.resource('s3')
    list_my_buckets(resource)
    try:
        print(resource.meta.client.meta.region_name)
        create_and_delete_my_buckets(resource=resource, bucket_name="demois.djd", keep_bucket=False)

    except ClientError:
        print('Exiting the demo')


if __name__ == "__main__":
    main()