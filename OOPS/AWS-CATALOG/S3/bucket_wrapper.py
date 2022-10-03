
"""
Purpose

Show how to use AWS SDK for Python (Boto3) with Amazon Simple Storage Service
(Amazon S3) to perform basic bucket operations.
"""

import json
import logging
import uuid

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

class BucketWrapper(object):
    """Encapsulates S3 bucket actions."""

    def __init__(self, bucket):
        """
        :param bucket: A Boto3 Bucket resource. This is a high-level resource in Boto3
                       that wraps bucket actions in a class-like structure.
        """
        self.bucket = bucket 
        self.name = bucket.name

    def create(self): 
        try:
            self.bucket.create()

            self.bucket.wait_until_exists()
            logger.info(
                "Created bucket '%s'", self.bucket.name)
        except ClientError as error:
            logger.exception(
                "Couldn't create bucket named '%s'",
                self.bucket.name)
            raise error
        return None   

    def delete(self):
        """
        Delete the bucket. The bucket must be empty or an error is raised.
        """
        try:
            self.bucket.delete()
            self.bucket.wait_until_not_exists()
            logger.info("Bucket %s successfully deleted.", self.bucket.name)
        except ClientError:
            logger.exception("Couldn't delete bucket %s.", self.bucket.name)
            raise
        return None   

    def exists(self):
        """
        Determine whether the bucket exists and you have access to it.

        :return: True when the bucket exists; otherwise, False.
        """
        try:
            self.bucket.meta.client.head_bucket(Bucket=self.bucket.name)
            logger.info("Bucket %s exists.", self.bucket.name)
            exists = True
        except ClientError:
            logger.warning(
                "Bucket %s doesn't exist or you don't have access to it.",
                self.bucket.name)
            exists = False
        return exists           

    @staticmethod
    def list(s3_resource):
        try:
            buckets = list(s3_resource.buckets.all())
            logger.info("Got buckets: %s.", buckets)
        except ClientError:
            logger.exception("Couldn't get buckets.")
            raise
        else:
            return buckets



def usage_demo():
    print('-'*88)
    print("Welcome to the Amazon S3 bucket demo!")
    print('-'*88)    
    
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    s3_resource = boto3.resource('s3')

    prefix = 'doc-example-bucket-'
    created_buckets = [
        BucketWrapper(s3_resource.Bucket(prefix + str(uuid.uuid1()))) for _ in range(3)
    ]
    for bucket in created_buckets:
        print(f"Created bucket {bucket.name}.")

    bucket_to_delete = created_buckets
    # if bucket_to_delete.exists():
    #     print(f"Bucket exists: {bucket_to_delete.name}.")

    # bucket_to_delete.delete()
    # print(f"Deleted bucket {bucket_to_delete.name}.")
    # if not bucket_to_delete.exists():
    #     print(f"Bucket no longer exists: {bucket_to_delete.name}.")  


    # for bucket in delete_bucket:
    #     print(f"Got bucket {bucket.name}.")           
    return None         



if __name__ == '__main__':
    usage_demo()