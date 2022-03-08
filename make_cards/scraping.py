import requests
from bs4 import BeautifulSoup
import re
import json

""" Obtiene una url y estrae los audios y los texto de las etiquetas que creemos que contienen los audios
    Crea un archivo Json a partir de esto
"""

# leer cualquier web
website = "https://leagueoflegends.fandom.com/wiki/Pantheon/LoL/Audio"
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')


# Obtenemos los audios y los textos en una lista
tags = soup.select('i, b , audio')
""" Extre las etiquetas que creemos que tiene el contenido importante"""
get_data = re.compile(r'(?<=src=").*?(?=")|(?<=>").*?(?="<)') #
""" extrae la url de las etiquetas y el texto de una etiqueta"""
resultado = get_data.findall(str(tags))

# Agregamos los textos y audios a un dict
lista = []
objeto = {}
for i in resultado:
    """ si es una url agrega 1 elemento a un dic luego agrega ese dict a la lista"""
    if i.startswith("http") == True:
        objeto = {"url": i}
    else:
        # text = re.sub(r'[^\w]', ' ', i.lower())
        # text = " ".join(re.split(r"\s+", text))
        objeto["text"] = i
        lista.insert(len(lista), objeto) 
        objeto.clear



card_name = "Pantheon"

# CREAR UN ARCHIVO CON LA INFORMACION
with open(f'{card_name}/{card_name}.json', "w") as outfile:
    json.dump(lista, outfile)
    