from banco import Banco

bc = Banco('Banco Prim', 999)
#cpfs = dict()

for _ in range(7):
        operacao, *parametros = input().split()
        
        if operacao[0] == 'abre_conta':
            #cpf = parametros[0]
            bc.abre_conta(parametros[-1], parametros[0])
            #cpfs[cpf] = nct
            
        elif operacao[0] == 'deposito':
            #bc.deposito(cpfs[cpf], float(parametros[2]))
            cpf = parametros[0]
            nconta = bc.descobrir_conta(cpf)
            bc.deposito(nconta, float(parametros[2]))
            
        elif operacao[0] == 'transferencia':
            nconta_origem = bc.descobrir_conta(parametros[0])
            nconta_destino = bc.descobrir_conta(parametros[1])
            bc.transferencia(nconta_origem, nconta_destino, float(parametros[-1]))
            
        elif operacao[0] == 'saque':
            cpf = parametros[0]
            nconta = bc.descobrir_conta(cpf)
            bc.saque(nconta, float(parametros[-1]))
            
for cpf, saldo in bc.relatorio_cpf_saldo():
    print(cpf, saldo)