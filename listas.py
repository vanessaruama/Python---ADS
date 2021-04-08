lista_itens = ["Laranja", "Banana", "Batata", "Brocolis"]
lista_precos = [2.5, 4.0, 5.0, 10.0]
valorTotal = sum(lista_precos)
linha = '-' * 38

print(linha)
print("------- Minha Lista de Mercado -------")
print(linha)

lista_mercado = "1 - " + lista_itens[0] + " - R$ " + str(lista_precos[0]) + "\n"
lista_mercado += "2 - " + lista_itens[1] + " - R$ " + str(lista_precos[1]) + "\n"
lista_mercado += "3 - " + lista_itens[2] + " - R$ " + str(lista_precos[2]) + "\n"
lista_mercado += "4 - " + lista_itens[3] + " - R$ " + str(lista_precos[3])
print(lista_mercado)

print(linha)
print("--- Valor total da compra: R$", valorTotal, "---")
print(linha)


#--------Exemplos/OutrasFormas----------
#lista_maluca = ["String", 10, 45.6]

#print("1 - " + lista_itens[0] + " - R$ " + str(lista_precos[0]))
#print("2 - " + lista_itens[1] + " - R$ " + str(lista_precos[1]))
#print("3 - " + lista_itens[2] + " - R$ " + str(lista_precos[2]))
#print("4 - " + lista_itens[3] + " - R$ " + str(lista_precos[3]))
