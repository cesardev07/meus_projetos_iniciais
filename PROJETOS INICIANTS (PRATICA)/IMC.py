peso = float(input("Qual o seu peso? "))
altura = float(input ("Qual sua altura? "))
imc = peso / (altura ** 2)

print("o IMC dessa pessoa é {:.2f}".format(imc))

if imc < 18.5:
    print("Esta pessoa está ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("Esta pessoa está com PESO IDEAL")
elif 25 <= imc < 30:
    print("Esta pessoa está com SOBREPESO")
elif 30 <= imc < 40:
    print("Esta pessoa está com OBESIDADE")
elif imc >= 40:
    print("Esta pessoa está com OBESIDADE MÓRBIDA!")
