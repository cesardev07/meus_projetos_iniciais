n = 0
cont = 0
soma = 0
n = int(input("Digite um número [ao digitar 999 o programa finaliza]: "))
while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um número [ao digitar 999 o programa finaliza]: "))
print ("Você digitou {} números e a soma entre esses é igual a {}".format(cont, soma))
