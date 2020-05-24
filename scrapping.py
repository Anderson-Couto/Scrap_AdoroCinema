from selenium import webdriver
from bs4 import BeautifulSoup as bs
from dao import salvar, desconectar_banco
from classe_duracao import Duracao
import re


class AdoroCinema:
    def __init__(self, driver):
        self.driver = driver
        self.end_base = "http://www.adorocinema.com/"
        self.end_Mfil = f'{self.end_base}/filmes/todos-filmes/notas-espectadores/'

    def navegar(self):
        self.driver.get(self.end_Mfil)
        self.obj_AC = bs(self.driver.page_source, 'html.parser')

    def encontrar_obj(self):
        self.filmes = self.obj_AC.find_all('div', {'class': 'data_box'})
        self.compl_filme = [link_desc.find('a').get('href') for link_desc in self.filmes]
        self.links_completos = [f'{self.end_base}{i}' for i in self.compl_filme]

    def raspagem(self):
        for j in self.links_completos:
            self.driver.get(j)
            self.page_desc = bs(self.driver.page_source, 'html.parser')

            # Nome do Filme
            nome_filme = self.page_desc.find('div', {'class': 'titlebar-title titlebar-title-lg'}).text
            nome_filme = nome_filme.strip().title()

            # Descriçao do Filme
            descricao_filme = self.page_desc.find('div', {'class': 'content-txt'}).text
            descricao_filme = descricao_filme.strip()

            # Div das informações
            infos = self.page_desc.find('div', {'class': 'meta-body-item meta-body-info'})

            # Data de Lançamento
            lancamento = infos.find('a', {'class': 'xXx date blue-link'}).text.strip()

            # Duração do Filme
            duracao = re.search("[\d]{0,9}h [\d]{0,9}min", str(infos)).group()
            duracao = Duracao(duracao)

            # Categorias do Filme
            todos_dados = infos.find_all('a', {'class': 'xXx'})
            lista = [str(objeto.contents[0]).strip() for objeto in todos_dados]
            categorias = '/'.join(lista[1:])

            salvar(nome_filme, lancamento, duracao, categorias, descricao_filme)


"""
    def passa_pagina(self):
        v = self.obj_AC.find('a', {'class': '"xXx button btn-default btn-large fr"'}).get('href')
        self.end_Mfil = f'{self.end_base}{v}'
        if v != 0:
            return True
"""

ff = webdriver.Firefox()
g = AdoroCinema(ff)
g.navegar()
g.encontrar_obj()
g.raspagem()
"""
g.passa_pagina()
while g.passa_pagina():
    g.navegar()
    g.encontrar_obj()
    g.raspagem()
    g.passa_pagina()
"""
ff.quit()
desconectar_banco()
