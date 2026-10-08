#67: Faça um programa que mostre a tabuada de vários
# números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o
# número solicitado for negativo.

#(VERSAO GUANABARA)
while True:
    n = int(input("De qual número quer ver a tabuada? "))
    print("~" * 30)
    if n < 0:
        break
    for c in range (1,11):
        print (f"{n} x {c} = {n*c}")
    print("~" * 30)
print("TABUADA ENCERRADA...")

#(MINHA VERSAO FEAT. CLAUDE)
while True:
    n = int(input("De qual número quer ver a tabuada? "))
    print("~" * 30)
    if n < 0:
        break
    inicio = int(input("Multiplicar a partir de qual número? "))
    quantidade = int(input("Quantas multiplicações quer ver? "))
    for c in range(inicio, inicio + quantidade):
        print(f"{n} x {c} = {n*c}")

    print("~" * 30)

print("TABUADA ENCERRADA...")