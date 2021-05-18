#!/usr/bin/python3

import wget
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
#import eventlet


def crawl(paginas, profundidade):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #eventlet.monkey_patch()
    contadorPDFs = 0
    contadorpaginas = 0
    for i in range(profundidade):
        novas_paginas = set()
        for pagina in paginas:
            http = urllib3.PoolManager()
            try:
                #with eventlet.Timeout(15):
                dados_pagina = http.request('GET', pagina)
            except:
                print("Erro ao abrir a página " + pagina)
                continue

            sopa = BeautifulSoup(dados_pagina.data, "lxml")
            links = sopa.find_all('a')

            for link in links:
                if('href' in link.attrs):
                    url = urljoin(pagina, str(link.get('href')))
                    if url.find("'") != -1:
                        continue
                    url = url.split('#')[0]
                    url = url.strip()
                    if url.lower().endswith("pdf"):
                        contadorPDFs += 1
                        try:
                            wget.download(url)
                        except:
                            print("ERRO AO FAZER O DOWNLOAD DO ARQUIVO " + url)
                            continue

                    if url[0:4].lower() == "http":
                        novas_paginas.add(url)
                        contadorpaginas += 1
            paginas = novas_paginas
            print("Quantidade de páginas encontradas: " + str(contadorpaginas))
            print ("Quantidade de PDFs encontrados: " + str(contadorPDFs))

listapaginas = []

if os.path.isfile("dominios.txt"):
    arquivo = open("dominios.txt", 'r')
    for dominio in arquivo.readlines():
        listapaginas.append(str(dominio))
    arquivo.close()
    crawl(listapaginas, 2)
else:
    print("Arquivo com os domínios não encontrado!")

