import os
import datetime

class Logger:
    rootDir = None
    log_file = None

    def __init__(self, log_file):
        self.root_dir = os.getcwd()
        self.log_file = log_file

    def _show_time(self):
        now = datetime.datetime.now()
        result = now.strftime("%d.%m.%Y %H:%M:%S")
        return result

    def _show_info(self, text):
        result = self._show_time() + ' - ' + text
        return result

    def show(self, text):
        text = self._show_info(text)
        print(text)

    def _save(self, text):
        file_log = self.log_file

        my_file = open(file_log, "a")
        my_file.write(text + '\n')
        my_file.close()

    def save(self, text):
        text = self._show_info(text)
        self._save(text)

    def save_show(self, text):
        text = self._show_info(text)
        self._save(text)
        print(text)