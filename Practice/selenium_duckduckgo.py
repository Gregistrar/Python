"""
Bandcamp Web Scraper - Using Selenium
=====================================
Python class that connects to bandcamp.com, streams music from the "discovery"
section and keeps track of the listening history in a CSV.
    - Today you will use a full-fledged browser running in headless mode to do
     the HTTP requests for you.

https://realpython.com/modern-web-automation-with-python-and-selenium/
"""

# from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

opts = Options()
opts.set_headless(headless=True)
assert opts.headless
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')

# After inspecting the page with dev tools, the search form <input> element has an 'id'
# attribute "search_form_input_homepage"
search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()

# The search form gets filled out and checks out the top result
results = browser.find_elements_by_class_name('result')
print(results[0].text)

browser.close()
quit()



