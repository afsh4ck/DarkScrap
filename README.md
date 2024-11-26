# DarkScrap
![image](https://github.com/afsh4ck/DarkScrap/assets/132138425/6cc8a80f-a5c9-4aa9-9717-25fbf49c5a87)


## Descripción
Este programa es una herramienta de código abierto diseñada para realizar operaciones de scraping y descarga de medios desde un onion link en la deep web de manera automatizada. Utiliza la red Tor para asegurar la privacidad y el anonimato durante las operaciones de scraping, garantizando que las solicitudes sean enrutadas de forma anónima a través de nodos Tor.
<br><br>
Todas las imágenes, documentos, links y comentarios del código fuente se almacenan en el directorio /Media, dentro de la carpeta con el nombre del site que hemos introducido.
<br><br>
![image](https://github.com/afsh4ck/DarkScrap/assets/132138425/feb79af5-3a3f-4009-bf68-7a345763bd60)

## Testeado en

* Kali Linux 2024.1
* Kali Nethunter
* Arc Linux

## Instalación

```bash
git clone https://github.com/afsh4ck/DarkScrap.git
pip3 install -r requirements.txt
python3 darkscrap.py
```
## Iniciar TOR
Es necesario iniciar TOR antes de ejecutar la herramienta de la siguiente manera:

```bash
sudo apt update
sudo apt install tor
sudo service tor start
sudo service tor status
```
## Video de la herramienta
https://youtu.be/SbdPsxYT_mU?si=gKIolbbuNXKMUycs

## Características
* **Descarga de Medios**: Descarga todos los archivos multimedia desde un Onion Link.
* **Scraping desde URL Única**: Obtén enlaces, comentarios y media desde una única URL.
* **Reconocimiento Facial**: Reconocimiento de rostros en imágenes obtenidas.
* **Scraping desde Archivos**:
  - **Txt**: Scraping desde un archivo de texto con múltiples URLs.
  - **Csv**: Scraping desde un archivo CSV con múltiples URLs.
  - **Excel**: Crawling desde un archivo Excel con múltiples URLs.
  
## Autor
- Autor:       afsh4ck
- Instagram:   <a href="https://www.instagram.com/afsh4ck">afsh4ck</a>
- Youtube:     <a href="https://youtube.com/@afsh4ck">afsh4ck</a>

## Inspiración:
Este programa está basado en el programa original <a href="https://github.com/itsmehacker/DarkScrape/tree/master" target=_blanc>Dark Scrape</a>, añadiendo nuevas funcionalidades y mejoras, cómo:
- La descarga automática de documentos e imágenes
- El scraping de links y comentarios del código fuente a un archivo de texto
- La creación de una carpeta con el nombre del site y mejor gestión de archivos
- Manejo de excepciones y mantenimiento

## Soporte

<a href="https://www.buymeacoffee.com/afsh4ck" rel="nofollow"><img width="250" align="left">
![buy-me-a-coffe](https://github.com/user-attachments/assets/8c8f9e81-334e-469e-b25e-29888cfc9fcc)
</a>
