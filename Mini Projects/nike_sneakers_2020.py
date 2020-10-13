import os
import time
import sys
import datetime

import pandas as pd
import csv
import logging.config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

seconds = time.time()
time_result = time.localtime(seconds)
path = 'C:/Users/ghodg/desktop'

# Set the path and selenium options
os.chdir(path)
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('browser.helperApps.alwaysAsk.force', False)
profile.set_preference('browser.download.manager.alertOnEXEOpen', False)
profile.set_preference('browser.download.manager.focusWhenStarting', False)

# Logging configuration
logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [PID %(process)d] [Thread %(thread)d] [%(levelname)s] [%(name)s] %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
            "stream": "ext://sys.stdout"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": [
            "console"
        ]
    }
})


# Firefox options for a headless browser to run
options = Options()
driver = webdriver.Firefox(profile, options=options)
nike_site = 'https://www.nike.com/us/en_us/'
actions = ActionChains(driver)

time.sleep(1)
driver.get(nike_site)
logger = logging.getLogger()

driver.maximize_window()
driver.set_page_load_timeout(page_load_timeout)



