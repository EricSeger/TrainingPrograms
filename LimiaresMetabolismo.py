# qual fonte de energia foi utilizada
# perguntar o tempo de fadiga, a intensidade, usar os dados de tempo.
# se não falou que cansou antes de 1min, perguntar mais dados.
# dados
# até 15s - creatina-fosfato
# 15s a 1min - Glicólise anaeróbia
# 1min a 20min - Glicólise aeróbia
# acima de 20min - Gordura
print('='*60)
print("Programa do Metabolismo")
print("Neste programa você escolhe um movimento para executar até cansar,"
      " enquanto cronometra\nquanto tempo levou para atingir a fadiga.\n"
      "Com estes dados,o programa retorna o tipo de metabolismo "
      "principal utilizado.")
print('='*60)
while True:
    nome = str(input("Digite o movimento que você realizou: "))
    print("O tempo será digitado no formato __min__s")
    print("Exemplos: se você cansou em 20 segundos, digite 0 nos minutos e 20 nos segundos. ")
    print("Se você cansou em 15min, digite 15 nos minutos e 0 nos segundos.")
    print("Se você cansou em 1min e 30s, digite 1 nos minutos e 30 nos segundos.")
    tempoM = int(input("Digite o(s) minuto(s): "))
    tempoS = int(input("Digite os segundos: "))
    tempo = (tempoM*60) + tempoS
    if (tempo <= 15):
        print("A principal rota metabólica foi a Creatina-Fosfato.\nEste exercício"
              "é indicado para treinar potência e força.")
    elif (tempo <= 60):
        print("A principal rota metabólica foi a Glicólise Anaeróbia.\nEste exercício"
              "é indicado para treinar força e hipertrofia.")
    elif (tempo <= 1200):
        print("A principal rota metabólica foi a Glicólise Aeróbia.\nEste exercício é"
              "indicado para treinar a resistência aeróbica e queima de gordura.")
    elif (tempo > 1200 ):
        print("A principal rota metabólica foi a Lipólise.\nEste exercício é indicado"
              " para treinar a queima de gordura.")
    f = str(input("Você quer continuar? [S/N]")).upper()
    if f in "nN":
        break
