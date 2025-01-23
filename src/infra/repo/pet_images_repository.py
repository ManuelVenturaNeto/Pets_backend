from typing import BinaryIO
from botocore.exceptions import ClientError
from src.infra.config import S3Handler


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

    def insert_file(self, pet_id: int, file: BinaryIO) -> bool:
        """
        Insert the image into bucket S3 and return true or false
        """
        filename = file.filename
        img_data = file.stream

        key = f"{self.location}/{pet_id}/{filename}"

        try:
            self.s3_client.upload_fileobj(img_data, self.bucket_name, key)
            return True

        except ClientError:
            return False

    def select_files(self, pet_id: int) -> list:
        """
        List the images by one pet_id into S3
        """
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name, Prefix=f"{self.location}/{pet_id}/"
            )
            if "Contents" in response:
                return [
                    f'{getattr(self.s3_config, "custom_domain", "")}/{item["Key"]}'
                    for item in response["Contents"]
                ]
            return []

        except ClientError:
            return []

    def delete_file(self, pet_id: int, filename: str) -> bool:
        """
        Delete a file into S3
        """
        key = f"{self.location}/{pet_id}/{filename}"
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=key)
            return True

        except ClientError:
            return False

    def update_file(self, pet_id: int, old_filename: str, new_file: str) -> bool:
        """
        Update an image into S3
        """
        try:
            self.delete_file(pet_id=pet_id, filename=old_filename)
            self.insert_file(pet_id, new_file)

            return True

        except ClientError:
            return False
