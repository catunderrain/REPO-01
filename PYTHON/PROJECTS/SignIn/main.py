
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from box import *
driver = webdriver.Chrome('python/projects/signin/chromedriver.exe')
driver.get('https://www.google.com/search?q=baso+thnah+nien&oq=baso+thnah+nien&aqs=chrome..69i57j0i13i131i433l2j0i13l7.2276j0j7&sourceid=chrome&ie=UTF-8')
driver.find_element_by_class_name('LC20lb MBeuO DKV0Md').click()
