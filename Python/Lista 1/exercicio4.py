# Exercício 4
# Faça um programa que receba como entrada dois valores entre os caracteres R, U e I, e calcule o terceiro
# valor com base na primeira lei de Ohm.
# A Primeira Lei de Ohm postula que um condutor ôhmico (resistência constante) mantido à temperatura
# constante, a intensidade (i) de corrente elétrica será proporcional à diferença de potencial (ddp) aplicada
# entre suas extremidades. Ou seja, sua resistência elétrica é constante. Ela é representada pela seguinte fórmula:
# R = U/I

print("--- Calculadora Lei de Ohm---")
valor_correto = False
resistencia_ok = False
corrente_ok = False
tensao_ok = False
calculo_escolhido = int(input("Digite o número de qual valor você gostaria de descobrir: \n 1-Tensão \n 2-Resistência \n 3-Corrente \n"))

if calculo_escolhido == 1: #Tensão: U = R.I | Volts
    while valor_correto == False:
        if resistencia_ok == False:
            resistencia = (float(input("Digite o valor da resistência: "))) #R
            if resistencia < 0: 
                print("O valor não pode ser negativo")
            else:
                resistencia_ok = True
              
        if resistencia_ok:
            corrente = (float(input("Digite o valor da corrente elétrica: "))) #I
            if corrente < 0:
                print("O valor não pode ser negativo")
                valor_correto = False
            else:
                corrente_ok = True
               
        if resistencia_ok and corrente_ok:
            valor = resistencia * corrente
            print("O valor da Tensão é de " + str(valor) + " Volts")
            valor_correto = True

elif calculo_escolhido == 2: #Resistência: R = U/I | Ohms
    while valor_correto == False:
        if tensao_ok == False:    
            tensao = (float(input("Digite o valor da tensão: "))) #U
            if tensao < 0:
                print("O valor não pode ser negativo")
            else:
                tensao_ok = True

        if tensao_ok:    
            corrente = (float(input("Digite o valor da corrente elétrica: "))) #I
            if corrente < 0:
                print("O valor não pode ser negativo")
                valor_correto == False
            else:
                corrente_ok = True    

        if corrente_ok and tensao_ok:
            valor = tensao / corrente
            print("O valor da Resistência é de " + str(valor) + " Ohms")
            valor_correto = True

elif calculo_escolhido == 3: #Corrente: I = U/R | Amper
    while valor_correto == False:
        if tensao_ok == False:
            tensao = (float(input("Digite o valor da tensão: "))) #U
            if tensao < 0:
                print("O valor não pode ser negativo")
            else:
                tensao_ok = True

        if tensao_ok:
            resistencia = (float(input("Digite o valor da resistência: "))) #R
            if resistencia < 0:
                print("O valor não pode ser negativo")
                valor_correto == False
            else:
                resistencia_ok = True    

        if tensao_ok and resistencia_ok:
            valor = tensao / resistencia
            print("O valor da Corrente Elétrica é de " + str(valor) + " Amper")
            valor_correto = True
else:
    print("Opção inválida")    


