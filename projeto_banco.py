
valor_conta = 0
numero_saque = 0
limite_saque = 3
extrato = ""

while True:

    print("\n\n===================================================")
    print('******************** BEM VINDO ********************')
    print("===================================================")
    op_menu = int(input("\n1. Deposito \n2. Saque \n3. Extrato \n4. Sair \n\n Digite uma opção: "))
    

    if op_menu == 1:
        deposito = float(input('Digite o valor a ser depositado: '))  
        if deposito > 0:
            valor_conta += deposito
            extrato += f"Valor depositado: R$ {deposito:.2f}\n"
        else:
            print("Valor inválido!")
    
    elif op_menu == 2:
        saque = float(input('Digite o valor para saque: '))
        if saque > valor_conta:
            print("saldo insuficiente")
        
        elif numero_saque >= limite_saque:
            print("Número de saques excedido!")

        elif saque > 0 and saque < 500:
            valor_conta -= saque
            extrato += f"Valor saque: R$ {saque:.2f}\n"
            numero_saque += 1
            
        else:
            print("Valor acima do limite permitido!")
    
    elif op_menu == 3:
        print("\n===================== EXTRATO =====================\n")
        if len(extrato) == 0:
            print('Não foram realizadas movimentações.')
        else:
            print(extrato)
            print(f"Saldo em conta: R$ {valor_conta:.2f}")
        print("\n===================================================")

    elif op_menu == 4:
        print('Encerrando operação!')
        break
    else:
        print('Opção invalida!')
