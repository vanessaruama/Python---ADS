alunos_grupo = ["William", "Eloisa", "Ivanise", "Victor"]
representante = input("Digite o número do aluno: ")

if alunos_grupo[0] == representante:
    print("Representante do Grupo posição 1:")
    print(representante)

elif alunos_grupo[1] == representante:
    print("Representante do Grupo posição 2:")
    print(representante)

elif alunos_grupo[2] == representante:
    print("Representante do Grupo posição 3:")
    print(representante)

elif alunos_grupo[3] == representante:
    print("Representante do Grupo posição 4:")
    print(representante)

else:
    print("Representante não esta no Grupo")