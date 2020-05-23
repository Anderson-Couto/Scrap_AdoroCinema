from selenium import webdriver
from bs4 import BeautifulSoup as bs
from dao import salvar_nome_desc, desconectar_banco


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
            nome_filme = self.page_desc.find('div', {'class': 'titlebar-title titlebar-title-lg'}).text
            nome_filme = nome_filme.strip().title()
            descricao_filme = self.page_desc.find('div', {'class': 'content-txt'}).text
            descricao_filme = descricao_filme.strip()
            salvar_nome_desc(nome_filme, descricao_filme)


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
