import os
import os.path
import json

class Config:
    file_name = ''
    file_name_full = ''
    configs = {}

    def __init__(self, file_name='app'):
        self.file_name = file_name
        self.file_name_full = file_name + '.json'

    def getData(self):
        configs = self.getAll()
        envs = self.getEnv()
        try:
            envs_mass = envs[self.file_name]
            for env in envs_mass:
                configs[env] = envs_mass[env]
        except:
            pass
        self.configs = configs
        return self.configs

    def getEnv(self):
        configs = {}
        rootDir = os.getcwd()
        configFile = os.path.join(rootDir, '.env')
        if os.path.exists(configFile):
            try:
                with open(configFile, encoding='windows-1251') as file:
                    configs = json.load(file)
            except:
                pass
        return configs

    def getAll(self):
        configs = []
        rootDir = os.getcwd()
        configFile = os.path.join(rootDir, 'config', self.file_name_full)
        if os.path.exists(configFile):
            try:
                with open(configFile, encoding='windows-1251') as file:
                    configs = json.load(file)
            except:
                pass
        return configs

    def get(self, param):
        rootDir = os.getcwd()
        configFile = os.path.join(rootDir, 'config', self.file_name_full)

        with open(configFile, encoding='windows-1251') as file:
            configs = json.load(file)
            if param in configs:
                value = configs[param]
                return value
        return ''