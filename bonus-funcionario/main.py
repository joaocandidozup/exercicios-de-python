from funcionarios import FuncionarioComum, Gerente
from sistema_rh import SistemaRH

funcionario1 = FuncionarioComum("Carlos Silva", 1500.00)
gerente1 = Gerente("Ana Paula", 5000.00, 3200.00)

sistema_rh = SistemaRH()

print("\n--- Cálculo de Bônus ---")
sistema_rh.mostrar_bonus(funcionario1)
sistema_rh.mostrar_bonus(gerente1)

print("\n--- Acessando informações dos funcionários ---")
print(f"Nome do funcionário: {funcionario1.nome}, Salário: R$ {funcionario1.salario:.2f}")
print(f"Nome do gerente: {gerente1.nome}, Salário: R$ {gerente1.salario:.2f}, Bônus Adicional: R$ {gerente1.bonus_adicional:.2f}")

print("\n--- Tentativa de atualizar salário com valor inválido ---")
try:
    funcionario1.salario = -100
except ValueError as e:
    print(f"Erro ao atualizar salário: {e}")

funcionario1.salario = 2800.00
print("\n---Atualizando o salário ---")
print(f"Novo salário de {funcionario1.nome}: R$ {funcionario1.salario:.2f}")
sistema_rh.mostrar_bonus(funcionario1)
