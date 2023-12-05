#Apresentação
print('\n\n\t\t--Estação do ano!--')
print('-'*45)

#Processamento
def verificar(dia):
    if dia < 31:
        return True

    else:
        return False

def obter_estacao(mes, dia):
    if (mes == 12 and dia >= 22) or (mes == 1 or mes == 2) or (mes == 1 or mes == 3 and dia < 20):
        print('Verão')
    elif (mes == 3 and dia >= 20) or (mes == 4 and mes == 5) or (mes == 6 and dia < 21):
        print('Outono')
    elif (mes == 6 and dia >= 21) or (mes == 7 and mes == 8) or (mes == 9 and dia < 23):
        print('Inverno')
    elif (mes == 9 and dia >=23) or (mes == 10 or mes == 11) or (mes == 12 and dia <22):
        print('Primavera')

# Saída

mes = int(input('\nInforme o mês:'))
dia = int(input('Informe o dia:'))
if (dia <= 31 and mes <= 12):
    estaçao = obter_estacao(mes, dia)

else:
    print('Més ou dia Invalido!')



