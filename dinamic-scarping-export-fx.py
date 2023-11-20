from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

def extraer_textos_con_selenium(url):
    chrome_options = Options()
    chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)

    driver.get(url)
    time.sleep(10)

    datos = {'h1': [], 'h2': [], 'h3': [], 'h4': [], 'h5': [], 'h6': [], 'p': []}
    for etiqueta in datos.keys():
        elementos = driver.find_elements(By.XPATH, f'//{etiqueta}')
        for elemento in elementos:
            texto_elemento = elemento.text
            if texto_elemento:
                datos[etiqueta].append(texto_elemento)

    driver.quit()
    return datos

def exportar_a_excel(datos, nombre_archivo):
    with pd.ExcelWriter(nombre_archivo, engine='openpyxl') as writer:
        for etiqueta, textos in datos.items():
            df = pd.DataFrame(textos, columns=[etiqueta])
            df.to_excel(writer, sheet_name=etiqueta, index=False)

def main():
    url = input("Ingresa la URL: ")
    datos = extraer_textos_con_selenium(url)
    nombre_archivo = "textos_extraidos.xlsx"
    exportar_a_excel(datos, nombre_archivo)
    print(f"Los textos han sido exportados a {nombre_archivo}")

if __name__ == "__main__":
    main()
