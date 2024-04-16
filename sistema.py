#SISTEMA BANCÁRIO
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Deposito efetuado. Volte sempre!")
    else:
        print("O valor é inválido, tente novamente!")
    return depositar

def sacar():
    global saldo, extrato, numero_saques
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Você não tem saldo suficiente para realizar essa operação!")
        
    elif excedeu_limite:
        print("O valor do saque excede o limite! Informe um valor menor ou igual ao limite.")
    
    elif excedeu_saques:
        print("Operação sem sucesso! Número máximo de saques excedido!")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque efetuado. Volte sempre!")
    
    else:
        print("Operação falhou! O valor é inválido.")
    return sacar

def mostrar_extrato():
    print("\n============ EXTRATO ============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}\n")
    print("=================================")
    return mostrar_extrato 

def sair():
    print("""
    Obrigado por usar nosso sistema,
    volte sempre!
    """)

menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
"""
while True:
    opcao = input(menu)
    if opcao == '1':
        depositar()
    elif opcao == '2':
        sacar()
    elif opcao == '3':
        mostrar_extrato()
    elif opcao == '4':
        sair()
        break
    else:
        print("Operação inválida, por favor selecione a opração correta.")