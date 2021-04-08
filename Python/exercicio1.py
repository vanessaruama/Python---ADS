# Receba o nome de uma pessoa, diga oi pra ela e diga qual a
# última letra do nome dela.

print("Exercício 1")
nomeDaPessoa = input("Olá, diga seu nome: ")
print("Oi " + nomeDaPessoa)
tamanho = len(nomeDaPessoa)
posicaoUltimaLetra = tamanho -1
ultimaLetra = nomeDaPessoa[posicaoUltimaLetra]
print("A última letra do seu nome é: "  + ultimaLetra )