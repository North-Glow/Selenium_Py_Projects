from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10) # Pausar la prueba durante 10 segundos o hasta que se cargen todos los elementos requeridos

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Buscar elementos
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")

driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()

assert '/signin' in driver.current_url
# Probar el atributo placeholder para cada elemento
assert email.get_attribute('placeholder') == 'Correo electrónico', f"Expected 'Correo electrónico', but got '{email.get_attribute('placeholder')}'"
assert password.get_attribute('placeholder') == 'Contraseña', f"Expected 'Contraseña', but got '{password.get_attribute('placeholder')}'"
print("Pruebas exitosas!")

# Cerrar el navegador
driver.quit()
