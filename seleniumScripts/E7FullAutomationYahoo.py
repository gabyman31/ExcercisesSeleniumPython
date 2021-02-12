from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\DriverChrome\chromedriver")
driver.maximize_window()
driver.get("https://login.aol.com/account/create?lang=es-ES&src=oauth&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Frequest_auth%3Fresponse_type%3Dcode%26client_id%3DGzkftzubVdjySPGg%26redirect_uri%3Dhttps%253A%252F%252Flogin.yahoo.com%252Faccount%252Fchallenge%252Ftpa%252Fredirect%26scope%3Dopenid%2520sdpp-r%2520openid2%26ui_locales%3Des-ES%26state%3Dacrumb%253D0Xj35vqY%257Cactivity%253Duh-signin%257Cpspid%253D1185550002%257Csrc%253Dfinance%257CsessionIndex%253DQQ--%257Cdisplay%253Dlogin%257CauthMechanism%253Dprimary%257Cintl%253Des%257Clang%253Des-ES&specId=yidReg")

name=driver.find_element(By.ID, "usernamereg-firstName").send_keys("Maria")
lastname=driver.find_element(By.ID, "usernamereg-lastName").send_keys("Hostal")
mail=driver.find_element(By.ID, "usernamereg-yid").send_keys("xqwouvvek")
driver.find_element(By.ID, "usernamereg-yid").send_keys(Keys.TAB)
password=driver.find_element(By.ID, "usernamereg-password").send_keys("Qwaszxrt*2010")

phone=driver.find_element(By.NAME, "shortCountryCode")
code=Select(phone)
code.select_by_value("PA")
driver.implicitly_wait(3)

number=driver.find_element(By.NAME, "phone").send_keys(65554444)

month=driver.find_element(By.ID,"usernamereg-month")
monthDD=Select(month)
monthDD.select_by_value("3")

day=driver.find_element(By.ID, "usernamereg-day").send_keys(23)
year=driver.find_element(By.NAME, "yyyy").send_keys(1985)

accep=driver.find_element(By.XPATH, "//button[@id='reg-submit-button']").click()

time.sleep(3)

driver.quit()






