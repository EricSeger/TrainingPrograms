massa = float(input("Digite a massa corporal: "))
ingesta = int(input("Digite a ingesta calórica: "))
FCrep = int(input("Digite a Frequência de Repouso: "))
FCmax = int(input("Digite a FC máx: "))
vo2max = float(input("Digite o vo2max: "))
taxa = float(input("Digite a Taxa metabólica basal: "))
# treino = float(input("Digite o gasto com o treino principal: "))
# intensidade = float(input("Digite a intensidade "
#                          "do treino aeróbio desejada: "))
while True:
    FCtreino = int(input("Digite a FC do treino: "))
    tempo = int(input("Digite o tempo de treino: "))
    intensidade = (FCtreino - FCrep)/(FCmax - FCrep)
    vo2treino = ((vo2max - 3.5)*intensidade) + 3.5
    MET = vo2treino/3.5
    #gpm gasto calorico por minuto
    gpm = (MET*massa)/60
    gasto = gpm*tempo
    RFC = ((FCmax - FCrep)*(intensidade/100)) + FCrep
    print(f"Kcal a gastar com treino aeróbio: {gasto} kcal")
    print(f"Vo2 treino: {vo2treino}   MET: {MET}  GPM:{gpm}")
    print(f"RFC : {RFC} = {RFC*100/FCmax}%")
    print(f"Tempo de treino com intensidade {intensidade*100:.2f}% é de : {tempo} minutos")
    sair = str(input("Deseja sair[s/n]?"))
    if sair in 'Ss':
        break
