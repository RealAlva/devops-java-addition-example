from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("file:///home/daniel/devops-java-addition-example/src/test/resources/addition_test.html")  # Ruta local del archivo HTML

input1 = driver.find_element(By.ID, "num1")
input2 = driver.find_element(By.ID, "num2")
submit = driver.find_element(By.ID, "submit")

input1.send_keys("5")
input2.send_keys("7")
submit.click()

result = driver.find_element(By.ID, "result").text
assert result == "La suma es: 12", "Test fallido: Resultado incorrecto"

driver.quit()
