import os

class Remover:

    def __init__(self):
        pass

    def remove_files(self, files):
        for file in files:
            self.remove_file(file)

    def remove_file(self, path):
        try:
           os.remove(path)
        except:
            pass