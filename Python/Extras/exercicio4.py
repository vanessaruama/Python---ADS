# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ela

digite = input("Digite algo: ")
print("O tipo primitivo desse valor é", type(digite))
print("Só tem espaço?", digite.isspace())
print("É um número?", digite.isnumeric())
print("É alfabético?", digite.isalpha())
print("É alfanumérico?", digite.isalnum())
print("Esta em letras maiúsculas?", digite.isupper())
print("Esta em letras minúsculas?", digite.islower())
print("Esta capitalizada?", digite.istitle())