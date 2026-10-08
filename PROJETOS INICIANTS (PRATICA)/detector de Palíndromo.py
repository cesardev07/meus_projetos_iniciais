frase = str(input("Digite uma frase: ")).strip().upper()
palavras =  frase.split()
junto = ''.join(palavras)
inverso = ''
#print("Você digitou a frase {}".format(frase))
print("Você digitou a frase {}".format(palavras))
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("Temos um palindromo!")
else:
    print("A frase não é palindromo")

