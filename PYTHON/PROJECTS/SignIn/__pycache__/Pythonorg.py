from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element_by_id('homepage')
search_bar.click()
print(driver.current_url)
