
from selenium import webdriver
from box import *
username = un
password = pd

driver = webdriver.Chrome()
driver.get('https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fe-learning.hcmut.edu.vn%2Flogin%2Findex.php%3FauthCAS%3DCAS')
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_name('submit').click()

driver2 = webdriver.Chrome('chromedriver.exe')

driver2.get('https://mybk.hcmut.edu.vn/stinfo/')
driver2.find_element_by_id('username').send_keys(username)
driver2.find_element_by_id('password').send_keys(password)
driver2.find_element_by_name('submit').click()

driver3 = webdriver.Chrome('chromedriver.exe')

driver3.get('https://mybk.hcmut.edu.vn/app/')
driver3.find_element_by_id('username').send_keys(username)
driver3.find_element_by_id('password').send_keys(password)
driver3.find_element_by_name('submit').click()
