# Exceções de Saque
def exceptions(valor):
    global numero_saques
    global saldo
    global limite
    global extrato
    global LIMITE_SAQUES
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
        
    if excedeu_saldo:
        print(f"Operação falhou! Saldo Insuficiente\nSaldo Atual: R$ {saldo}")
        return False
    elif excedeu_limite:
        print("Operação falhou! Valor do saque excede o limite (limite de R$ 500)")
        return False
    elif excedeu_saques:
        print(f"Operação falhou! Número máximo (3) de saques excedido\nSaques realizados hoje: {numero_saques}")
        return False
    else:
        return True


menu = """
Escolha um número de 1-5 para realizar um operação:
[1] Depositar
[2] Sacar
[3] Extrato
[4] Saldo
[5] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    opcao = input(menu)
    
    # Realizar Depósito
    if opcao == "1":
        try:
            valor = float(input("Informe o valor do depósito: "))
            
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("O valor de depósito precisa ser maior que 0 (zero).")
                       
        except ValueError:
            print("\nNúmero Inválido, por favor utilize o formato: 000.00")
            
    # Realizar Saque
    elif opcao == "2":
        try:
            valor = float(input("Informe o valor do saque: "))

            if valor > 0:
                if exceptions(valor):
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saques += 1
                    print("Saque realizado com sucesso!!!")
                    
            else:
                print("O valor do saque precisa ser maior que 0 (zero)")
        except ValueError:
            print("\nNúmero Inválido, por favor utilize o formato: 000.00")
            
    # Vizualizar Extrato
    elif opcao == "3":
        print("==================EXTRATOS======================")
        print("Não foram realizadas movimentações." if not extrato else f"Movimentações realizadas: \n{extrato}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================================")
    
    # Vizualizar Saldo Atuaal
    elif opcao == "4":
        print(f"Saldo Atual: R$ {saldo}")
    
    # Fechar Aplicação
    elif opcao == "5":
        print("Finalizando Operação")
        break  
     
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")