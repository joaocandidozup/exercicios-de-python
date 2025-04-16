
class Transacao:
    def __init__(self, descricao, valor, categoria, data):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = data

    def resumo(self):
        if self.valor > 0:
            sinal = "+"
        else:
           sinal = "-"
        return f"{self.descricao} | {sinal}{abs(self.valor)} | {self.categoria} | {self.data}"

