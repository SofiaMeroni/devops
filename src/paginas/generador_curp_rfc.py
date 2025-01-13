from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from src.utils.formularios import llenado_de_formulario
import uuid
import random
import time
import json
import os

def curp_rfc(driver):
    # Navegar a la página
    urlbase = 'https://datafakegenerator.com/genrfc'
    driver.get(urlbase)
    time.sleep(5)
    
    Registro = 'prueba_' + str( uuid.uuid4() )
    
    llenado_de_formulario(driver, 'nombre', Registro)
    llenado_de_formulario(driver, 'paterno', Registro)
    llenado_de_formulario(driver, 'materno', Registro)  
   
    dia = [str(dia) for dia in range(1, 32)]
    mes = [str(mes) for mes in range(1, 13)]
    anio = [str(anio) for anio in range(1920, 2014)]
    
    Select(driver.find_element(By.NAME,'dia')).select_by_visible_text(random.choice(dia))
    Select(driver.find_element(By.NAME,'mes')).select_by_visible_text(random.choice(mes))
    Select(driver.find_element(By.NAME,'anio')).select_by_visible_text(random.choice(anio))
    
    estado = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche']
    Select(driver.find_element(By.NAME,'estado')).select_by_visible_text(random.choice(estado))
    
    sexo = ['Male', 'Female']
    Select(driver.find_element(By.NAME,'sexo')).select_by_visible_text(random.choice(sexo))
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/form/div[7]/button').click()
    time.sleep(6)
    
    curp = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[1]/p[6]')
    rfc = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[1]/p[5]')
    
    n_curp = curp.text
    n_rfc = rfc.text

    # Ruta al archivo JSON
    archivo_curps = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos', 'curps.json')
    os.makedirs(os.path.dirname(archivo_curps), exist_ok=True)

    # Leer el archivo JSON
    try:
        with open(archivo_curps, 'r') as file:
            datos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        datos = {"curps": []}

    # Agregar nuevo CURP
    datos.setdefault("curps", []).append(n_curp)

    # Guardar los datos actualizados
    with open(archivo_curps, 'w') as file:
        json.dump(datos, file, indent=4)

    print(f"CURP: {n_curp}, RFC: {n_rfc}")
    
    
    return (n_curp, n_rfc)
