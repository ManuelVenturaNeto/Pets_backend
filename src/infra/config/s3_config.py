import os
import boto3
from dotenv import load_dotenv

load_dotenv()


class S3Handler:
    """
    Class to define connection with bucket S3
    """

    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=str(os.getenv("AWS_ACCESS_KEY_ID")),
            aws_secret_access_key=str(os.getenv("AWS_SECRET_ACCESS_KEY")),
            region_name=str(os.getenv("AWS_REGION")),
        )
        self.bucket_name = str(os.getenv("AWS_STORAGE_BUCKET_NAME"))
        self.custom_domain = f"{str(os.getenv('AWS_STORAGE_BUCKET_NAME'))}.s3.{str(os.getenv('AWS_REGION'))}.amazonaws.com"
        self.default_acl = "public-read"
        self.cache_control = "max-age=86400"
        self.location = "static"
        self.querystring_auth = False
        self.headers = {
            "Access-Control-Allow-Origin": "*",
        }

    def get_client(self):
        """
        Retorna o cliente do S3.
        """
        return self.s3_client


    def get_bucket_name(self):
        """
        Retorna o nome do bucket S3.
        """
        return self.bucket_name


    def get_location_file(self):
        """
        Return the location of files into s3
        """
        return self.location


    def get_custom_domain(self):
        """
        Return the custom domain of image
        """
        return self.custom_domain


    def get_cache_control(self):
        """
        Return the cache_control
        """
        return self.cache_control
