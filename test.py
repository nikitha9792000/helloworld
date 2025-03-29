from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

serv_obj=Service('C:\\Users\\ADMIN\\PycharmProjects\\sample proj\\Drivers\\chromedriver.exe')
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=serv_obj,options=options)

time.sleep(2)
driver.get("https://magento.softwaretestingboard.com/")
time.sleep(2)
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[3]/a").click()

driver.find_element(By.XPATH,"//*[@id='firstname']").send_keys("nikit")
driver.find_element(By.ID,"lastname").send_keys("palla")
driver.find_element(By.NAME,"email").send_keys("nikitha979200@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[title=Password]").send_keys("NIKI2000p")
driver.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[3]/div/input").send_keys("NIKI2000p")
driver.find_element(By.XPATH,"//*[@id='form-validate']/div/div[1]/button").click()
driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button").click()
driver.find_element(By.LINK_TEXT,"Sign Out").click()
driver.find_element(By.LINK_TEXT,"Sign In").click()
driver.find_element(By.NAME,"login[username]").send_keys("nikitha979200@gmail.com")
driver.find_element(By.ID,"pass").send_keys("NIKI2000p")
driver.find_element(By.XPATH,"//*[@id='send2']").click()
driver.close()

