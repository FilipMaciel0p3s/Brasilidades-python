from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formato_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]

        mes_cadastro = self.momento_cadastro.month - 1
        print( mes_cadastro)
        return meses_do_ano[mes_cadastro]

    def semana_cadastro(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def formato_data(self):
        formato_date = self.momento_cadastro.strftime("%d/%m/%Y  %H:%M")
        return  formato_date

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days= 30)) - self.momento_cadastro
        return tempo_cadastro