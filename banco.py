from ficha_bancaria import *

class Banco:
    def __init__(self, nome_banco, codigo_banco):
        self.__nome = nome_banco
        self.__numero = codigo_banco
        self.__ultima_conta_criada = 0
        self.__fichario = {}
        
    def abre_conta(self, nome_cliente, cpf_cliente):
        self.__ultima_conta_criada += 1
        
        ficha = FichaBrancaria()
        ficha.set_numero(self.__ultima_conta_criada)
        ficha.set_nome(nome_cliente)
        ficha.set_cpf(cpf_cliente)
        self.__fichario[self.__ultima_conta_criada] = ficha
        return self.__ultima_conta_criada
        
    def encerra_conta(self, numero_conta):
        if numero_conta in self.__fichario and self.saldo(numero_conta) == 0:
            del self.__fichario[numero_conta]
            return True
        else:
            return False
        
    def saldo(self, numero_conta):
        if numero_conta in self.__fichario:
            conta = self.__fichario[numero_conta]
            saldo = conta.get_saldo()
            return saldo
        else:
            return False
        
    def deposito(self, numero_conta, valor):
        if numero_conta in self.__fichario:
            self.__fichario[numero_conta].credite(valor)
            return True
        else:
            return False
    def saque (self, numero_conta, valor):
        if numero_conta in self.__fichario:
            self.__fichario[numero_conta].debite(valor)
            return True
        else:
            return False
    
    def tranferencia(self, nct_origem, nct_destino, valor):  
        if nct_origem in self.__fichario and nct_destino in self.__fichario:
            ficha_origem = self.__fichario[nct_origem]
            if ficha_origem.get_saldo() >= valor:
                self.__fichario[nct_destino].debite(valor)
                self.__fichario[nct_destino].credite(valor)
                return True
            else:
                return False
    def relatorio_cpf_saldo(self):
        pares = list()
        for ficha in self.__fichario.values():
            pares.append((ficha.get_cpf(), ficha.get_saldo()))
        pares.sort()
        return pares
        
    def saldo_medio(self):
        soma = 0
        contas = 0
        for ficha in self.__fichario.values():
            soma += ficha.get_saldo()
            contas += 1
        media = soma / contas
        return media
    
    def conta_maior_saldo(self):      
        maior_saldo = -10000
        nct = 0
        for ficha in self.__fichario.values():
            if ficha.get_saldo() > maior_saldo:
                maior_saldo = ficha.get_saldo()
                nct = ficha.get_numero()
        return nct
        
    def cpf_duplicados(self):
        cpfs = set()
        cpfs_duplicados = set()
        for cpf in self.__fichario.values():
            if cpf in cpfs:
                cpfs_duplicados.add(cpf)
            else:
                cpfs.add(cpf)
        return cpfs_duplicados
    
    def descobrir_conta(self, cpf):
        for ficha in self.__fichario.values():
            if ficha.get_cpf() == cpf:
                return ficha.get_numero()
        return -1