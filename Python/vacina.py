print("*-------------------------------*")
print("Bem vindo ao sistema de vacinação")
print("*-------------------------------*")

tipo_vacina = int(input("Entre com o código da vacina de sua preferência:\n[1]Coronavac \n[2]Oxford\n\n"))

dia = int(input("Entre com o número do dia que você tomou a primeira dose, entre 1 e 30: "))
mes = int(input("Entre com o número do mês que você tomou a primeira dose, entre 1 e 12: "))

if tipo_vacina == 1:
    print("Você tomou a Coronavac | Data da primeira dose: " + str(dia) + "/" + str(mes))
    dia_seg_dose_menor = dia + 14
    dia_seg_dose_maior = dia + 28
    mes_1 = mes
    mes_2 = mes

    if dia_seg_dose_menor > 30:
        dia_seg_dose_menor = dia_seg_dose_menor - 30
        mes_1 = mes_1 + 1

    if dia_seg_dose_maior > 30:
        dia_seg_dose_maior = dia_seg_dose_maior - 30
        mes_2 = mes_2 + 1

    if mes_1 > 12:
        mes_1 = mes_1 - 12

    if mes_2 > 12:
        mes_2 = mes_2 - 12    

    print("Data da segunda dose (menor): " + str(dia_seg_dose_menor) + "/" + str(mes_1))
    print("Data da segunda dose (maior): "  + str(dia_seg_dose_maior) + "/" + str(mes_2))
    
elif tipo_vacina == 2:
    print("Você tomou a Oxford | Data da primeira dose: " + str(dia) + "/" + str(mes))
    #90dias
    dia_seg_dose = dia
    mes = mes + 3

    if mes > 12:
        mes = mes - 12
        print("Data da segunda dose: "  + str(dia_seg_dose) + "/" + str(mes) + " do ano que vem")
    else:
        print("Data da segunda dose: "  + str(dia_seg_dose) + "/" + str(mes))
else:
    print("Vacina não cadastrada, tente novamente")    