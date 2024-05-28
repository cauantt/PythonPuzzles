cont50 = 0 
cont20 = 0 
cont10 = 0 
cont5 = 0 
cont1 = 0 
saque = int(input("Digite quanto voce deseja sacar:\n"))
print("seu saque vai ser de: {}".format(saque))
while True:

    if saque >= 50:
        cont50 += 1 
        saque -= 50 
    elif saque < 50 and saque >= 20:
        cont20 += 1
        saque -= 20
    elif saque < 20 and saque >= 10:
        cont10 += 1
        saque -= 10
    elif saque < 10 and saque >= 5:
        cont5 += 1
        saque -= 5
    elif saque < 5 and saque >= 1:
        cont1 += 1
        saque -= 1
    elif saque == 0:
        break

print("Notas de 50 reais: {}".format(cont50))
print("Notas de 20 reais: {}".format(cont20))
print("Notas de 10 reais: {}".format(cont10))
print("Notas de 5 reais: {}".format(cont5))
print("Notas de 1 real: {}".format(cont1))