
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

class Carteira:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, transacao):
        self.transacoes.append(transacao)

    def exibir_transacoes(self):

        print("\n*** exibir transações ***")
        for transacao in self.transacoes:
            print(transacao.resumo())

    def saldo(self):
        return sum(transacao.valor for transacao in self.transacoes)

    def filtrar_por_categoria(self, categoria):
        print("\n*** filtrar por categoria ***")
        transacoes_filtradas = [
            transacao
            for transacao in self.transacoes
            if transacao.categoria == categoria
        ]

        if not transacoes_filtradas:

            print(f"Transações na categoria '{categoria}':")
        for transacao in transacoes_filtradas:
            print(transacao.resumo())

    def gastos_totais(self):
        total_gastos = 0
        for transacao in self.transacoes:
            if transacao.valor < 0:
                total_gastos += transacao.valor
        return total_gastos

    def renda_total(self):
        total_renda = 0
        for transacao in self.transacoes:
            if transacao.valor > 0:
                total_renda += transacao.valor
        return total_renda

    def resumo_geral(self):
        print("\n*** Resumo Geral ***")
        print(f"Total de transações: {len(self.transacoes)}")
        print(f"Renda total: R$ {self.renda_total():.2f}")
        print(f"Gastos totais: R$ {self.gastos_totais():.2f}")
        print(f"Saldo final: R$ {self.saldo():.2f}")


carteira = Carteira()

transacao1 = Transacao("Salário", 2500, "Renda", "1/04/2025")
transacao2 = Transacao("Mercado", -300, "Alimentação", "30/04/2025")
transacao3 = Transacao("Aluguel", -1200, "Moradia", "1/04/2025")
transacao4 = Transacao("Extra", 100, "Renda", "15/04/2025")
transacao5 = Transacao("Restaurante", -50, "Alimentação", "6/04/2025")


carteira.adicionar(transacao1)
carteira.adicionar(transacao2)
carteira.adicionar(transacao3)
carteira.adicionar(transacao4)
carteira.adicionar(transacao5)

carteira.exibir_transacoes()

carteira.filtrar_por_categoria("Alimentação")

carteira.resumo_geral()
