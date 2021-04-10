# Crie um script python que leia dois números e tente mostrar a soma deles

n1 = int((input("Digite um número: ")))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
print("A soma entre", n1, "e", n2, "é igual a", soma)

#outra forma de fazer o print
print("A soma entre {} e {} é igual a {}" .format(n1,n2,soma))