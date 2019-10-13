from loader import *
from constants import LOADER_TYPE


class LoaderType:
    """
    To choose the Loader type
    """
    class_type = {
        "STDOUT": StdoutLoader,
        "file": FileLoader
    }

    @classmethod
    def loader_type(cls):
        """
        Find out the loader type object from class_type dict
        :return: Loader class type object
        """
        return cls.class_type[LOADER_TYPE]()
