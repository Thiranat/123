import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service('C:\\webdriver\\chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("http://www.google.com/")
time.sleep(2)
driver.close()