"""
Purpose

Shows how to use the AWS SDK for Python (Boto3) with AWS Secrets Manager to
create and manage secrets, and how to use a secret that contains database credentials
to access an Amazon Aurora database cluster.
"""

import argparse
import base64
import json
import logging
from pprint import pprint
import time
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

class SecretsManagerSecret:

    """Encapsulates Secrets Manager functions."""

    def __init__(self, secretsmanager_client):
        """
        :param secretsmanager_client: A Boto3 Secrets Manager client.
        """
        self.secretsmanager_client = secretsmanager_client
        self.name = None

    def _clear(self):
        self.name = None

    def create(self, name, secret_value):

        self._clear()
        try:
            kwargs = {'Name': name}
            if isinstance(secret_value, str):
                kwargs['SecretString'] = secret_value
            elif isinstance(secret_value, bytes):
                kwargs['SecretBinary'] = secret_value
            response = self.secretsmanager_client.create_secret(**kwargs)
            self.name = name
            logger.info("Created secret %s.", name)
        except ClientError:
            logger.exception("Couldn't get secret %s.", name)

        else:
            return response


    def describe(self, name=None):
        """
        Gets metadata about a secret.

        :param name: The name of the secret to load. If `name` is None, metadata about
                     the current secret is retrieved.
        :return: Metadata about the secret.
        """
        if self.name is None and name is None:
            raise ValueError
        if name is None:
            name = self.name
        self._clear()
        try:
            response = self.secretsmanager_client.describe_secret(SecretId=name)
            self.name = name
            logger.info("Got secret metadata for %s.", name)
        except ClientError:
            logger.exception("Couldn't get secret metadata for %s.", name)
            raise
        else:
            return response



def main():
    """
    Shows how to use AWS Secrets Manager to create a secret, update its value and
    stage, and delete it.
    """
    secret = SecretsManagerSecret(boto3.client('secretsmanager'))
    print("Create a secret")
    secret.create("doc-example-secretsmanager-secret", "Shh, don't tell.")




if __name__ == '__main__':
    main()