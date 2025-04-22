import unittest
from unittest.mock import patch
from funcionarios import FuncionarioComum, Gerente
from sistema_rh import SistemaRH

class TestSistemaBonus(unittest.TestCase):

    def test_funcionario_comum_calcula_bonus_corretamente(self):
        funcionario = FuncionarioComum("Alice", 2000)
        self.assertAlmostEqual(funcionario.calcular_bonus(), 200.0)

    def test_gerente_calcula_bonus_corretamente(self):
        gerente = Gerente("Marcio", 5000, 1000)
        self.assertAlmostEqual(gerente.calcular_bonus(), 2000.0)

    def test_set_salario_nao_aceita_valor_negativo(self):
        funcionario = FuncionarioComum("Maria", 1500)
        with self.assertRaises(ValueError) as context:
            funcionario.salario = -100
        self.assertEqual(str(context.exception), "O salário não pode ser negativo.")

    @patch('builtins.print')
    def test_mostrar_bonus_imprime_mensagem_correta(self, mock_print):
        sistema_rh = SistemaRH()
        funcionario = FuncionarioComum("Diana", 3000)
        sistema_rh.mostrar_bonus(funcionario)
        mock_print.assert_any_call(f"O bônus de Diana é de R$ 300.00")
        mock_print.assert_any_call(f"LOG: Bônus de Diana calculado e exibido: R$ 300.00")

    @patch('builtins.print')
    def test_mostrar_bonus_com_gerente_imprime_mensagem_correta(self, mock_print):
        sistema_rh = SistemaRH()
        gerente = Gerente("Everaldo", 6000, 1500)
        sistema_rh.mostrar_bonus(gerente)
        mock_print.assert_any_call(f"O bônus de Everaldo é de R$ 2700.00")
        mock_print.assert_any_call(f"LOG: Bônus de Everaldo calculado e exibido: R$ 2700.00")

if __name__ == '__main__':
    unittest.main()
