import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global url

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(chrome_options = chrome_options)

driver.get("https://tuportal5.temple.edu")


def loginScreen():
	inputUsername = driver.find_element_by_id("username")
	inputPassword = driver.find_element_by_id("password")
	submitButton = driver.find_element_by_xpath('//*[@id="login-container"]/div[1]/form/div[6]/button')

	inputUsername.send_keys('')
	inputPassword.send_keys("")
	submitButton.click()

def homePage():
	studentPage = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layout_8"]/a'))) 
	studentPage.click()

	scrollLocation = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="portlet_56_INSTANCE_uxNsjIBwKCbn"]/header/h2/span[2]'))) 
	driver.execute_script("arguments[0].scrollIntoView()", scrollLocation)

	driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="iFrame_AppTupChannelsStudentRegistration"]'))
	
	activeReg = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="StudentRegistration_6"]')))

	activeReg.click()
	driver.implicitly_wait(4)


loginScreen()
homePage()

exit()