class FornecedorNaoExisteException(BaseException):
    def __init__(self,cnpj):
        super().__init__()
        self.cnpj = cnpj
    def __str__(self):
        return ("O CNPJ \""+(self.cnpj) + "\" NA POSSUI CADASTRO!!!")