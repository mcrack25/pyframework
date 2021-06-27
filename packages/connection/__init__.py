import os
from peewee import *

class Connection:
    db = set()
    db_type = ''
    db_sqlite_path = ''
    db_user = ''
    db_password = ''
    db_name = ''
    db_host = ''
    db_port = ''

    def __init__(self, config):
        params = [
            'db_type',
            'db_sqlite_path',
            'db_user',
            'db_password',
            'db_name',
            'db_host',
            'db_port'
        ]
        self.set_or_null(config, params)

    def getDb(self):
        self.select_db()
        return self.db

    def set_or_null(self, config, params):
        for param in params:
            try:
                if config[param]:
                    setattr(self, param, config[param])
            except:
                pass

    def select_db(self):
        if (self.db_type == 'mysql'):
            self.db = MySQLDatabase(self.db_name, user=self.db_user, password=self.db_password,host=self.db_host, port=self.db_port)
        elif(self.db_type == 'postgres'):
            self.db = PostgresqlDatabase(self.db_name, user=self.db_user, password=self.db_password, host=self.db_host, port=self.db_port)
        elif(self.db_type == 'sqlite'):
            self.db = SqliteDatabase(self.db_sqlite_path)
        else:
            print('Ошибка!!! Не верный тип базы данных')
            exit()