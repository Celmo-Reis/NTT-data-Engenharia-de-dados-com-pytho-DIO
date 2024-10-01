
def deposito(saldo, valor, mostrar_extrato,/):
    if valor > 0 : 
        saldo += valor
        mostrar_extrato += f'+R${valor}\n'    
    else:
        print("apenas depositos positivos")
    
    return saldo, mostrar_extrato

def saque(*,saldo, valor, mostrar_extrato, limite, numero_saque, limite_saque):

    if numero_saque < limite_saque:

        if valor <= saldo:
                
            if valor <= limite:
                saldo -= valor
                numero_saque = numero_saque + 1
                mostrar_extrato += f'-R${valor}\n'
                                                
            else: 
                print("NEGADO, limite máximo de R$ 500.00 por saque")      
                
        else: 
            print(f"não poderá sacar o dinheiro por falta de saldo {saldo}")
                
    else:
        print("limite de saque diário esgostado")
    
    return saldo, mostrar_extrato, numero_saque

def extrato(saldo,/,*,mostrar_extrato):
    print("==============EXTRATO==============\n")
    print(mostrar_extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print("===================================")

def criar_usuario(usuarios):
        cpf = input("digite o seu cpf\n")
        usuario = filtrar_usuario(cpf, usuarios)
        if usuario:
            print("já tem usuario com esse cpf")
            return 
    
        nome = input("digite o nome do usuario\n")
        data_nascimento = input("digite data de nascimento dd-mm-yy\n")
        endereco = input("digite o endereço: logradouro - nro-bairro - cidade/sigla estado\n")

        usuarios.append({"nome": nome, "cpf": cpf, "data nascimento": data_nascimento, "endereco" :endereco })
        print ('usuario criado com sucesso')
       
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [x for x in usuarios if x["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None  

def criar_conta(usuarios, agencia, numero_conta ):
    cpf = input("digite o cpf\n")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("conta criada com sucesso")
        return {"agencia" : agencia, "numero da conta" : numero_conta, "usuario": usuario}
    
    print("\n usuario não encontrado")

def lista_contas(contas):
    if contas:
        print("Contas cadastradas:\n")
        for conta in contas:
            nome_usuario = conta["usuario"]["nome"]
            agencia = conta["agencia"]
            numero_conta = conta["numero da conta"]

            print(f"Titular: {nome_usuario} \nNúmero da conta: {numero_conta} \nAgencia: {agencia}\n")
    else:
        print("0 contas cadastradas")

def menu():
    menu ="""    
Digite a operação:
[d] = deposito
[s] = saque
[e] = extrato
[cu] = criar usuario
[cc] = cadastrar conta
[ll] = listar contas
[f] = sair
"""
    return input(menu) 

def main():
    saldo = 0
    numero_saque = 0
    mostrar_extrato = ""
    usuarios = []
    contas = []
    agencia = "0001"
    limite = 500
    limite_saque = 3
    
    while True:

        operacao = menu()
        
        if operacao not in ["d", "s", "e", "f", "cu", "cc", "ll"]:
            print("Operação inválida")
        
        elif operacao == "d":
            valor = float(input("Qual valor deseja depositar?\n"))
            saldo, mostrar_extrato = deposito(saldo, valor, mostrar_extrato)
                    
        elif operacao == "s":
            valor = float(input("Qual o valor que deseja sacar?\n"))
            saldo, mostrar_extrato, numero_saque = saque(saldo = saldo, valor = valor, mostrar_extrato = mostrar_extrato,limite = limite, numero_saque = numero_saque, limite_saque = limite_saque)     
                
        elif operacao == "e":
            extrato(saldo, mostrar_extrato = mostrar_extrato)
            
        elif operacao =="cu":
            criar_usuario(usuarios)
        
        elif operacao == "cc":
            numero_contas = len(contas) +1
            conta = criar_conta(usuarios, agencia, numero_contas)

            if conta:
                contas.append(conta) 
        
        elif operacao == "ll":
            lista_contas(contas)
               
        elif operacao == "f":
            break       

main()