
'''Criando menu'''


menu = """

Bem vindo ao Banco G10bank
--------------------------
Qual funcao deseja utlizar?
            
[1] - Deposito
[2] - Saque
[3] - Extrato

[0] - Sair
--------------------------

=> """

'''Inicializando as variáveis necessárias'''
saldo = 0
limite = 500
extrato = ""
qtda_saques = 0
LIMITE_SAQUE = 3
deposito = 0

'''While true para sempre que for verdade o laço continue iterando'''
while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Qual o valor deseja Depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("")
            print(f"Valor R$ {valor:.2f} Depositado com sucesso!")
        elif valor < 0:
            print("Valor Incorreto, Digite um valor acima de 0")

    elif opcao == 2:
        valor = float(input("Qual o valor deseja Sacar? "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = qtda_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Transação não concluída! Saldo Insuficiente")
        elif excedeu_limite:
            print("Transação não concluída! Limite de R$500,00 Excedido")
        elif excedeu_saque:
            print("Transação não concluída! Limite de Saques Excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qtda_saques += 1
            print(f"Valor R$ {valor:.2f} Sacado com sucesso!")

        else:
            print("Transação falhou, O valor informado é inválido")

    elif opcao == 3:
        print("========EXTRATO========")
        print("Não Foram Realizada Transações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=======================")

    elif opcao == 0:
        break

    else:
        print("Operação Inválida - Selecione novamente a opção desejada")
