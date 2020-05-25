import datetime
import re


class Duracao:

    def __init__(self, string):
        self._string = string
        self.duracao = self._formatacao()

    def _tratamento(self):
        string = self._string.replace(" ", "")
        return string

    def _formatacao(self):
        str_tempo = self._tratamento()
        hora = int(str_tempo[:str_tempo.index("h")])
        minuto = int(str_tempo[str_tempo.index("h") + 1:str_tempo.index("min")])
        tempo = datetime.time(hour=hora, minute=minuto)
        return tempo

    def __str__(self):
        return str(self.duracao)


class Lancamento:

    def __init__(self, string):
        self._string = string
        self._meses = {
            'janeiro': "01",
            'fevereiro': "02",
            'março': '03',
            'abril': '04',
            'maio': '05',
            'junho': '06',
            'julho': '07',
            'agosto': '08',
            'setembro': '09',
            'outubro': '10',
            'novembro': '11',
            'dezembro': '12',
        }
        self.lancamento = self._formatacao()

    def _tratamento(self):
        if self._string is None:
            return "28/12/1895"

        retorno = "28121895"
        for chave, valor in self._meses.items():
            str_mes = re.search(chave, self._string)
            if str_mes is not None:
                retorno = self._string.replace(str_mes.group(), str(valor))
                retorno = re.sub(r"\D", "", retorno)

        r = list(retorno)
        if len(r) == 7:
            return f"0{r[0]}/{r[1]}{r[2]}/{r[3]}{r[4]}{r[5]}{r[6]}"
        elif len(r) == 8:
            return f"{r[0]}{r[1]}/{r[2]}{r[3]}/{r[4]}{r[5]}{r[6]}{r[7]}"
        else:
            return "28/12/1895"

    def _formatacao(self):
        data_format = self._tratamento()
        data_format = datetime.datetime.strptime(data_format, '%d/%m/%Y').date()
        return data_format

    def __str__(self):
        return str(self.lancamento)
