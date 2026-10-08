from random import randint
PC = randint(0,10)
print("Bem-Vindo ao Teste de IA da MKN Corp. Faremos um \npequeno jogo de advinhação, vamos ver quantas\ntentativas precisará para acertar.")
acertou = False
tentativas = 0
while not acertou:
    player = int(input("Qual o seu palpite? "))
    tentativas += 1
    if player == PC:
        acertou = True
        print("Acertou! Foram {} tentativas até acertar!".format(tentativas))
    else:
        if player > PC:
            print("O número foi maior que o escolhido, tente novamente.")
        else:
            print("O número foi menor que o escolhido, tente novamente.")

