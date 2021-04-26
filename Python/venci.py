venci = False
print("Jogo da adivinhação")
jogada = int(input("Digite um número de 1 a 10: "))

venci = jogada >= 5

if venci:
    print("Eu ganhei :)")
else:
    print("Eu perdi :(")    