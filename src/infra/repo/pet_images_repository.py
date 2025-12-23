from typing import BinaryIO
import logging
from botocore.exceptions import ClientError
from src.infra.config import S3Handler

logging.basicConfig(level=logging.INFO)


class PetImagesRepository:
    """
    Class to manage PetImages Repository
    """

    def __init__(self):
        self.s3_config = S3Handler()
        self.s3_client = self.s3_config.get_client()
        self.bucket_name = self.s3_config.get_bucket_name()
        self.location = self.s3_config.get_location_file()
        self.domain = self.s3_config.get_custom_domain()
        self.cache_control = self.s3_config.get_cache_control()



    def insert_file(self, pet_id: int, file: BinaryIO) -> bool:
        """
        Insert the image into bucket S3 and return true or false
        """
        filename = file.filename
        img_data = file.stream

        key = f"{self.location}/{pet_id}/{filename}"

        try:
            # Checking if the file is a valid image
            if not filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                logging.error("Invalid file type for %s. Only image files are accepted.", filename)
                return False

            # add cache control
            extra_args = {"CacheControl": self.cache_control}

            self.s3_client.upload_fileobj(img_data, self.bucket_name, key, ExtraArgs=extra_args)
            logging.info("File %s uploaded successfully to %s", filename, key)
            return True

        except ClientError as e:
            logging.error("Error uploading file %s: %s", filename, e)
            return False

    def select_files(self, pet_id: int) -> list:
        """
        List the images by one pet_id into S3
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=f"{self.location}/{pet_id}/")

            if "Contents" in response:
                return [f'{self.s3_config.get_custom_domain()}/{item["Key"]}' for item in response["Contents"]]

            return []

        except ClientError as e:
            logging.error("Error listing files for pet_id %d: %s", pet_id, e)
            return []


    def delete_file(self, pet_id: int, filename: str) -> bool:
        """
        Delete a file into S3
        """
        key = f"{self.location}/{pet_id}/{filename}"
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=key)
            logging.info("File %s deleted successfully from %s", filename, key)
            return True

        except ClientError as e:
            logging.error("Error deleting file %s: %s", filename, e)
            return False



    def update_file(self, pet_id: int, old_filename: str, new_file: BinaryIO) -> bool:
        """
        Update an image into S3
        """
        try:
            # delete old file
            if not self.delete_file(pet_id=pet_id, filename=old_filename):
                logging.error("Failed to delete old file %s.", old_filename)
                return False

            # insert new file
            if not self.insert_file(pet_id, new_file):
                logging.error("Failed to upload new file for pet_id %d.", pet_id)
                return False

            logging.info("File %s updated successfully for pet_id %d.", old_filename, pet_id)
            return True

        except ClientError as e:
            logging.error("Error updating file %s for pet_id %d: %s", old_filename, pet_id, e)
            return False
