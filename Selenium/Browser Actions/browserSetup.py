from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serviceObject = Service("C:\Driver\chromedriver107.exe")

driver = webdriver.Chrome(service=serviceObject)




#-----make sure you have downloaded the existing chrome version in your pc-------