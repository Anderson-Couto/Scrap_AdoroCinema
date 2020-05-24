import datetime


class Duracao:

    def __init__(self, string):
        self._string = string

    def _tratamento(self):
        lista = list(self._string)
        while " " in lista:
            lista.remove(" ")
        lista = "".join(lista)
        return lista

    def _formatacao(self):
        string = self._tratamento()
        hora = int(string[:string.index("h")])
        minuto = int(string[string.index("h") + 1:string.index("min")])
        tempo = datetime.time(hour=hora, minute=minuto)
        return tempo

    def __str__(self):
        return str(self._formatacao())
