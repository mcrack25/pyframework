import os
from packages.config import Config
from packages.make_struct import MakeStruct
from packages.logger import Logger
from packages.dirs import Dirs
from packages.remover import Remover

# ПОДКЛЮЧАЕМ ВСЕ БИБЛИОТЕКИ ПРОЕКТА
# .......................

# ВПИСЫВАЕМ НАЗВАНИЕ ПРОГРАММЫ
program_name = 'ProgramName v1.0'

# ПОЛУЧАЕМ ВСЕ КОНФИГИ
config_struct = Config('struct').getAll()
config_app = Config('app').getAll()
config_env = Config().getEnv()

# ПОЛУЧАЕМ ВСЕ ПУТИ К ПАПКАМ
dir_logs = Dirs().get('logs')

# ПОЛУЧАЕМ ВСЕ ПУТИ К ФАЙЛАМ
log_file = os.path.join(dir_logs, config_app['log_file'])

# УДАЛЯЕМ НЕНУЖНЫЕ, СТАРЫЕ ФАЙЛЫ
del_files = [
    log_file,
]
Remover().remove_files(del_files)

if(__name__ == "__main__"):
    # Создаём структуру папок для работы
    MakeStruct(config_struct).run()

    # Создаём объект логера
    logger = Logger(log_file)

    # Логируем запуск
    logger.save_show('Программа запущена!!!')
    # ****************** ТУТ ВЫПОЛНЯЕТСЯ ПРОГРАММА

    # СОЗДАЁМ ПЕРЕМЕННЫЕ ДЛЯ ПРОГРАММЫ С ЗАЩИЩЁННЫМИ ДЛЯ РАЗРАБОТКИ ДАННЫМИ
    if config_env['login']:
        login = config_env['login']
    else:
        login = config_app['login']
    if config_env['password']:
        password = config_env['password']
    else:
        password = config_app['password']






    # ****************** ТУТ ВЫПОЛНЯЕТСЯ ПРОГРАММА
    logger.save_show('Программа выполнена!!!')
    print('')
    print('***')
    print('Название программы: ' + program_name)
    print('Разработка: Министерства труда и социального развития РД')
    print('Разработчик: Ахмедов Мурад Алилович')
    print('***')
    print('')
    input('Нажмите любую клавишу, для завершения работы программы')