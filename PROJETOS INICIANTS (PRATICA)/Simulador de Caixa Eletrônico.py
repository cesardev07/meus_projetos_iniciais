#71: Crie um programa que simule o funcionamento de
# um caixa eletrônico. No início, pergunte ao usuário qual
# será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédul
# as de R$50, R$20, R$10 e R$1.

print('-'*30)
print("Bem-Vindo ao setor MKN de Finanças!")
print('-'*30)
valor = int(input("Qual valor quer retirar? R$ "))
total = valor
ced = 50 #(nesse exemplo o valor maximo é 50)
totalced = 0 #(contator criado para quantas cedulas usar)

while True:
    if total >= ced:
       total -= ced
       totalced += 1
    else:
        if totalced > 0:
            print(f"Total de {totalced} cédulas de R$ {ced:.2f}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
