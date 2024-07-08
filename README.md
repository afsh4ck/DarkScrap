# DarkScrap
![image](https://github.com/afsh4ck/DarkScrap/assets/132138425/3517d58c-5dd2-471f-89d3-6a6c0a0fb287)

## Descripción
Este programa es una herramienta de código abierto diseñada para realizar operaciones de scraping y descarga de medios desde un onion link en la deep web de manera automatizada. Utiliza la red Tor para asegurar la privacidad y el anonimato durante las operaciones de scraping, garantizando que las solicitudes sean enrutadas de forma anónima a través de nodos Tor.

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

```bash
sudo apt update
sudo apt install tor
sudo service tor start
sudo service tor status
```

## Características
* **Descarga de Medios**: Descarga todos los archivos multimedia desde una página web.
* **Crawling desde URL Única**: Obtén enlaces, comentarios y media desde una única URL.
* **Reconocimiento Facial**: Reconoce rostros en imágenes obtenidas.
* **Crawling desde Archivos**:
  - **Txt**: Crawling desde un archivo de texto con múltiples URLs.
  - **Csv**: Crawling desde un archivo CSV con múltiples URLs.
  - **Excel**: Crawling desde un archivo Excel con múltiples URLs.
  
## Autor
@afsh4ck

## Inspiración:
Este programa está basado en el programa original <a href="https://github.com/itsmehacker/DarkScrape/tree/master" target=_blanc>Dark Scrape</a>, añadiendo nueva funcionalidades y mejoras.
