from constants import LOADER_FILE


class Loader:
    """
    Loader base class
    """
    pass


class StdoutLoader(Loader):
    """
    Loader to standard output
    """
    def load(self, results):
        """
        Print on stdout
        :param results: results list
        :return: No return
        """
        for res in results:
            print(res)


class FileLoader(Loader):
    """
    Loader to provide output in a file
    """
    def load(self, results):
        """
        load to a file
        :param results: Results list
        :return: No return
        """
        with open(LOADER_FILE, 'w') as f:
            for res in results:
                f.write(str(res))
                f.write("\n")
