import sys
from constants import *
import pysftp
import boto3

class Extractor:
    def __init__(self):
        pass

    @staticmethod
    def decorate_command(line):
        return line.strip().upper()

    def get_commands_from_file(self, file_name):
        with open(file_name) as cmd_file:
            for line in cmd_file:
                cmd = self.decorate_command(line)
                yield cmd


class StdinExtractor(Extractor):
    def __init__(self):
        pass

    def extract(self, arg):
        for line in sys.stdin:
            cmd = self.decorate_command(line)
            yield cmd


class S3Extractor(Extractor):
    def __init__(self):
        pass

    @staticmethod
    def get_bucket_and_obj_name(arg):
        s3_path = arg.split("//")[1]
        s3_path_arr = s3_path.split('/')

        bucket_name = s3_path_arr[0]
        object_name = '/'.join(s3_path_arr[1:])

        return bucket_name, object_name

    def extract(self, arg):
        s3_bucket, s3_object = self.get_bucket_and_obj_name(arg)

        local_path = "/tmp/input_file.txt"
        s3_client = boto3.client(
            's3',
            aws_access_key_id=S3_ACCESS_KEY,
            aws_secret_access_key=S3_SECRET_KEY,
        )
        with open(local_path, 'wb') as f:
            s3_client.download_fileobj(s3_bucket, s3_object, f)

        return self.get_commands_from_file(local_path)


class FileExtractor(Extractor):
    def __init__(self):
        pass

    def get_file_name_from_arg(self, arg):
        return arg.split("//")[1]

    def extract(self, arg):
        file_name = self.get_file_name_from_arg(arg)
        return self.get_commands_from_file(file_name)


class SFTPFileExtractor(FileExtractor):
    def __init__(self):
        pass

    def extract(self, arg):
        remote_path = self.get_file_name_from_arg(arg)
        local_path = "/tmp/input_file.txt"
        with pysftp.Connection(host=SFTP_HOST, username=SFTP_USER, password=SFTP_PASSWORD) as sftp:
            sftp.get(remote_path, local_path)

        return self.get_commands_from_file(local_path)
