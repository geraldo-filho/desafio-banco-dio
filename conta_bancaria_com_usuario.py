import textwrap


def menu():
    menu = """\n
    Bem vindo ao Banco G10bank
    --------------------------
    Qual funcao deseja utlizar?
    [1] - \tDeposito
    [2] - \tSaque
    [3] - \tExtrato
    [4] - \tCriar Usuário
    [5] - \tCriar Conta
    [6] - \tListar Contas

    [0] - \tSair
    --------------------------
    => """
    return input(textwrap.dedent(menu))


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário nã encontrado, Fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))


def cadastrar_usuario(usuarios):
    cpf = input("Digite seu CPF (Somento número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Digite seu primeiro Nome: ")
    data_nasc = input("Digite sua Data de Nascimento: (dd/mm/aaaa): ")
    endereco = input(
        "Digite seu endereço completo: (lagradouro, nro - bairro - cidade/sigla: ")

    usuarios.append({"nome": nome, "data_nasc": data_nasc,
                    "cpf": cpf, "endereco": endereco})

    print("Usuário criado com ucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def sacar(*, saldo, valor, extrato, limite, qtda_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = qtda_saques >= limite_saques

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
        print(f"Transação não concluída! Valor informado é invalido.")

    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("")
        print(f"Valor R$ {valor:.2f} Depositado com sucesso!")
    elif valor <= 0:
        print("Valor Incorreto, Digite um valor acima de 0")

    return saldo, extrato


def extrato_conta(saldo, /, *, extrato):

    print("========EXTRATO========")
    print("Não Foram Realizada Transações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=======================")


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    qtda_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = int(menu())

        if opcao == 1:
            valor = float(input("Qual o valor deseja Depositar? "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Qual o valor deseja Sacar? "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                qtda_saques=qtda_saques,
                limite_saques=LIMITE_SAQUE
            )
        elif opcao == 3:
            extrato_conta(saldo, extrato=extrato)

        elif opcao == 4:
            cadastrar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)
        elif opcao == 0:
            break
        else:
            print("Operação Inválida - Selecione novamente a opção desejada")


main()
