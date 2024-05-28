dicio = {}
lista = []
soma = 0
listam = []
cont = 0
listaid = []
while True:
    menu = int(input("Deseja inserir uma pessoa (1/2): "))
    if menu == 2:
        break
    else:

        dicio["nome"]  = str(input("Digite o nome da pessoa: "))
        dicio["sexo"]  = str(input("Digite o sexo da pessoa (M/F): "))
        dicio["idade"] = int(input("Digite a idade da pessoa: "))
        cont += 1
        soma += dicio["idade"]
        if dicio['sexo'] == 'F':
            listam.append(dicio.copy())

        lista.append(dicio.copy())

media = soma/cont
for p in lista:
    if p['idade'] > media:
        listaid.append(p['idade'])


print("{} pessoas lidas".format(cont))
print("A média da idade das pessoas é {}".format(media))
