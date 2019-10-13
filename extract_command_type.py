from extractor import *


class ExtractCommandType:
    class_type = {
        "stdin": StdinExtractor,
        "s3": S3Extractor,
        "file": FileExtractor,
        "sftp": SFTPFileExtractor
    }

    @classmethod
    def extract_type(cls, argument):
        for key, value in cls.class_type.items():
            if argument.lower().startswith(key):
                return value()
