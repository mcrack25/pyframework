import os
import time
from packages.config import Config
from packages.make_struct import MakeStruct
from packages.logger import Logger
from packages.dirs import Dirs
from packages.remover import Remover

# Подключаем библиотеки проекта
from packages.selenium_get_driver import GetDriver
from selenium.webdriver.support.ui import Select
from app.controllers.FilesController import FilesController
from app.controllers.XlsxController import XlsxController

# Вписываем название программы
program_name = 'openSite v1.0'

# Получаем все конфиги
config_struct = Config('struct').getAll()
config_app = Config('app').getAll()
config_env = Config().getEnv()

# Получаем нужные пути к папкам
dir_logs = Dirs().get('logs')
dir_drivers = Dirs().get('drivers')

# Создаём переменные для программы
if config_env['login']:
    login = config_env['login']
else:
    login = config_app['login']

if config_env['password']:
    password = config_env['password']
else:
    password = config_app['password']

# Получаем нужные пути к файлам
log_file = os.path.join(dir_logs, config_app['log_file'])
log_file_snilses = os.path.join(dir_logs, 'snilses.txt')
driver_file = os.path.join(dir_drivers, config_app['driver_file'])

# Удаляем ненужные файлы
del_files = [
    log_file,
    log_file_snilses
]
Remover().remove_files(del_files)

def waitElement(driver, element, typeElement = 'id'):
    hasElement = False
    while hasElement == False:
        try:
            if typeElement == 'id':
                driver.find_element_by_id(element)
            hasElement = True
        except:
            logger.save_show('Элемент ' + str(element) + ' не найден, ждём 1 секунду')
            time.sleep(1)

def openURL(driver, url):
    success = False
    while success == False:
        try:
            driver.get(url)
            success = True
        except:
            logger.save_show('Не удалось открыть URL, ждём 1 секунду')
            time.sleep(1)


# functions
def doLogin(driver, login, password):
    logger.save_show('Входим в систему')
    waitElement(driver, 'tbLogin')

    tbLogin = driver.find_element_by_id('tbLogin')
    tbPassw = driver.find_element_by_id('tbPassw')
    btnLogin = driver.find_element_by_id('btnLogin')

    # Очищаем введённое значение
    tbLogin.clear()
    tbPassw.clear()

    # Вводим значение в поле поиска
    tbLogin.send_keys(login)
    tbPassw.send_keys(password)

    # Кликаем Войти
    logger.save_show('Входим в систему')
    btnLogin.click()

def goToPGU(driver):
    logger.save_show('Переходим в раздел ПГУ')
    waitElement(driver, 'ml_PGU')
    ml_PGU = driver.find_element_by_id('ml_PGU')
    ml_PGU.click()

def goToTiketsPGU(driver):
    logger.save_show('Переходим в раздел заявки с ПГУ')
    waitElement(driver, 'mr_REQUEST')
    mr_REQUEST = driver.find_element_by_id('mr_REQUEST')
    mr_REQUEST.click()

def deleteFilter(driver):
    logger.save_show('Удаляем фильтр если есть')
    try:
        ESERVICE_REQUEST77_cancelfilter = driver.find_element_by_id('ESERVICE_REQUEST77_cancelfilter')
        ESERVICE_REQUEST77_cancelfilter.click()
    except:
        pass

def openFilter(driver):
    logger.save_show('Открываем новый фильтр')
    waitElement(driver, 'ESERVICE_REQUEST77_filter')
    ESERVICE_REQUEST77_filter = driver.find_element_by_id('ESERVICE_REQUEST77_filter')
    ESERVICE_REQUEST77_filter.click()

def setSnilsNumber(driver, number):
    logger.save_show('Вставляем СНИЛС заявителя: ' + str(number))
    logger_snilses.save(str(number))

    waitElement(driver, 'Filt1_filt_SNILS')

    Filt1_filt_REQUESTID = driver.find_element_by_id('Filt1_filt_SNILS')
    Filt1_filt_REQUESTID.clear()
    Filt1_filt_REQUESTID.send_keys(str(number))

def setSnilsAccuracy(driver):
    logger.save_show('Указываем точность поиска: совпадает')
    waitElement(driver, 'Filt1_filtZnak_REQUESTID')
    Filt1_filtZnak_REQUESTID = Select(driver.find_element_by_id('Filt1_filtZnak_SNILS'))
    Filt1_filtZnak_REQUESTID.select_by_value('1')

def setServiceNumber(driver, number):
    logger.save_show('Вставляем код услуги: ' + str(number))
    waitElement(driver, 'Filt1_filt_ESERVICEID')
    Filt1_filt_ESERVICEID = driver.find_element_by_id('Filt1_filt_ESERVICEID')
    Filt1_filt_ESERVICEID.clear()
    Filt1_filt_ESERVICEID.send_keys(str(number))

def setServiceAccuracy(driver):
    logger.save_show('Указываем точность поиска: совпадает')
    waitElement(driver, 'Filt1_filtZnak_ESERVICEID')
    Filt1_filtZnak_ESERVICEID = Select(driver.find_element_by_id('Filt1_filtZnak_ESERVICEID'))
    Filt1_filtZnak_ESERVICEID.select_by_value('1')

