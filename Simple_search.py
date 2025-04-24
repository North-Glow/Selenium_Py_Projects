from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window() # Modo de pantalla completa

driver.get('https://www.google.com/')

driver.implicitly_wait(10) # Pausar la prueba durante 10 segundos o hasta que carge la pagina

driver.find_element(By.TAG_NAME, "textarea").send_keys("Python")
driver.find_element(By.TAG_NAME, "textarea").clear()
driver.find_element(By.TAG_NAME, "textarea").send_keys("Selenium")
driver.find_element(By.TAG_NAME, "textarea").submit()

assert 'google.com' in driver.current_url

driver.quit()
