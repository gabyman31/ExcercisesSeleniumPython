from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome(executable_path="C:\DriverChrome\chromedriver")
driver.maximize_window()
driver.get("https://login.aol.com/account/create?lang=es-ES&src=oauth&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Frequest_auth%3Fresponse_type%3Dcode%26client_id%3DGzkftzubVdjySPGg%26redirect_uri%3Dhttps%253A%252F%252Flogin.yahoo.com%252Faccount%252Fchallenge%252Ftpa%252Fredirect%26scope%3Dopenid%2520sdpp-r%2520openid2%26ui_locales%3Des-ES%26state%3Dacrumb%253D0Xj35vqY%257Cactivity%253Duh-signin%257Cpspid%253D1185550002%257Csrc%253Dfinance%257CsessionIndex%253DQQ--%257Cdisplay%253Dlogin%257CauthMechanism%253Dprimary%257Cintl%253Des%257Clang%253Des-ES&specId=yidReg")

month=driver.find_element(By.ID,"usernamereg-month")
monthDD=Select(month)
ddlist=monthDD.options

monthDD.select_by_index(3)
time.sleep(2)
monthDD.select_by_value("6")
time.sleep(2)
monthDD.select_by_visible_text("Diciembre")
time.sleep(2)

#Usefull to know how many elements there are into a list
print(len(ddlist))
assert 13== len(ddlist)

for ele in ddlist:
    print("Value is ", ele.text)
    if ele.text=="Octubre":
       ele.click()
       time.sleep(3)
       break

#Usefull to know if an any specific vaue is by Default
ddefault=monthDD.first_selected_option
assert "Octubre"==ddefault.text

driver.quit()
