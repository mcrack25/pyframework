import os
import os.path
import json

class Config:

    def __init__(self, fileName='app'):
        self.fileName = fileName + '.json'

    def getEnv(self):
        configs = []
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
        configFile = os.path.join(rootDir, 'config', self.fileName)
        if os.path.exists(configFile):
            try:
                with open(configFile, encoding='windows-1251') as file:
                    configs = json.load(file)
            except:
                pass
        return configs

    def get(self, param):
        rootDir = os.getcwd()
        configFile = os.path.join(rootDir, 'config', self.fileName)

        with open(configFile, encoding='windows-1251') as file:
            configs = json.load(file)
            if param in configs:
                value = configs[param]
                return value
        return ''