from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import pandas as pd

options = Options()
options.add_argument('--headless')  # Runs Chrome in headless mode.
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

url= 'https://acharts.co/france_singles_top_100'

chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
timeout = 40
browser = webdriver.Chrome(service=chromedriver, options=op)
browser.get(url)
delay = 1
# timeout = 40
try:
    WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/table/tbody')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
itembox = browser.find_elements(By.XPATH, '/html/body/div/div/div/main/div[2]/table/tbody/tr')
print(len(itembox))
for each in itembox:
    item_title= each.find_elements(By.XPATH, '/html/body/div/div/div/main/div[2]/table/tbody/tr/td[3]/a/span')
    print(item_title)
    item_artist= each.find_elements(By.XPATH,'/html/body/div/div/div/main/div[2]/table/tbody/tr/td[3]/span[2]/span/span')
    print(item_artist)
