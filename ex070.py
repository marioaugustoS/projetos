'''# Função para verificar se a string contém apenas letras
def contem_apenas_letras(string):
    return string.isalpha()

# Função para verificar se a string contém apenas números
def contem_apenas_numeros(string):
    return string.isdigit()

# Função para solicitar ao usuário um valor que atenda a determinado critério
def solicitar_valor(mensagem, criterio):
    valor = input(mensagem)
    while not criterio(valor):
        valor = input("Por favor, insira um valor válido: ")
    return valor

# Criando um dicionário vazio para armazenar informações do produto
produto = {}

# Solicitando informações do produto ao usuário
produto['nome'] = solicitar_valor("Digite o nome do produto: ", contem_apenas_letras)
produto['preco'] = float(solicitar_valor("Digite o preço do produto: ", contem_apenas_numeros))
produto['id'] = solicitar_valor("Digite o ID do produto: ", contem_apenas_numeros)

# Exibindo as informações do produto
print("Informações do Produto:")
print("Nome:", produto['nome'])
print("Preço:", produto['preco'])
print("ID:", produto['id'])'''
import operator
listaProdutos = []

def verificaNome(x):
    return x.isalpha()

def verificaID(x):
    return x.isdigit()

def verificaPreço(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

while True:
    nome = input("coloque o nome do produto")
    preço = input("coloque o preço do produto ")
    id = input("coloque o ID do produto ")
    if verificaPreço(preço):
       preço = float(preço)

    if not verificaPreço(preço):
        print("preço invalido ")
        continue
    if not verificaNome(nome):
        print("nome invalido")
        continue
    if not verificaID(id):
        print("id invalido")
        continue


    produto = {'nome':nome, 'preço': preço,'id':id}

    listaProdutos.append(produto)

    continuar = input('deseja continuar? s/n')
    if continuar.lower() != 's':
        break

    for id,produto in enumerate(listaProdutos, start=1):
        print(f"Produto {id}: Nome - {produto['nome']}, Preço - {produto['preço']}, ID - {produto['id']}")


total_preço = 0
for produto in listaProdutos:
    total_preço += produto['preço']

produtosCaros = 0

for produto in listaProdutos:
    if produto['preço'] > 1000:
        produtosCaros += 1


lista_ordenada = sorted(listaProdutos, key=operator.itemgetter('preço'))

print(f'o preço total foi de {total_preço} reais')
print(f'voce comprou {produtosCaros} produtos acima de 1000 reais')
print(f"o produto mais barato foi {lista_ordenada[0]['preço']} reais")