def setServiceNot(driver):
    logger.save_show('Выставляем отрицание для кода услуги')
    waitElement(driver, 'Filt1_filtNOT_ESERVICEID')
    el = driver.find_element_by_xpath("//input[@id='Filt1_filtNOT_ESERVICEID']/following-sibling::span")
    el.click()

def applyFilter(driver):
    logger.save_show('Применяем фильтр')
    waitElement(driver, 'Filt1_lbApplyFilt')
    Filt1_lbApplyFilt = driver.find_element_by_id('Filt1_lbApplyFilt')
    Filt1_lbApplyFilt.click()

if(__name__ == "__main__"):
    # Создаём структуру папок для работы
    MakeStruct(config_struct).run()

    # Создаём объект логера
    logger = Logger(log_file)
    logger_snilses = Logger(log_file_snilses)

    # Логируем
    logger.save_show('Программа запущена!!!')


    # ТУТ ВЫПОЛНЯЕТСЯ ПРОГРАММА

    # Получаем список всех файлов в папке XLSX
    dir_xlsx = Dirs().get('xlsx')
    filesXlsx = FilesController().setDir(dir_xlsx).getFilesPath()

    url = config_app['url']
    url_list = url + config_app['uri_list']
    # Получаем драйвер Selenium
    driver = GetDriver(driver_file, config_app['browser']).get()

    # Открываем url
    openURL(driver, url)

    # Логинемся в системе
    doLogin(driver, login, password)

    # Переходим в раздел ПГУ
    goToPGU(driver)

    # Переходим в раздел Заявки с ПГУ
    goToTiketsPGU(driver)

    for fileXlsx in filesXlsx:
        rows = XlsxController(fileXlsx, 3, 'C', 'E').getData()
        for row in rows:

            # Открываем url списка
            openURL(driver, url_list)

            # Удаляем фильтр
            deleteFilter(driver)

            # Открываем фильтр
            openFilter(driver)

            # Вставляем номер заявления
            setSnilsNumber(driver, row['snils'])
            # Устанавливаем точность поиска - совпадает
            setSnilsAccuracy(driver)

            # Вставляем код услуги, который не хотим видеть
            setServiceNumber(driver, 'familychildsub')
            # Устанавливаем точность поиска - совпадает
            setServiceAccuracy(driver)
            # Выставляем отрицание
            setServiceNot(driver)

            # Применяем фильтр
            applyFilter(driver)

            # Получаем всех людей, которые подходят под результаты фильтрации
            logger.save_show('Получаем список всех людей по фильтру')
            grd_ESERVICE_REQUEST = driver.find_element_by_id('grd_ESERVICE_REQUEST')
            grd_ESERVICE_REQUEST_list = grd_ESERVICE_REQUEST.find_elements_by_class_name('normal')

            row_ids = []
            for grd_ESERVICE_REQUEST_one_r in grd_ESERVICE_REQUEST_list:
                row_id = grd_ESERVICE_REQUEST_one_r.get_attribute('id')
                row_ids.append(row_id)

            for row_id in row_ids:
                logger.save_show('Переходим к одному заявлению')
                grd_ESERVICE_REQUEST_one = driver.find_element_by_id(row_id)

                # Определяем ID строки
                id = grd_ESERVICE_REQUEST_one.get_attribute('id')
                id_mass = id.split('_')
                id_number = id_mass[-1]

                # Находим все установленные статусы ПГУ
                # Если в статусах нет статуса исполненно или отказ, тогда продолжаем выполнение программы, иначе пропускаем
                has_statuses = grd_ESERVICE_REQUEST_one.find_elements_by_class_name('ATN-bl-item')
                has_status = False
                for one_status in has_statuses:
                    if 'Исполнено' in one_status.text:
                        has_status = True
                    elif 'Отказ' in one_status.text:
                        has_status = True
                if has_status:
                    continue

                # Находим флаг и кликаем по нему
                logger.save_show('Находим флаг и кликаем по нему')
                flag_id = 'lbActionRow_ESERVICE_REQUEST77_' + str(id_number)
                flag = driver.find_element_by_id(flag_id)
                flag.click()
                time.sleep(1)

                # Получаем все статусы
                popup_str = 'tbActionRow_ESERVICE_REQUEST77_' + str(id_number)
                popup = driver.find_element_by_id(popup_str)
                links = popup.find_elements_by_tag_name('a')

                # Переводим статус из xlsx файла в число
                status = 0
                if row['status'] == 'Назначить выплату':
                    status = 1
                elif row['status'] == 'Отказать в выплате':
                    status = 2

                if status != 0:
                    if status == 1:
                        for link in links:
                            try:
                                if 'Ответить положительно' in link.text:
                                    link.click()
                                    time.sleep(1)
                            except:
                                pass

                        waitElement(driver, 'popupLBClose')
                        close_btn_success = driver.find_element_by_id('popupLBClose')
                        try:
                            close_btn_success.click()
                            flag.click()
                        except:
                            pass

                    elif status == 2:
                        for link in links:
                            try:
                                if 'Ответить отказом' in link.text:
                                    link.click()
                                    time.sleep(1)
                            except:
                                pass

                        waitElement(driver, 'popupLBClose')
                        close_btn_success = driver.find_element_by_id('popupLBClose')
                        try:
                            close_btn_success.click()
                            flag.click()
                        except:
                            pass

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