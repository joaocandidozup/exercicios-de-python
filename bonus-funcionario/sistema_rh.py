def logar_acao(func):
    def wrapper(sistema_rh_instance, funcionario, *args, **kwargs):
        bonus = func(sistema_rh_instance, funcionario, *args, **kwargs)
        print(f"LOG: Bônus de {funcionario.nome} calculado e exibido: R$ {bonus:.2f}")
        return bonus
    return wrapper

class SistemaRH:
    @logar_acao
    def mostrar_bonus(self, funcionario: 'Funcionario') -> float:
        bonus = funcionario.calcular_bonus()
        print(f"O bônus de {funcionario.nome} é de R$ {bonus:.2f}")
        return bonus