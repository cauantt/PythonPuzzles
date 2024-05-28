def leiaint(num):
    while True:
        print("-=" * 15)
        num = str(input("Digite um numero:  "))
        if num.isdigit():
            return num
        else:

            print("\nERRO!!Digite outro numero\n")


n = leiaint("")
print("-=" * 15)
print(f"\nVoce digitou {n}")