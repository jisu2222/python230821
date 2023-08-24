# 셀리니움_웹드라이버.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time

driver = webdriver.Chrome()

driver.get('https://nid.naver.com/nidlogin.login')

loginID = "kim"
clipboard.copy(loginID)
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL,'v')                                                        

loginPW = "1234"
clipboard.copy(loginPW)
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL,'v')
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="log.login"]').click()

while True:
    pass