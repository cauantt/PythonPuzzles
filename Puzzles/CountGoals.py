jogador = {}
soma = 0
gols = []
v = 0
jogador["nome"] = str(input("Digite o nome do jogador: "))
jogador["numpartidas"] = int(input("Digite a quantidade de partidas: "))

for i in range(jogador["numpartidas"]):
    print("Quantos gols ele fez na partida {}: ".format(i+1), end = "")
    gol = int(input("?"))
    soma += gol
    gols.append(gol)
jogador["gols"] = gols
print("-=" * 15)
print(jogador)
print("-=" * 15)
for i, v in enumerate(gols):
    print("o campo {} tem o valor {}.".format(i,v))
print("-=" * 15)
print("o jogador jogou {} jogos.".format(jogador["numpartidas"]))
for i, v in enumerate(jogador["gols"]):
    print("  >>> na partida {}, fez {} gols".format(i+1,v))
print("Fez um total de {} gols".format(soma))
