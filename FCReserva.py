# Reserva da Frequência Cardíaca (RFC)
# RFC = FCmáxima - FC repouso
# FC máxima? Idade. Repouso é o que o programa pergunta e é o que muda com o treino
# Limiar aeróbio: RFC * 50% + FCRepouso
# Limiar anaeróbio: RFC*85% + FCRepouso
# para qualquer % de limiar.
# anotar as correspondências de intervalo dos metabolismos.
# MET = vo2/3.5
# Gasto calórico = (MET*massa corporal)/60
print("Cálculo da FC de treino")

idade = int(input("Digite a idade: "))
massa = float(input("Digite o peso em kg: "))
FCrepouso = int(input("Digite a frequência cardíaca de repouso: "))
FCmaxima = int(input("Digite a frequência cardíaca máxima: "))

RFC = FCmaxima - FCrepouso
LimiarA = (RFC*0.5) + FCrepouso
LimiarB = (RFC*0.85) + FCrepouso
# GastoCal = ((vo2/3.5)*massa)/60
print(f"Limiar Aeróbico: {LimiarA}\nLimiar Anaeróbico: {LimiarB}")