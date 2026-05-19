menu = """
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair
Digite uma opção:
"""

limite = 500
saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informao é inválido.")
    
    elif opcao == "s":
        valor = float(input("Digite o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > 500
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        if excedeu_limite:
            print("Operação falhou! Você atingiu o limite de R$ 500,00 de valor do saque.")

        if excedeu_saque:
            print("Operação falhou! Você atingiu o limite de saque.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n ============= EXTRATO =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida. Por favor selcione novamente a operação desejada.")