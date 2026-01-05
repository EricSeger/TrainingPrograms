# Avaliação pre treino
s = 0
FCmax = 0
TMB = 0
gordura = 0
MM = 0
vo2max = 0
FCdepre = 0
#Coleta de dados do cliente
nome = str(input("Nome: "))
data = str(input("Data: (dd/mm/aaaa:"))
idade = int(input("Idade: "))
massa = float(input("Digite a massa corporal (kg): "))
estatura = float(input("Digite a estatura(m): "))
sexo = str(input("Digite o Sexo [M/F]: "))
while True:
    if sexo not in 'MmFf':
        sexo = str(input("Digite um caracter válido M ou F: "))
    else:
        break
if sexo in 'Mm':
    s = 1
elif sexo in 'Ff':
    s = 0
FCrep = int(input("Digite a Frequencia Cardíaca de Repouso: "))
CA = float(input("Digite a Circunferência de Abdômen (CA, cm): "))
CG = float(input("Digite a Circunferência do Quadril (CQ, cm): "))
CP = float(input("Digite a Circunferência do Punho (CP, cm): "))
ingesta = int(input("Digite a ingesta calórica diária: "))

print("Métodos de Vo2máx:")
print("1 - Já tenho este valor.\n2- Cálculo pelo índice de atividade física.\n"
      "3 - Protocolo de Caminhada\n4 - Teste de Cooper\n5 - Teste de Esteira sem "
      "inclinação.\n6 - Teste de Esteira com inclinação\n7 - Teste de Cicloergômetro")
i = int(input("Digite o método escolhido para Vo2max:"))
if i == 1:
    vo2max = float(input("Digite o valor do vo2máx: "))
elif i == 2:
    # calculo do vo2max pelo indice
    atividade = int(input("Digite o índice de atividade física: "))
    vo2max = 34.142 + (0.133 * idade) - (0.005 * (idade * idade)) + (11.403 * s) + \
             (1.463 * atividade) + (9.17 * (estatura / 100)) - (0.254 * massa)
elif i ==3:
    tempo = int(input("Digite o tempo do teste(min): "))
    FCteste = int(input("Digite a FC no fim do teste: "))
    if sexo in "Mm":
#   vo2max = 6.952 + (0.0091*(massa*2.205)) – (0.0257*idade) + (0.5955*1) – (0.2240*tempo) – (0.0115*FCteste)
       vo2max = 132.853 - (0.0769*(massa*2.205)) - (0.3877*idade) + (6.315*1) - (3.2649*tempo) - (0.1565*FCteste)
    if sexo in "Ff":
        vo2max = 132.853 - (0.0769*(massa * 2.205)) - (0.3877 * idade) + (6.315*0) - (3.2649*tempo) - (0.1565*FCteste)
elif i ==4:
    distancia = float(input("Digite a distancia percorrida em m:"))
    vo2max = (distancia - 504.9)/44.73

elif i ==5:
    j = int(input("Fases de teste:\n1-Caminhando até 7km/h\n2-Correndo acima de 7 km/h\n"
                  "Digite o tipo: "))
    FCmax = int(input("Digite a FC max: "))
    if j == 1:
        velocidade = float(input("Digite a velocidade máxima(km/h): "))
        print(f"Velocidade em m/min:{velocidade*16.67} m/min ")
        vo2max = ((velocidade*16.67)*0.1) + 3.5
    elif j == 2:
        velocidade = float(input("Digite a velocidade máxima(km/h): "))
        print(f"Velocidade em m/min:{velocidade * 16.67} m/min ")
        vo2max = ((velocidade*16.67)*0.2) + 3.5
elif i == 6:
    velocidade = float(input("Digite a velocidade (km/h): "))
    inclinacao = float(input("Digite a inclinação: "))
    FCmax = int(input("Digite a FC max: "))
    vo2max = (velocidade*0.1) + (inclinacao*1.8) + 3.5
elif i == 7:
    carga = int(input("Digite a carga máxima: "))
    vo2max = ((12*carga) + 200)/massa
    FCmax = int(input("Digite a FCmax: "))
#Cálculo da Taxa Metabólica Basal:
if idade in range(10,19):
    if sexo in 'Ff':
        TMB = (12.2*massa) + 746
    elif sexo in 'Mm':
        TMB = (17.5*massa) + 651
elif idade in range (19, 31):
    if sexo in 'Ff':
        TMB = (14.7*massa) + 496
    if sexo in 'Mm':
        TMB = (15.3*massa) + 679
elif idade in range(31, 61):
    if sexo in 'Ff':
        TMB = (8.7*massa) + 829
    if sexo in 'Mm':
        TMB = (8.7*massa) + 879
elif idade > 60:
    if sexo in 'Ff':
        TMB = (10.5*massa) + 596
    if sexo in 'Mm':
        TMB = (13.5*massa) + 487
# calculo da Frequência Cardíaca Máxima e do Percentual de Gordura
# Métodos de % Gordura

# 1 - Protocolo de Penroe, Nelson & Fisher e Coté & Wilmore (%gordura)
if sexo in "Ff":

    if i < 5:
        FCmax = 192 - (0.7*idade)
    gordura = ((0.55*CG) - (0.24*estatura) + (0.28*CA) - (8.43))
    MM = massa - ((massa*gordura)/100)

