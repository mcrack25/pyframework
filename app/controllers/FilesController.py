import os

class FilesController():
    dir = set()
    files = []

    def setDir(self, dir):
        self.dir = dir
        return self

    def getFilesPath(self):
        for one_file in os.listdir(self.dir):
            fullPath = os.path.join(self.dir, one_file)
            self.files.append(fullPath)
        return self.files