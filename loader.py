from constants import LOADER_FILE


class Loader:
    def __init__(self):
        pass


class StdoutLoader(Loader):
    def __init__(self):
        pass

    def load(self, results):
        for res in results:
            print(res)


class FileLoader(Loader):
    def __init__(self):
        pass

    def load(self, results):
        with open(LOADER_FILE, 'w') as f:
            for res in results:
                f.write(res)
