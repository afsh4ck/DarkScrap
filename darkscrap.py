#!/usr/bin/env python3
import subprocess as subp
import requests
import os
from bs4 import BeautifulSoup, Comment
from urllib.parse import urljoin, urlparse

R = '\033[31m'  # rojo
G = '\033[32m'  # verde
C = '\033[36m'  # cian
W = '\033[0m'   # blanco

VERSION = '1.0'

def banner():
    banner = r'''                                                                                       

    ____                __   _____                         
   / __ \ ____ _ _____ / /__/ ___/ _____ _____ ____ _ ____ 
  / / / // __ `// ___// //_/\__ \ / ___// ___// __ `// __ \
 / /_/ // /_/ // /   / ,<  ___/ // /__ / /   / /_/ // /_/ /
/_____/ \__,_//_/   /_/|_|/____/ \___//_/    \__,_// .___/ 
                                                  /_/      
                                                                                        
'''
    print(G + banner + W)
    print(R + "Creado por: " + G + "afsh4ck" + W)
    print(R + "Sígueme en: " + G + "Instagram y Youtube" + W)
    print(R + "Versión: " + G + VERSION + W + '\n')

session = requests.session()
session.proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

def service():
    """
    Verifica que el servicio Tor esté en ejecución antes de continuar
    """
    print('\n' + C + "[>] Verificando servicio de Tor..." + W + '\n')
    cmd = 'systemctl is-active tor.service'
    co = subp.Popen(cmd, shell=True, stdout=subp.PIPE).communicate()[0]
    if 'inactive' in str(co):
        print(R + '[!] Servicio Tor no está en ejecución..' + W + '\n')
        print(R + '[>] Este script requiere que el servicio Tor esté activo...')
        exit()
    else:
        print(C + "[>] Servicio Tor está en ejecución..." + W + '\n')

def scrap():
    r = session.get("http://icanhazip.com").text.strip()
    print(R + '[+]' + G + ' Conectado a Tor...')
    print(R + '[+]' + G + ' Tu IP Tor -> {}'.format(r))

def parse_url():
    url = input(G + '[+]' + C + " Por favor ingresa la URL -> " + W)
    response = session.get(url)
    if response.status_code == 200:
        # Crear directorio con el nombre del sitio web
        parsed_url = urlparse(url)
        dir_name = parsed_url.netloc.replace(".", "_")
        media_dir = os.path.join("Media", dir_name)
        images_dir = os.path.join(media_dir, "Imágenes")  # Directorio para las imágenes
        os.makedirs(images_dir, exist_ok=True)  # Asegura que el directorio exista

        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraer todos los enlaces
        links = [urljoin(url, link['href']) for link in soup.find_all('a', href=True)]
        
        # Extraer todos los comentarios
        comments = [comment for comment in soup.find_all(string=lambda text: isinstance(text, Comment))]
        
        # Guardar enlaces y comentarios en un archivo de texto
        guardar_links_y_comentarios(links, comments, dir_name)

        # Descargar archivos multimedia si es necesario (en este caso, imágenes)
        urls_multimedia = [urljoin(url, img['src']) for img in soup.find_all('img')]
        for url_multimedia in urls_multimedia:
            nombre_archivo = url_multimedia.split('/')[-1]
            ruta_archivo = os.path.join(images_dir, nombre_archivo)
            respuesta_multimedia = session.get(url_multimedia)
            if respuesta_multimedia.status_code == 200:
                with open(ruta_archivo, 'wb') as archivo_multimedia:
                    archivo_multimedia.write(respuesta_multimedia.content)
                print(C + "[>] Descargado: " + W + url_multimedia)
            else:
                print(R + "[!] Error al descargar: " + W + url_multimedia)
    else:
        print(R + "[!] No se pudo acceder a la URL: " + W + url)

def guardar_links_y_comentarios(links, comentarios, nombre_directorio):
    nombre_archivo = os.path.join("Media", nombre_directorio, "links_y_comentarios.txt")
    
    # Eliminar duplicados de links y comentarios usando sets
    links = set(links)
    comentarios = set(comentarios)
    
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write("Links:\n")
        for link in links:
            f.write(link + '\n')
        f.write("\nComentarios:\n")
        for comentario in comentarios:
            f.write(comentario.strip() + '\n')
    
    print(C + "[>] Links y comentarios guardados en: " + W + nombre_archivo)

def main():
    """
    Presenta opciones para raspar desde una URL única o desde un tipo de archivo
    """
    choice = '0'
    while choice == '0':
        print(R + '[+] ' + G + 'Elige el formato de archivo:' + W)
        print(R + '[1] ' + G + 'Scrapping desde archivo' + W)
        print(R + '[2] ' + G + 'Scrapping desde URL única' + W + '\n')
        choice = input(G + '[+]' + C + " Ingresa el número de la opción ->  " + W)

        if choice == "1":
            elegir_archivo()
        elif choice == "2":
            parse_url()
        else:
            print('\n' + R + "[!] No comprendo tu elección." + W + '\n')
            return main()

try:
    banner()
    service()
    scrap()
    main()
except KeyboardInterrupt:
    print('\n' + R + '[!]' + R + ' Interrupción por teclado.' + W)
    exit()
