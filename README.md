# Sistema de Banco - Fundamentos de Python

Este projeto foi desenvolvido como parte do curso de Python da Suzano DIO. O objetivo é construir um sistema bancário simples, permitindo operações de saque, depósito e visualização de extratos.


## Funcionalidades Requisitadas

- **Depósito**: Permite adicionar um valor ao saldo da conta.
- **Saque**: Realiza retiradas, com controle para garantir que o saldo seja suficiente.
- **Extrato**: Exibe todas as transações realizadas, como depósitos e saques.


## Tecnologias Utilizadas

[![Python](https://img.shields.io/badge/python-000?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/3/)


## Minhas Implementações Pessoais

- **Tratamento de Erros**: Adicionei um bloco `try` para evitar que o programa quebre caso o valor inserido não seja convertido corretamente para `float`.
- **Função de Exceções**: Criei uma função dedicada exclusivamente ao tratamento das exceções durante o saque.
- **Exibição de Saldo**: Adicionei uma opção para o usuário consultar o saldo atual da conta.


## Testes Realizados

- **Caracteres Inválidos**: O sistema impede que o usuário insira caracteres não numéricos durante as operações.
- **Depósito Negativo ou Zero**: O sistema impede depósitos de valores negativos ou iguais a zero.
- **Saque Negativo ou Zero**: O sistema impede saques de valores negativos ou iguais a zero.
- **Exceções**: O sistema garante que não seja possível sacar um valor superior ao saldo, ao limite permitido ou ao limite diário de saques.
