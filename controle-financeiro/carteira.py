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
