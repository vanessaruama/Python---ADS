# -*- coding: UTF-8 -*-

# Regras da Nota
# (20% * NI + 30% * PROJETO + 50 * PROVA) / 100

# Notas Obtidas
# NI: 8  PROJETO: 10 PROVA: 5

print("Cálculo da Média FECAP")

# nota_ni, nota_projeto,nota_prova é do tipo float (valores quebrados, exemplo: 2.2, 4.5 etc)
nota_ni = 8.0
nota_projeto = 10.0
nota_prova = 5.0

# Comando type me ajuda a descobrir de que tipo é a variavel
print(type(nota_ni))

media = (20 * nota_ni + 30 * nota_projeto + 50 * nota_prova) / 100

# boleanos são varias que salvam verdadeiro (True) ou Falso
aprovado = True

# mensagem_nota_aluno é do tipo string, textos, frases e etc ex: "Olá Mundo"
mensagem_nota_aluno = "Minha nota foi: " + str(media) + " Aprovado?: " + str(aprovado)

print(mensagem_nota_aluno)

