import requests

def obtener_html(url):
    """
    Obtiene el HTML de la página web especificada.
    
    :param url: URL de la página web.
    :return: HTML de la página como una cadena de texto.
    """
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Esto asegurará que se lance una excepción para respuestas HTTP no exitosas
        return respuesta.text
    except requests.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Otro error: {err}")

def main():
    url = input("Ingresa la URL de la página web: ")
    html = obtener_html(url)
    if html:
        print("\nContenido HTML de la página:")
        print(html)

if __name__ == "__main__":
    main()
