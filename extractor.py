import sys
from constants import *
import pysftp
import boto3


class Extractor:
    """
    Extractor base class
    """
    @staticmethod
    def decorate_command(line):
        """
        Decorate the command by stripping whitespaces and all upper cases
        :param line: String of word/s
        :return: Return decorated string
        """
        return line.strip().upper()

    def get_commands_from_file(self, file_name):
        """
        Read file and return the lines in generated object
        :param file_name: file name
        :return: Return generated object of lines
        """
        with open(file_name) as cmd_file:
            for line in cmd_file:
                cmd = self.decorate_command(line)
                yield cmd


class StdinExtractor(Extractor):
    """
    Extractor for stdin
    """
    def extract(self, arg):
        """
        Take inputs from stdin and then send the decorated lines to process
        Can end the commands by pressing 0
        :param arg: Not using
        :return: list of lines
        """
        print("Press 0 to end the command list\n")
        lines = []
        for line in sys.stdin:
            if line.strip() == "0":
                break
            lines.append(self.decorate_command(line))
        return lines


class S3Extractor(Extractor):
    """
    Extractor from AWS S3 buckets and objects
    """
    @staticmethod
    def get_bucket_and_obj_name(arg):
        """
        static method to get bucket and object name from input string
        :param arg: input string
        :return: bucket name and object name
        """
        s3_path = arg.split("//")[1]
        s3_path_arr = s3_path.split('/')

        bucket_name = s3_path_arr[0]
        object_name = '/'.join(s3_path_arr[1:])

        return bucket_name, object_name

    def extract(self, arg):
        """
        Extract list of commands stored in S3
        :param arg: string contains bucket nd object name
        :return: Returns decorated commands list in generated form
        """
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
    """
    Extractor to get strings from file on local machine
    """
    def get_file_name_from_arg(self, arg):
        """
        get file name from string
        :param arg: string
        :return: file name
        """
        return arg.split("//")[1]

    def extract(self, arg):
        """
        Extracted the generated decorated commands from file
        :param arg: input string
        :return: generated object
        """
        file_name = self.get_file_name_from_arg(arg)
        return self.get_commands_from_file(file_name)


class SFTPFileExtractor(FileExtractor):
    """
    Extractor to extract commands from file at remote location through sftp
    """
    def extract(self, arg):
        """
        Download the file from sftp location and decorate the commands and return
        :param arg: input string
        :return: generated object of all commands
        """
        remote_path = self.get_file_name_from_arg(arg)
        local_path = "/tmp/input_file.txt"
        with pysftp.Connection(host=SFTP_HOST, username=SFTP_USER, password=SFTP_PASSWORD) as sftp:
            sftp.get(remote_path, local_path)

        return self.get_commands_from_file(local_path)
