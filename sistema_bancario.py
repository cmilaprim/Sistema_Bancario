menu = """
[d] depositar
[s] saque
[e] extrato
[s] sair
"""
saldo = 0
extrato = ''
valor_limite = 500
num_saque = 0
quantidade_saque_limite = 3

while True:
    opçao = input(menu)
    
    if opçao == 'd':
        valor = float(input('Infome o valor de saque: R$'))
        if valor > 0:
            extrato += f"Depósito: R${valor:.2f}"
            saldo += valor
        else:
            print('Valor incorreto. Erro na operação')
    elif opçao == 's':
        valor = float(input('Informe o valor do seu saque: R$'))
        
        excedeu_limite = valor > valor_limite
        excedeu_saldo = valor > saldo
        excedeu_quantidade_saque = num_saque > quantidade_saque_limite
        
        if excedeu_limite:
            print('Limite de saque excedito. Erro na operação.')
        elif excedeu_quantidade_saque:
            print('Quantidade de saques excedito. Erro na oparção.')
        elif excedeu_saldo:
            print('Saldo insuficiente. Erro na opração.')
        elif valor > 0:
            saldo -= valor
            num_saque += 1
            extrato = f'Saque: R${valor:.2f}'
        else:
            print('Valor inválido!Operação falhou')
            
    elif opçao == 'e':
        print('extrato').center()
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'\nR${saldo:.2f}')
    else:
        break