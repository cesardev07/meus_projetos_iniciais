somaidade = 0
mediaidade = 0
nomevelho = ''
totalmulher20 = 0
for pessoa in range (1,5):
    print("----{} PESSOA ----".format(pessoa))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    genero = str(input("Genero [M/F]: ")).strip()
    somaidade += idade
    if pessoa == 1 and genero in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if genero in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if genero in "Ff" and idade < 20:
        totalmulher20 += 1
mediaidade= somaidade / 4
print("A Média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho da lista é {}, tendo {} anos".format(nomevelho, maioridadehomem))
