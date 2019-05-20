class Funcionario:
    def __init__(self, rg, cpf, nome, funcao, data_nasc, salario):
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.funcao = funcao
        self.data_nasc = data_nasc
        self.salario = salario
    def str(self):
        string = "RG: "+str(self.rg)+"\nCPF: "+str(self.cpf)+"\nNOME: "+self.nome+"\nFUNCAO: "+self.funcao+\
                 "DATA NASCIMENTO: "+str(self.data_nasc)+"SALARIO: R$ "+round(self.salario,2)
        return string