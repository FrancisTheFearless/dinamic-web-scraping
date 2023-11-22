import requests
from bs4 import BeautifulSoup
import csv

def extraer_textos(url, etiquetas):
    """
    Extrae textos de las etiquetas especificadas de la página web dada.
    :param url: URL de la página web.
    :param etiquetas: Lista de etiquetas para extraer textos.
    :return: Lista de textos.
    """
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        raise Exception(f"Error al acceder a la página: {url}")

    soup = BeautifulSoup(respuesta.text, 'html.parser')
    textos = []
    for etiqueta in etiquetas:
        for elemento in soup.find_all(etiqueta):
            texto = elemento.get_text(strip=True)
            if texto:  # Asegurarse de que el texto no esté vacío
                textos.append(texto)
    return textos

def exportar_a_csv(datos, nombre_archivo):
    """
    Exporta los datos a un archivo CSV.
    :param datos: Lista de datos a exportar.
    :param nombre_archivo: Nombre del archivo CSV.
    """
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        for dato in datos:
            escritor.writerow([dato])

def main():
    url = input("Ingresa la URL: ")
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    etiquetas = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
    textos = extraer_textos(url, etiquetas)
    nombre_archivo = "textos_extraidos.csv"
    exportar_a_csv(textos, nombre_archivo)
    print(f"Los textos han sido exportados a {nombre_archivo}")

    # Imprimir los textos extraídos en pantalla
    print("\nTextos Extraídos:")
    for texto in textos:
        print(texto)

if __name__ == "__main__":
    main()
