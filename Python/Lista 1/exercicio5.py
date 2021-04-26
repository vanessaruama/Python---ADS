# Exercício 5
# A campanha de vacinação para COVID-19 se adaptou para atender diversos grupos.
# - Para o público geral, a idade mínima é 64 anos.
# - Para os educadores a idade mínima é 47 anos.
# - Para os profissionais da segurança pública não há idade limite, todos já podem tomar vacina.
# - Para os profissionais da saúde pública não há idade limite, todos já podem tomar vacina.
# Com base nestas regras escreva um programa que receba dois valores, um valor para idade 
# e um valor para identificar o grupo pertencente. 
# (Você pode criar um menu no caso do grupo)

print("-" * 42)
print("-- Bem vinda(o) a Campanha de Vacinação --")
print("-" * 42)

idade = int(input("Por favor, digite a sua idade: "))
grupos_disponiveis = "Grupos de vacinação: \n 1- Público Geral \n "
grupos_disponiveis += "2- Educadores \n 3- Profissionais da Segurança pública \n "
grupos_disponiveis += "4- Profisisonais da Saúde Pública"
print(grupos_disponiveis)
grupo = int(input("Digite o número correspondente ao grupo que você se encaixa: "))

if grupo == 1: #Público Geral - idade mínima é de 64 anos
    if idade < 64:
        print("Vacinação não disponível para a sua idade")
    else:
        print("Você já pode ser vacinado")    
elif grupo == 2: #Educadores - idade mínima é de 47 anos
    if idade < 47:
        print("Vacinação não disponível para a sua idade")
    else:    
        print("Você já pode ser vacinado")    
elif grupo == 3: #Profissionais da Segurança pública - todos podem
        print("Você já pode ser vacinado")
elif grupo == 4: #Profisisonais da Saúde Pública - todos podem
        print("Você já pode ser vacinado")
else:
    print("Grupo inválido")