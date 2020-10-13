import os
import time
import datetime

import pandas as pd
import csv
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

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


# Firefox options for a headless browser to run
options = Options()
driver = webdriver.Firefox(profile, options=options)
topps_site = 'https://www.topps.com/cards-collectibles/online-brands/project-2020.html'
actions = ActionChains(driver)

time.sleep(1)
driver.get(topps_site)
time.sleep(0.25)
iframes = driver.find_elements_by_xpath('//iframe')
driver.switch_to.frame(iframes[0])
WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[3]/span[1]"))).click()

slider = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]")
slider_container = driver.find_element_by_css_selector(".geetest_wrap")

width = slider.get_attribute("style")

actions.move_to_element(slider).click_and_hold().move_by_offset(80, 0).release().perform()
actions.move_to_element(slider).click_and_hold().move_by_offset(slider_container.size['width'] / 3, 0).release().perform()
actions.click_and_hold(slider).move_by_offset(xoffset=80, yoffset=0).release().perform()
actions.click_and_hold(slider).perform()


agent = driver.execute_script("return navigator.userAgent")
profile.set_preference("general.useragent.override", userAgent)



from fake_useragent import UserAgent
ua = UserAgent()
userAgent = ua.random



