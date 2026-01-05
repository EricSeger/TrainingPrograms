# Borg convertido em vo2 e limiares

tabela = list()
borg1 = dict()
borg2 = dict()
borg3 = dict()
borg4 = dict()
borg5 = dict()
LimiarA = LimiarB = float

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
print("Programa Escala de Borg e Gasto Calórico")
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
massa = int(input("Digite a massa corporal(kg): "))
FCrep = int(input("Digite a FC em repouso: "))
FCmax = int(input("Digite a FC máxima:"))
vo2M = float(input("Digite o vo2 máx: "))
tempo = int(input("Digite o tempo de treino: "))
metabolismo = float(input("Digite a taxa metabólica basal: "))
ingesta = float(input("Digite a ingesta calórica diária: "))
# RFC = ((FCmax - FCrep)*tabela[borg]["vo2"]) + FCrep
RFC = (FCmax - FCrep)
LimiarA = (RFC*0.5) + FCrep
LimiarB = (RFC*0.85) + FCrep
vo2treino = vo2M*(tabela[borg]["vo2"])
MET = vo2treino/3.5
GC = (MET*massa)/60
GCT = GC*tempo

print(f"Vo2 de treino: {vo2treino}\nRFC de treino?: {RFC}")
print(f"Gasto Calórico por minuto: {GC:.3} kcal, gasto calórico total: {GCT:.5} kcal")
print(f"Limiar Aeróbico: {LimiarA}\nLimiar Anaeróbico: {LimiarB}")
print(f"Gasto calórico do dia:{GCT + metabolismo}")
print(f"Déficit calórico: {ingesta - (GCT + metabolismo)}")

print(f"Vo2: {tabela[borg]['vo2']}")

#RFC = [(FCmáx - FCrep) x %intensidade] + FCrep
# vo2treino = VO2máx x %intensidade
#MET = VO2treino ÷ 3,5
# Gasto calórico = (MET x massa corporal) ÷ 60
# Gasto calórico total = gasto calórico x tempo do treinamento



print("Com este nível de esforço os parâmetros correspondentes são: ")
print(f'{tabela[borg]} indice {borg}')

# pegar FC repouso, FC máxima, Vo2máx. Com isso dá pra fazer
# gasto calórico tb, e saber as FC pra cada coisa de treino, bem como
#vo2 correspondente.