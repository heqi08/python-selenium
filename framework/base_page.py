import configparser
import os
import time

from selenium import webdriver

import getcwd
from logs.log import log1

path = getcwd.get_cwd()
config_path = os.path.join(path, 'config/config.ini')
rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def quit(self):
        self.driver.quite()
        log1.info('close browser')

    @staticmethod
    def config_get(section, option):
        # load config.ini and return
        config = configparser.ConfigParser()
        config.read(config_path, encoding="utf-8-sig")
        return config.get(section, option)

    def open_browser(self):
        url = self.config_get('amazon', 'url')
        log1.info('load url：%s' % url)
        driver = webdriver.Chrome()
        log1.info('Open chrome')
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        log1.info('sleep 10 seconds')
        return driver

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

