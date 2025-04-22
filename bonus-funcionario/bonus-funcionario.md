# Sistema de Funcionários de uma Startup
Uma startup está criando um sistema para calcular o bônus de seus funcionários. Existem dois tipos de funcionários: os comuns e os gerentes. Além disso, o setor de Recursos Humanos (RH) deseja registrar todas as ações relacionadas ao bônus e verificar se os cálculos estão corretos.
Objetivo do desafio:
Você deve implementar classes e métodos utilizando os conceitos de Programação Orientada a Objetos (POO). Além disso, é necessário escrever testes automatizados para garantir que o sistema funciona como esperado.

Enunciado do Desafio
Crie um sistema com as seguintes etapas:
Etapa 1 – Criação das classes:
Crie uma classe abstrata chamada Funcionario com os seguintes itens:


Dois atributos privados: nome e salario.


Um método abstrato chamado calcular_bonus.


Três métodos públicos:


get_nome para retornar o nome.


get_salario para retornar o salário.


set_salario para atualizar o salário, com uma validação que impede valores negativos.


Crie uma classe chamada FuncionarioComum, que herda da classe Funcionario:


Implementa o método calcular_bonus, que deve retornar 10% do salário.


Crie uma classe chamada Gerente, que também herda da classe Funcionario:


Possui um atributo extra chamado bonus_adicional.


Implementa o método calcular_bonus retornando 20% do salário mais o valor de bonus_adicional.


Etapa 2 – Decorator para log:
Crie um decorator chamado logar_acao que exibe uma mensagem de log sempre que um bônus for mostrado na tela.


Etapa 3 – Classe de sistema:
Crie uma classe chamada SistemaRH com um método chamado mostrar_bonus, decorado com @logar_acao.


Este método deve receber um funcionário e exibir seu nome e o valor do bônus.


Etapa 4 – Testes automatizados:
Usando a biblioteca unittest, crie testes para verificar:


Se as classes FuncionarioComum e Gerente calculam corretamente seus bônus.


Se o método set_salario não aceita valores negativos.


Se o método mostrar_bonus imprime corretamente a mensagem (utilize unittest.mock para capturar a saída do print).



Entregáveis
Você deverá entregar três arquivos:
funcionarios.py – Contendo as classes Funcionario, FuncionarioComum e Gerente.


sistema_rh.py – Com a classe SistemaRH e o decorator logar_acao.


testes.py – Com os testes automatizados utilizando unittest.
