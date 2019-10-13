from loader import *
from constants import LOADER_TYPE


class LoaderType:
    class_type = {
        "STDOUT": StdoutLoader,
        "file": FileLoader
    }

    @classmethod
    def loader_type(cls):
        return cls.class_type[LOADER_TYPE]()
