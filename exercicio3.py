# Faça um programa que você digite seu nome
# E o programa escreve quantas letras tem seu nome e primeira letra

seuNome = input("Qual o seu nome: ")
print("Oi " + seuNome)
numeroletras = len(seuNome)
primeiraletra = seuNome[0] 
quantletras = str(numeroletras)
print("Você sabia que seu nome tem " + quantletras + " letras" + " e a primeira letra do seu nome é " + "'" + primeiraletra + "'")