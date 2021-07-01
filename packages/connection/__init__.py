import os
from peewee import *

class Connection:
    db = None
    db_type = ''
    db_user = ''
    db_password = ''
    db_name = ''
    db_host = ''
    db_port = ''

    def __init__(self, config):
        params = [
            'db_type',
            'db_user',
            'db_password',
            'db_name',
            'db_host',
            'db_port'
        ]
        self._set_or_null(config, params)

    def getDb(self):
        if self.db != None:
            return self.db
        else:
            self._select_db()
            return self.db

    def _set_or_null(self, config, params):
        for param in params:
            try:
                if config[param]:
                    setattr(self, param, config[param])
            except:
                pass

    def _select_db(self):
        if (self.db_type == 'mysql'):
            self.db = MySQLDatabase(self.db_name, user=self.db_user, password=self.db_password,host=self.db_host, port=self.db_port)
        elif(self.db_type == 'postgres'):
            self.db = PostgresqlDatabase(self.db_name, user=self.db_user, password=self.db_password, host=self.db_host, port=self.db_port)
        elif(self.db_type == 'sqlite'):
            root_dir = os.getcwd()
            db_path = os.path.join(root_dir, 'databases', self.db_name)
            if os.path.exists(db_path):
                self.db = SqliteDatabase(db_path)
            else:
                print('Ошибка!!! База данных SQLite не найдена по следующему пути:', db_path)
                exit()
        else:
            print('Ошибка!!! Не верный тип базы данных')
            exit()