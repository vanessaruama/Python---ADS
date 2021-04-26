#Exercício 2
#Faça um programa que receba um valor inteiro de 1 a 3 e imprima os seguintes respostas:
# 1 – “Pagamento Débito”
# 2 – “Pagamento Crédito”
# 3 – “Pagamento Cartão”

forma_de_pagamento = int(input("Escolha sua forma de pagamento, sendo elas: \n 1- Débito \n 2- Crédito \n 3-Cartão \n" ))

if forma_de_pagamento == 1:
    print("Pagamento Débito")
elif forma_de_pagamento == 2:
    print("Pagamento Crédito")
elif forma_de_pagamento == 3:
    print("Pagamento Cartão")    
else:
    print("Opção inválida, escolhe entre as opções 1 e 3")

## Obs.: no enunciado esta opção 'cartão' pra mim não faz sentido, seria 'dinheiro' no lugar, já que débito
# e crédito já são opções de cartão, mas fiz conforme o enunciado        