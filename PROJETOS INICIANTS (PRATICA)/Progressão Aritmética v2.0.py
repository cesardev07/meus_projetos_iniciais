print("Gerador de P.A")
primerio = int(input("Primeiro Termo: "))
razão = int(input("Razão da PA: "))
termo = primerio
cont = 1
while cont <=10:
    print("{} -> ".format(termo), end='')
    termo += razão
    cont += 1
print("Fim")