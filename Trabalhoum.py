def calcular_total(produtos):
    total = sum([produto[1] * produto[2] for produto in produtos])
    return total

produtos = []

while True:
    nome = input("Digite o nome do perfume: ")
    preco = float(input("Digite o preço do perfume: "))
    quantidade = int(input("Digite a quantidade de unidades disponíveis: "))
    produtos.append((nome, preco, quantidade))
    adicionar = input("Deseja adicionar mais um perfume?: ")
    if adicionar.lower() != 's':
        break

venda_total = calcular_total(produtos)

print("Produtos disponíveis na loja:")
for produto in produtos:
    print("Nome:", produto[0])
    print("Preço:", produto[1])
    print("Quantidade disponível:", produto[2])
    print("_________________")

print("Total de vendas na loja:", venda_total)
