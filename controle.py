from transacao import Transacao
from carteira import Carteira

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
