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
program_author = 'Ахмедов Мурад Алилович'

# ПОЛУЧАЕМ ВСЕ КОНФИГИ
config_struct = Config('struct').getData()
config_app = Config('app').getData()

# ПОЛУЧАЕМ ВСЕ ПУТИ К ПАПКАМ
dir_logs = Dirs().get('logs')

# ПОЛУЧАЕМ ВСЕ ПУТИ К ФАЙЛАМ
log_file = os.path.join(dir_logs, config_app['log_file'])

# УДАЛЯЕМ НЕНУЖНЫЕ, СТАРЫЕ ФАЙЛЫ
Remover().remove_files([
    log_file
])

# Создаём структуру папок для работы
MakeStruct(config_struct).run()

# Создаём объект логера
logger = Logger(log_file)

if(__name__ == "__main__"):
    # Логируем запуск
    logger.save_show('Программа запущена!!!')

    # ****************** ТУТ ВЫПОЛНЯЕТСЯ ПРОГРАММА ****************** #








    # ****************** ТУТ ВЫПОЛНЯЕТСЯ ПРОГРАММА ****************** #

    # Логируем завершение программы
    logger.save_show('Программа выполнена!!!')
    print('')
    print('***')
    print('Название программы: ' + program_name)
    print('Разработка: Министерства труда и социального развития РД')
    print('Разработчик: ' + program_author)
    print('***')
    print('')
    input('Нажмите любую клавишу, для завершения работы программы')