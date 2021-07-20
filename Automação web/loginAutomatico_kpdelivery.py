from selenium import webdriver
import pyautogui
import time

navegador = webdriver.Chrome()

navegador.get("https://kpdelivery.com.br/")
time.sleep(3)
navegador.find_element_by_xpath('//*[@id="UserName"]').send_keys("afsilva")
navegador.find_element_by_xpath('//*[@id="Password"]').send_keys("Teste1")
time.sleep(5)
navegador.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[4]/div/button').click()
