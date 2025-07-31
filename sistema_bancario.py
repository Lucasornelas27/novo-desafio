
import textwrap

def main():
    valor_depositado = 0
    valor_a_sacar = 0
    numero_de_saque = 3
    tentativas_de_saque = 0
    limite = 500
    extrato = ""
    saldo = 0
    contas = [{
        "agencia": "0001",
        "numero": "0001",
        "titular": {"nome": "lucas"}
    }]
    usuarios = []

    while True:
        opcao_do_menu = menu()

        if opcao_do_menu == 1:
            valor_depositado = float(input("valor a depositar: "))
            saldo, extrato = depositar(saldo, valor_depositado, extrato)

        elif opcao_do_menu == 2:
            valor_a_sacar = float(input("qual valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor_a_sacar=valor_a_sacar,
                extrato=extrato,
                limite=limite,
                numero_de_saque=numero_de_saque,
                tentativas_de_saque=tentativas_de_saque,
            )

        elif opcao_do_menu == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao_do_menu == 4:
            listar_contas(contas)

        elif opcao_do_menu == 5:
            numero_de_contas = len(contas) + 1
            nova_conta = criar_conta(numero_de_contas, contas, usuarios)
            if nova_conta:
                contas.append(nova_conta)

        elif opcao_do_menu == 6:
            criar_usuario(usuarios)

        elif opcao_do_menu == 7:
            print("Obrigado por usar nosso sistema!")
            break


def menu():
    menu = textwrap.dedent("""
    ===============MENU=============
    [1] DEPOSITAR
    [2] SACAR
    [3] EXTRATO
    [4] LISTAR CONTAS
    [5] NOVA CONTA
    [6] NOVO USUÁRIO
    [7] SAIR
    =================================
    """)
    return int(input(menu))


def depositar(saldo, valor_depositado, extrato, /):
    if valor_depositado > 0:
        saldo += valor_depositado
        extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
    else:
        print("OPERAÇÃO FALHOU")
    return saldo, extrato


def sacar(*, saldo, valor_a_sacar, extrato, limite, numero_de_saque, tentativas_de_saque):
    excedeu_valor = valor_a_sacar > saldo
    excedeu_saques = tentativas_de_saque >= numero_de_saque
    excedeu_limite = valor_a_sacar > limite

    if excedeu_valor:
        print("Você não tem saldo.")
    elif excedeu_limite:
        print("Ultrapassou seu limite.")
    elif excedeu_saques:
        print("Ultrapassou suas tentativas de saque.")
    elif valor_a_sacar > 0:
        saldo -= valor_a_sacar
        extrato += f"Saque: R$ {valor_a_sacar:.2f}\n"
        tentativas_de_saque += 1
    else:
        print("Operação falhou!")

    return saldo, extrato


def exibir_extrato(saldo, /, extrato):
    print("\n======= EXTRATO BANCÁRIO =======")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=================================")


def listar_contas(contas):
    for conta in contas:
        linha = f""" 
Agência: {conta['agencia']}
Conta Corrente: {conta['numero']}
Titular: {conta['titular']['nome']}
"""
        print("=" * 100)
        print(textwrap.dedent(linha))
        print("=" * 100)


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(numero_de_contas, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        agencia = "0001"
        numero_conta = str(numero_de_contas).zfill(4)
        print("\n=== Conta criada com sucesso! ===")
        return {
            "agencia": agencia,
            "numero": numero_conta,
            "titular": usuario
        }

    print("\n@@@ Usuário não encontrado. Criação de conta cancelada. @@@")
    return None


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("=== Usuário criado com sucesso! ===")


main()
