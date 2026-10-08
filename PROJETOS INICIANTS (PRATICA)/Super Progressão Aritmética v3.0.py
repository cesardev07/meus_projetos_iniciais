print("Gerador de P.A")
primerio = int(input("Primeiro Termo: "))
razão = int(input("Razão da PA: "))
termo = primerio
cont = 1
total = 0
mais = 10
# esse "mais" indica quantos termos iniciais a PA terá
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end='')
        termo += razão
        cont += 1
    print("???")
    mais = int(input("Você gostaria de Acrescentar mais termos? "))
print("Progressão Finalizada com {} termos".format(total))
