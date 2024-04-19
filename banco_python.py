escolha = int (input("Digite a opção que deseja [1] para depósito, [2] para saque, [3] para extrato e [0] para sair:"))
opcao = escolha
sistema_bancario = "Sistema Bancario"
saldo = 1450.0
deposito = 0
saques = 0
valor_deposito = 0.0
valor_saque = 0.0
while opcao != 0:
    print(sistema_bancario.center(30,"#")) 
    opcao = escolha
    if opcao == 1:
        valor = float(input("Qual valor deseja depositar? "))
        
        while valor<=0:
            valor = float(input("Impossivel depositar essa quantia, digite outro valor: "))

        if valor >0:
            saldo+= valor
            deposito+=1   
            print(f"Saldo atual = R${saldo:.2f}")
            print()
            valor_deposito += valor
            escolha = int (input("Digite a opção que deseja [1] para depósito, [2] para saque, [3] para extrato e [0] para sair: "))
            opcao = escolha
    elif opcao == 2:
        if saques < 3: 
            valor =float(input("Qual valor você vai querer sacar, lembrando que o valor maximo por saque é R$ 500.00: "))
            while (valor > saldo) or (valor > 500):
                valor = float(input("Valor negado digite outro valor: "))
            if (valor < saldo) or (valor < 500):
                saldo -= valor
                saques += 1
                print(f"Saldo atual = R${saldo:.2f}")
                print()
                valor_saque += valor
                escolha = int (input("Digite a opção que deseja [1] para depósito, [2] para saque, [3] para extrato e [0] para sair: "))
                opcao = escolha
        else:
            print("Ja passou da quantidade de saque permitidas no dia")
            escolha = int (input("Digite a opção que deseja [1] para depósito, [2] para saque, [3] para extrato e [0] para sair: "))
            opcao = escolha
    elif opcao == 3:
        print(f"Total de depositos = {deposito}, no valor de R${valor_deposito:.2f}")
        print(f"Total de saques = {saques}, no valor de R${valor_saque:.2f}")
        print(f"Saldo atual = R${saldo:.2f}")

        escolha = int (input("Digite a opção que deseja [1] para depósito, [2] para saque, [3] para extrato e [0] para sair: "))
        opcao = escolha  
    else:
        escolha = int(input("Opcao invalida digite novamente, [1] para depósito, [2] para saque, [3] para extrato e [0] para sair:"))  
        opcao = escolha      
    
        


