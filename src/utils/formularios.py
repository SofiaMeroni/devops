from selenium.webdriver.common.by import By

def llenado_de_formulario(driver, value, input):
    input_text_fname = driver.find_element(By.NAME, value)
    input_text_fname.send_keys(input)
