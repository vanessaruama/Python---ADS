# Exercício 3
# Uma importadora importa produtos de vários países. O preço do frete varia de acordo com
# o país seguindo a tabela abaixo. Faça um programa que recebe o valor de um produto e o país de origem
# (imprima as opções possíveis em um menu) e imprima o valor total do produto mais frete.
# País | Estados Unidos | França | México | Argentina | China |
# Frete|     60,00      | 75,50  | 50,00  |   27,35   | 80,00 |

lista_produtos = ["Teclado", "Mouse", "Monitor", "Fone"]
lista_paises = ["Estados Unidos", "França", "México", "Argentina", "China"]
lista_precos = [100, 30.50, 700.50, 90]
valorTotal = sum(lista_precos)
linha = '-' * 38
linha2 = '-' * 74
produto_existente = False
pais_existente = False

#Primeiro mostrar lista de produtos
print(linha)
print("--------- Lista de Produtos ---------")
print(linha)

lista_compras = "1 - " + lista_produtos[0] + " - R$ " + str(lista_precos[0]) + "\n"
lista_compras += "2 - " + lista_produtos[1] + " - R$ " + str(lista_precos[1]) + "\n"
lista_compras += "3 - " + lista_produtos[2] + " - R$ " + str(lista_precos[2]) + "\n"
lista_compras += "4 - " + lista_produtos[3] + " - R$ " + str(lista_precos[3])
print(lista_compras)

while produto_existente == False:
    produto_escolhido = int(input("Digite o número correspondente ao seu produto para compra: "))
    #Verificar qual produto foi escolhido
    if produto_escolhido == 1:
        print("Você escolheu o Teclado")
        preço_produto = 100
        produto_existente = True
    elif produto_escolhido == 2: 
        print("Você escolheu o Mouse")
        preço_produto = 30.50
        produto_existente = True
    elif produto_escolhido == 3:    
        print("Você escolheu o Monitor")
        preço_produto = 700.50
        produto_existente = True
    elif produto_escolhido == 4: 
        print("Você escolheu o Fone")
        preço_produto = 90
        produto_existente = True
    else:
        print("Produto inválido, tente novamente") 

#Mostrar opções de países
print(linha2)
print("--------- Lista de Países para importação e seu respectivo frete ---------")
print(linha2)
paises_disponiveis = "1 - " + lista_paises[0] + "\n"
paises_disponiveis += "2 - " + lista_paises[1] + "\n"
paises_disponiveis += "3 - " + lista_paises[2] + "\n"
paises_disponiveis += "4 - " + lista_paises[3]
print(paises_disponiveis)
pais_escolhido = int(input("Digite o número de qual país você gostaria de importar seu produto para calcularmos o frete: "))

#fazer a conta com o produto escolhido + frete de acordo com o país
while pais_existente == False:
    if pais_escolhido == 1: #Estados Unidos
        print("O frete de importação dos Estados Unidos para a sua compra é de R$60")
        preco_total = preço_produto + 60 
        pais_existente = True
    elif pais_escolhido == 2: #França
        preco_total = preço_produto + 75.50
        print("O frete de importação da França para a sua compra é de R$75.50 \n")
        pais_existente = True
    elif pais_escolhido == 3: #México
        preco_total = preço_produto + 50 
        print("O frete de importação do México para a sua compra é de R$50.00 \n")
        pais_existente = True
    elif pais_escolhido == 4: #Argentina
        preco_total = preço_produto + 27.35
        print("O frete de importação da Argentina para a sua compra é de R$27.35 \n")
        pais_existente = True
    elif pais_escolhido == 5: #China   
        preco_total = preço_produto + 80 
        print("O frete de importação da China para a sua compra é de R$80 \n")
        pais_existente = True
    else:   
        print("Opção inválida, tente novamente")
        pais_escolhido = int(input("Digite o número de qual país você gostaria de importar seu produto para calcularmos o frete: "))

print(linha)
print("-- Valor total da compra: R$", preco_total, "--")
print(linha)