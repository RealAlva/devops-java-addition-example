from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar el navegador
driver = webdriver.Chrome()
driver.get("http://example.com")  # Cambia esta URL a la de la aplicación que deseas probar

# Ejemplo de prueba
print("Página cargada:", driver.title)

# Cerrar el navegador
driver.quit()
