import os


SFTP_HOST = os.environ.get("SFTP_HOST", "")
SFTP_USER = os.environ.get("SFTP_USER", "")
SFTP_PASSWORD = os.environ.get("SFTP_PASSWORD", "")
S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY", "")
S3_SECRET_KEY = os.environ.get("S3_SECRET_KEY", "")
LOADER_TYPE = os.environ.get("LOADER_TYPE", "STDOUT")
LOADER_FILE = os.environ.get("LOADER_FILE", "/tmp/output.txt")