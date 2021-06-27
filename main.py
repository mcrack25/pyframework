import os
from packages.config import Config
from packages.make_struct import MakeStruct
from packages.logger import Logger
from packages.dirs import Dirs
from packages.remover import Remover

# Подключаем библиотеки проекта
# .......................

# Вписываем название программы
program_name = 'ProgramName v1.0'

# Получаем все конфиги
config_struct = Config('struct').getAll()
config_app = Config('app').getAll()
config_env = Config().getEnv()

# Получаем нужные пути к папкам
dir_logs = Dirs().get('logs')

# Получаем нужные пути к файлам
log_file = os.path.join(dir_logs, config_app['log_file'])

# Удаляем ненужные файлы
del_files = [
    log_file,
]
Remover().remove_files(del_files)

# Создаём переменные для программы
if config_env['login']:
    login = config_env['login']
else:
    login = config_app['login']

if config_env['password']:
    password = config_env['password']
else:
    password = config_app['password']

if(__name__ == "__main__"):
    # Создаём структуру папок для работы
    MakeStruct(config_struct).run()

    # Создаём объект логера
    logger = Logger(log_file)

    # Логируем
    logger.save_show('Программа запущена!!!')

    # ТУТ ВЫПОЛНЯЕТСЯ ПРОГРАММА

    logger.save_show('Программа выполнена!!!')
    print('')
    print('***')
    print('Название программы: ' + program_name)
    print('Разработка: Министерства труда и социального развития РД')
    print('Разработчик: Ахмедов Мурад Алилович')
    print('***')
    print('')
    input('Нажмите любую клавишу, для завершения работы программы')