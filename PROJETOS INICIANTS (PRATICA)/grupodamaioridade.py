from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range (1,8):
    nasc = int(input("Em que ano a {} nasceu? ".format(pessoa)))
    idade = atual - nasc
    if idade >=21:
        totalmaior += 1
    else:
        totalmenor += 1
print ("Ao todo tivermos {} pessoas maiores de idade".format(totalmaior))
print("E tambem tivemos {} pessoas menores de idade".format(totalmenor))
