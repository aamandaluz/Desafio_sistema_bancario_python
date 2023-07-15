menu = """ 
Selecione uma opção

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""
contador_saque = 0
saldo = 0
extrato = ""

while True:
    opcao = input(menu)
    
    if opcao == "1": 
        valor_deposito = float(input("Digite o valor do depósito:"))
        
        if valor_deposito > 0:
            print ("Depósito realizado com sucesso!")
            saldo += valor_deposito 
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
        else: print ("Depósito inválido!")  

    elif opcao == "2":
        if contador_saque < 3:
            valor_saque = float(input("Digite o valor do saque:"))
            
            excedeu_limite = valor_saque > 500
            excedeu_saldo = valor_saque > saldo
            
            if excedeu_limite:
                print ("Valor acima do limite de saque.")
            elif excedeu_saldo:
                print ("Saldo insuficiente!")
            else :
                print("Realizando saque")
                contador_saque += 1
                saldo -= valor_saque
                extrato += f"Saque: R${valor_saque:.2f}\n"
            
        else: print("Limite diário de saque excedido!")
    
    elif opcao == "3": 
        e = "Extrato"
        print(e.center(20)) 
        print("Não foram realizadas movimentações." if not extrato else extrato)  
        print(f"\nSaldo: R$ {saldo:.2f}")
        

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")


          



        