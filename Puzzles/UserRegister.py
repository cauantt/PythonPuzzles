pessoa = {}
anobase = 2024




pessoa["nome"] = str(input("\nDigite o nome: "))
nasc = int(input("\nDigite o ano de nascimento: "))
pessoa["idade"] = anobase - nasc


cart = int(input("\nDigite numero da carteira de trabalho: "))
if cart != 0:
    pessoa["carteira"] = cart
    pessoa["anocon"] = int(input("\nDigite o ano de contratação: "))
    pessoa["salario"] = int(input("\nDigite seu salario: "))



aposentar = (pessoa["anocon"]-anobase) + 35 + pessoa["idade"]

for i, v in pessoa.items():
    print("O valor de {} é {}".format(i,v))
print("vai se aposentar com {}".format(aposentar))
