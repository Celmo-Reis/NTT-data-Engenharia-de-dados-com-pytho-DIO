from datetime import datetime
saldo = 0
movimentacao = []
contador_saque = 0
contador_operacao = 0
ultima_transacao=0

menu = """
Digite a operação:
[d] = deposito
[s] = saque
[e] = extrato
[f] = sair
"""

while True:
    hoje = datetime.today().date()  

    if hoje != ultima_transacao:
        contador_operacao = 0
        ultima_transacao = hoje
        contador_saque = 0
                
    operacao = input(menu)

    if operacao not in ["d", "s", "e", "f"]:
        print("Operação inválida")
    
    elif operacao == "d":

        if contador_operacao >= 10:
            print("Limite de transações diárias excedidas")

        else: 
            valor_deposito = float(input("Qual valor deseja depositar?"))
    
            if valor_deposito > 0 : 
                movimentacao.append(f' +R${valor_deposito:.2f} // {datetime.today().replace(microsecond=0)}')
                saldo += valor_deposito
                contador_operacao += 1
                ultima_transacao = hoje
        
            else:
                print("apenas depositos positivos")
        
    elif operacao == "s":

        if contador_operacao >= 10:
            print("Limite de transações diárias excedidas")
    
        elif contador_saque < 3:
            valor_saque = float(input("Qual o valor que deseja sacar?"))
        
            if valor_saque <= saldo:
            
                if valor_saque <= 500:
                    movimentacao.append(f' -R${valor_saque:.2f} // {datetime.today().replace(microsecond=0)}')
                    saldo -= valor_saque
                    contador_saque += 1 
                    contador_operacao +=1
                    ultima_transacao = hoje
                
                else: 
                    print("NEGADO, limite máximo de R$ 500.00 por saque")      
            
            else: 
                print(f"não poderá sacar o dinheiro por falta de saldo {saldo}")
            
        else:
            print("limite de saque diário esgostado")
        
    elif operacao == "e":
        print("==============EXTRATO==============\n")
        print("\n".join([f"{valor}\n" for valor in movimentacao]))
        print(f'Saldo: R${saldo:.2f}')
        print("===================================")  

    elif operacao == "f":
        break           
