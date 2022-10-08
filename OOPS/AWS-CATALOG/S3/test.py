import json
import logging
import random
import uuid

import boto3
from botocore.exceptions import ClientError
s3 = boto3.resource('s3')


logger = logging.getLogger(__name__)


class ObjectWrapper(object):
    
    """Encapsulates S3 object actions."""
    def __init__(self, s3_object):
        """
        :param s3_object: A Boto3 Object resource. This is a high-level resource in Boto3
                          that wraps object actions in a class-like structure.
        """
        self.object = s3_object
        self.key = self.object.key
        return None 
    
    def put(self, data):
        """
        Upload data ti the object.
        """
        put_data = data
        if isinstance(data, str):
            try:
                put_data = open(data, 'rb')
            except IOError:
                logger.exception("Expected file name or binary data, got '%s'.", data)
                   
        try:
            self.object.put(Body=put_data)
            self.object.wait_until_exists()
        except ClientError:
            logger.exception(
             "Couldn't put object '%s' to bucket '%s'.", self.object.key,
                self.object.bucket_name
            )            
        finally:
            if getattr(put_data, 'close', None):
                put_data.close()

    def copy(self, dest_bucket):
        """
        Copies the object to another bucket.

        :param dest_object: The destination object initialized with a bucket and key.
                            This is a Boto3 Object resource.
        """
        try:
            dest_bucket.copy_from(CopySource={
                'Bucket': self.object.bucket_name,
                'Key': self.object.key
            })
            dest_bucket.wait_until_exists()
            logger.info(
                "Copied object from %s:%s to %s:%s.",
                self.object.bucket_name, self.object.key,
                dest_bucket.bucket_name, dest_bucket.key)
        except ClientError:
            logger.exception(
                "Couldn't copy object from %s/%s to %s/%s.",
                self.object.bucket_name, self.object.key,
                dest_bucket.bucket_name, dest_bucket.key)
            raise

                
def main():
    bucket = s3.Bucket('pandan.lambdaa')
    object_key = 'doc-example-object'
    objectwrapper = ObjectWrapper(bucket.Object(object_key))
    # objectwrapper.put(__file__)
    # print(f"Put file object with key {object_key} in bucket {bucket.name}.")

    # with open(__file__) as file:
    #     lines = file.readlines()

    # line_wrappers = []
    # for _ in range(10):
    #     line = random.randint(0, len(lines))
    #     line_wrapper = ObjectWrapper(bucket.Object(f'line-{line}'))
    #     line_wrapper.put(bytes(lines[line], 'utf-8'))
    #     line_wrappers.append(line_wrapper)
    # print(f"Put 10 random lines from this script as objects.")

if __name__ == "__main__":
    main()
    