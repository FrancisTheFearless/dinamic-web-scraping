<!DOCTYPE html>
<html>
<body>

<h1>README.md para el Proyecto de Web Scraping con Selenium y BeautifulSoup</h1>

<h2>Descripción del Proyecto</h2>
<p>Este proyecto de Python utiliza Selenium y BeautifulSoup para realizar scraping de contenido web dinámico. Está diseñado específicamente para interactuar con Google Finance, cerrar diálogos emergentes de políticas de privacidad y extraer información relevante de la página, como los valores de divisas.</p>

<h2>Características</h2>
<ul>
    <li><strong>Automatización de Navegadores Web</strong>: Utiliza Selenium para cargar y manipular páginas web que contienen contenido dinámico.</li>
    <li><strong>Manejo de Diálogos Emergentes</strong>: Cierra automáticamente los diálogos de políticas de privacidad que pueden interferir con el scraping.</li>
    <li><strong>Extracción de Datos</strong>: Emplea BeautifulSoup para analizar el HTML y extraer datos específicos.</li>
</ul>

<h2>Requisitos</h2>
<p>Para ejecutar este script, se requieren las siguientes herramientas y bibliotecas:</p>
<ul>
    <li>Python</li>
    <li>Selenium</li>
    <li>BeautifulSoup</li>
    <li>WebDriver para Chrome (chromedriver)</li>
</ul>

<h2>Instalación de Dependencias</h2>
<p>Instala las dependencias necesarias con el siguiente comando:</p>
<pre><code>pip install selenium beautifulsoup4</code></pre>
<p>Asegúrate de tener el WebDriver adecuado para tu versión de Chrome. Puedes descargarlo desde <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads">aquí</a>.</p>

<h2>Configuración</h2>
<p>Antes de ejecutar el script, asegúrate de configurar la ubicación del binario de Chrome y el path del WebDriver en el script. Modifica las siguientes líneas según tu configuración:</p>
<pre><code>chrome_options.binary_location = "TU_UBICACIÓN_DE_CHROME"
driver = webdriver.Chrome(executable_path='TU_PATH_A_CHROMEDRIVER', options=chrome_options)</code></pre>

<h2>Uso</h2>
<p>Para ejecutar el script, simplemente corre el archivo Python. El script abrirá automáticamente Chrome, accederá a Google Finance, cerrará cualquier diálogo de políticas de privacidad y extraerá los datos requeridos.</p>

<h2>Ejemplo de Uso</h2>
<pre><code>url = 'https://www.google.com/finance/quote/USD-CLP?sa=X&ved=2ahUKEwjwhsG-1NOCAxX5T6QEHbFABtEQmY0JegQIDhAr&window=MAX'
main()</code></pre>

<h2>Contribuciones</h2>
<p>Las contribuciones son bienvenidas. Si tienes sugerencias o mejoras, no dudes en crear un 'pull request' o abrir un 'issue' en el repositorio.</p>

</body>
</html>
