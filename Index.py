
from Cep import BuscaEndereco
cep = "25800320"
objeto_cep = BuscaEndereco(cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r.text)

print(BuscaEndereco.retorna_endereco(cep))