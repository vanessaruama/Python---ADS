#Exercício 1
# Faça um programa que receba uma idade 0 - 150, e imprima para cada situação o seguinte:
# Se menor de 18 "Não pode beber e nem tirar carta"
# Se maior de 18 e menor que 21: "Não pode beber, mas pode tirar carta"
# Se maior que 21: "Liberado pela lei, pode beber e dirigir, mas não os dois no mesmo dia"

nome = input("Qual seu nome: ")
print("Olá", nome)
idade = int(input("Digite sua idade: "))

if idade < 0:
    print("A idade que você digitou é inválida")
elif idade < 18:
    print("Não pode beber e nem tirar carta")
elif idade >= 18 and idade < 21: #coloquei igual ou maior que 18 por lógica, creio que no enunciado esta errado
    print("Não pode beber, mas pode tirar carta") 
elif idade >= 21 and idade <= 150:
    print("Liberado pela lei, pode beber e dirigir, mas não os dois no mesmo dia")
else:
    print("Nosso sistema só aceita idade até os 150 anos")