if sexo in "Mm":
#    CP = float(input("Digite a Circunferência do Punho (CP, cm): "))
    MM = (41.955 + (1.038786*massa)) - (0.82816*(CA - CP))
    gordura = ((massa - MM)*100)/massa
    if i < 5:
        FCmax = 201 - (0.6*idade)

# 2 - Protocolo de Dotson e Davis, 1991 (adaptado por torres 1998)
# G% Homens = +[85,20969 . log (AB - Pç)] - [69,73016 . log (estatura em polegadas)] + 37,26673 (r=0,90) (S.E = 3,52%)
# {Obs: AB = Circ. abdome e Circ. Pç = pescoço}
# G% Mulheres= +[161,27327 . log (AB + GL- Pç)] - [100,81032 . log (estatura em polegadas)] - 69,55016 (r=0,85) (S.E = 3,64%)
# {Obs: AB = Circ. abdome; Circ. Pç = pescoço e GL = quadril}
#if sexo in "Mm":
#    gordura = (85.20969*)


# % gordura para pessoas obesas
# fonte: Wetman e col., 1988
IMC = massa/(estatura*estatura)
if IMC > 30:
    if sexo in "mM":
        gordura = (0.31457*CA) - (0.10969*massa) + 10.8336
    if sexo in "Ff":
        gordura = (0.11077*CA) - (0.17666*estatura) + (0.14354*massa) + 51.03301
        MM = massa - ((massa*gordura)/100)



#Cálculo das Frequências Cardícas dos limiares aeróbico anaeróbico
FCLimiarA = ((FCmax - FCrep)*0.5) + FCrep
FCLimiarB = ((FCmax - FCrep)*0.85) + FCrep

# cálculo da Frequência para antidepressivo:
FCdepre = ((FCmax - FCrep)*0.75) + FCrep

# Limite superior da FC da faixa que queima mais gordura
FCGordura = ((FCmax - FCrep)*0.65) + FCrep

# Exibição dos Resultados
print(f"Vo2máx: {vo2max:.2f} ml/(kg x min)              Classificação: ")
print(f"FCmax = {FCmax:.0f} bpm")
print(f"FC do limiar Aeróbio: {FCLimiarA:.0f} bpm")
print(f"FC do limiar Anaeróbico: {FCLimiarB:.0f} bpm")
print(f"Faixa de FC que utiliza predominantemente gordura: "
      f"{FCLimiarA:.0f} bpm até {FCGordura:.0f} bpm")
print(f"Para um efeito antidepressivo a FC deve manter-se em aproximadamente {FCdepre:.0f} rpm")
print(f"O percentual de gordura é: {gordura:.2f}%             Classificação:  ")
print(f"A massa livre de gordura é: {MM:.2f} kg")
print(f"A massa gorda é {(massa - MM):.2f} kg")
print(f"A Taxa de Metabolismo Basal é: {TMB:.2f} kcal")
print(f"O Déficit Calórico sem treino é: {(ingesta - TMB):.2f} kcal")


# Protocolo de Wetman e col., 1988 para pessoas obesas
# G% Homens = [0,31457 x (abdome)] - [ 0,10969 x (P) ] + 10,8336
# G% Mulheres= [0,11077 x (abdome)]- [ 0,17666 x (A) ] + [0,14354 x (P) + 51,03301


#Índice de Atividade Física:

#0 - Evita caminhar ou se esforçar. Por exemplo, sempre usa o elevador, usa o carro
# sempre que possível ao invés de caminhar.

#1 - Caminha por prazer, normalmente usa escadas, às vezes se exercita
#a ponto de ficar ofegante.

#2 - Normalmente participa de atividades não formais, ou de trabalho,
#que envolvam moderada atividade física, como caminhar para exercitar
# -se, montar à cavalo, ginástica, boliche, hidroginástica, musculação
# e afazeres domésticos. 10 a 60 minutos por semana.

# 3 - Normalmente participa de atividades não formais, ou de trabalho,
# que envolvam moderada atividade física, como caminhar para exercitar-se,
# montar à cavalo, ginástica, boliche,hidroginástica, musculação
# e afazeres domésticos. Mais de 1 hora por semana.

# 4 - Corre menos que 1,5 km por semana ou pratica atividades como
# natação, ciclismo, remo, pular corda, futebol, voleibol, tênis,
# basquetebol ou handebol por menos de 30 minutos por semana.

# 5 - Corre 1,5 a 8,0 km por semana ou pratica atividades como natação,
# ciclismo, remo, pular corda, futebol, voleibol, tênis, basquetebol
# ou handebol por 30 a 60 minutos por semana.

#6 - Corre 8,0 a 30,0 km por semana ou pratica atividades como natação,
# ciclismo, remo, pular corda, futebol, voleibol, tênis, basquetebol
# ou handebol por 1 a 3 horas por semana.

#7 - Corre mais de 30,0 km por semana ou pratica atividades como natação,
# ciclismo, remo, pular corda, futebol, voleibol, tênis, basquetebol
# ou handebol por mais de 3 horas por semana