from validate_docbr import CPF, CNPJ
class Documento:

    @staticmethod
    def criar_documento(documento):
        if len(documento) == 11:
            return docCpf(documento)
        elif len(documento) == 14:
            return docCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos inválido!")

class docCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
    def format (self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class docCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    def format (self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
