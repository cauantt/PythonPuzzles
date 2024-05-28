import random
from time import sleep
from operator import itemgetter

ranking = []
boletim = {"p1": random.randint(1,6),
           "p2": random.randint(1,6),
           "p3": random.randint(1,6),
           "p4": random.randint(1,6)}

print("Valores sorteados: ")



ranking = sorted(boletim.items(), key=itemgetter(1), reverse=True)

for i, u in enumerate(ranking):
    print("{} lugar: jogador {} tirou {} no dado".format(i+1,u[0],u[1]))

    sleep(1)
