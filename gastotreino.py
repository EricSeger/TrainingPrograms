tabela = list()
borg1 = dict()
borg2 = dict()
borg3 = dict()
borg4 = dict()
borg5 = dict()

borg1["borg"] = 1
borg2["borg"] = 4
borg3["borg"] = 6
borg4["borg"] = 9
borg5["borg"] = 10

borg1["RFC"] = borg1["vo2"] = 0.25
borg2["RFC"] = borg2["vo2"] = 0.41
borg3["RFC"] = borg3["vo2"] = 0.55
borg4["RFC"] = borg4["vo2"] = 0.77
borg5["RFC"] = borg5["vo2"] = 0.91

borg1["metab"] = "Sub-aeróbio lipolítico"
borg2["metab"] = "Sub-aeróbio lipolítico"
borg3["metab"] = "Aeróbio lipolítico"
borg4["metab"] = "Aeróbio/anaeróbio glicolítico"
borg5["metab"] = "Anaeróbio glicolítico/Creatina-fosfato"

tabela.append(borg1.copy())
tabela.append(borg2.copy())
tabela.append(borg3.copy())
tabela.append(borg4.copy())
tabela.append(borg5.copy())

print("="*60)
print("Programa Gasto Calórico do Treino Funcional")
print("="*60)

borg = int(input("Digite o nível de esforço percebido: "))
while True:
    if borg > 10:
        borg = int(input("Digite um número inteiro entre 0 e 10:"))
    else:
        break
if borg == 0:
    borg = 0
elif borg == 1:
    borg = 0
elif borg in range(2,5):
    borg = 1
elif borg in range(5,7):
    borg = 2
elif borg in range(7,10):
    borg = 3
elif borg == 10:
    borg = 4

massa = float(input("Digite a massa corporal: "))
ingesta = int(input("Digite a ingesta calórica: "))
vo2max = float(input("Digite o vo2max: "))
FCrep = int(input("Digite a FC de Repouso: "))
FCmax = int(input("Digite a FC máxima: "))
taxa = float(input("Digite a Taxa metabólica basal: "))
# intensidade = float(input("Digite a intensidade "
#                          "do treino aeróbio desejada: "))
tempo = int(input("Digite o tempo de treino: "))
vo2treino = ((vo2max - 3.5)*tabela[borg]["RFC"]) + 3.5
MET = vo2treino/3.5
#gpm gasto calorico por minuto
gpm = (MET*massa)/60
GCtreino = gpm*tempo
GCdia = GCtreino + taxa

gasto = ingesta + 150
aerobio = gasto - GCdia
print(f"Kcal a gastar com treino aeróbio: {aerobio} kcal")
# print(f"Vo2 treino: {vo2treino}   MET: {MET}  GPM:{gpm}")
print(f"RFC = {(tabela[borg]['RFC'])*FCmax/100} bpm")
print(f"Tempo de treino com intensidade {tabela[borg]['RFC']}% é de : {tempo} minutos")
print(f"Gasto do Treino: {GCtreino}\nGasto Calórico do Dia {GCdia}")