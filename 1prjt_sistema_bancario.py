##Sistema Bancario - Projetinho

#mensagem menu
menu = '''
        [d] - depositar
        [s] - sacar
        [e] - extrato
        [q] - sair

'''

#variaveis
saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3

while True:
    
    teclado = input(menu)
    
    if teclado == "d":
        valor = float(input("Qual o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato == f"Depósito no valor de R$ {valor:.2f}\n"
        else:
            print("Valor inválido, tente novamente")
            
    elif teclado == "s" :
        valor = float(input("Qual o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = num_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo Insuficiente")
        elif excedeu_limite:
            print("Excedeu Limite")
        elif excedeu_saques:
            print("Numero de saques diários excedido")
        elif valor > 0:
            saldo -= valor
            extrato == f"Saque no valor de R$ {valor:.2f}\n"
        else:
            print("Falha no saque, tente novamente")

    elif teclado == "e" :
        print("EXTRATO".center(20,"="))
        print("Sem movimentações" if not extrato else extrato)
        print(f"\n\nSaldo: R$ {saldo:10,.2f}\n")
        print("".center(20,"="))

    elif teclado == "q" : 
        break
    else:
        print("Opção inválida, tente novamente")
