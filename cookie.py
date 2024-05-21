from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service= service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(),'English')]")
language.click()

cookie_id = "bigCookie"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie_link = driver.find_element(By.ID, cookie_id)
#cookie_link.click()

for i in range(1000):
    cookie_link.click()



time.sleep(15)


driver.quit()