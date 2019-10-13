from extractor import *


class ExtractInputType:
    """
    Extract the Extractor class object by classifying the input type
    """
    class_type = {
        "stdin": StdinExtractor,
        "s3": S3Extractor,
        "file": FileExtractor,
        "sftp": SFTPFileExtractor
    }

    @classmethod
    def extract_type(cls, argument):
        """
        Extract from class_type dictionary, provide 4 options for now, which can be extended further
        :param argument: argument contains input string
        :return: Return Extractor class Object
        """
        for key, value in cls.class_type.items():
            if argument.lower().startswith(key):
                return value()
