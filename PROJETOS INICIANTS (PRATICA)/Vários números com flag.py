#66: Crie um programa que leia números inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

#(MODO GAMBIARRA)
#n = soma = 0
#while n != 999:
#    n = int(input("Digite um número: "))
#    soma += n
#soma -= 999
#print(f"A soma dos valores é {soma}")

soma = cont = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f"A soma dos {cont} valores foi {soma}!")
