import math
s = 0
FCmax = 0
TMB = 0
gordura = 0
MM = 0
vo2max = 0
FCdepre = 0

#Coleta de dados do cliente
nome = str(input("Nome: "))
data = str(input("Data: (dd/mm/aaaa:)"))
idade = int(input("Idade: "))
massa = float(input("Digite a massa corporal (kg): "))
estatura = float(input("Digite a estatura(cm): "))
CA = float(input("Digite a Circunferência de Abdômen (CA, cm): "))
CG = float(input("Digite a Circunferência do Quadril (CQ, cm): "))
CP = float(input("Digite a Circunferência do Punho (CP, cm): "))
Cpesc=float(input("Digite a Circunferência do Pescoço(Cpc, cm): "))
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
# 1 - Protocolo de Penroe, Nelson & Fisher e Coté & Wilmore (%gordura)
if sexo in "Ff":
    gordura = ((0.55*CG) - (0.24*estatura) + (0.28*CA) - (8.43))
    MM = massa - ((massa*gordura)/100)

if sexo in "Mm":

    MM = (41.955 + (1.038786*massa)) - (0.82816*(CA - CP))
    gordura = ((massa - MM)*100)/massa

# 2 - Protocolo de Dotson e Davis, 1991 (adaptado por torres 1998)
# G% Homens = +[85,20969 . log (AB - Pç)] - [69,73016 . log (estatura em polegadas)] + 37,26673 (r=0,90) (S.E = 3,52%)
# {Obs: AB = Circ. abdome e Circ. Pç = pescoço}
# G% Mulheres= +[161,27327 . log (AB + GL- Pç)] - [100,81032 . log (estatura em polegadas)] - 69,55016 (r=0,85) (S.E = 3,64%)
# {Obs: AB = Circ. abdome; Circ. Pç = pescoço e GL = quadril}
if sexo in "Mm":
    gordura = (85.20969* (math.log(CA - Cpesc))) - (69.73016*(math.log(estatura*0.3937))) + 37.26673

if sexo in "Ff":
    gordura = (161.27327* (math.log(CA +CG - Cpesc))) - (100.81032*(math.log(estatura*0.3937))) - 69.5501

# % gordura para pessoas obesas
# fonte: Wetman e col., 1988
IMC = massa/(estatura*estatura)
if IMC > 30:
    if sexo in "mM":
        gordura = (0.31457*CA) - (0.10969*massa) + 10.8336
    if sexo in "Ff":
        gordura = (0.11077*CA) - (0.17666*estatura) + (0.14354*massa) + 51.03301
        MM = massa - ((massa*gordura)/100)
