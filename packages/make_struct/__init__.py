import os

class MakeStruct:
    struct = set()
    rootDir = None

    def __init__(self, struct):
        self.struct = struct
        self.root_dir = os.getcwd()

    def run(self):
        struct_json = self.struct
        for struct in struct_json:
            path_mass = struct_json[struct].split('.')
            half_path = os.path.join(*path_mass)
            full_path = os.path.join(self.root_dir, half_path)
            self.make_folder(full_path)

    def make_folder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)