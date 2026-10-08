gen = str(input("Para Prosseguirmos informe seu gênero [M / F]: ")).strip().upper()[0]
while gen not in 'MmFf':
    gen = str(input("Dados Inválidos! Por favor, informe novamente seu gênero: ")).strip().upper()[0]
if gen == "F":
    print("Opção {} escolhida! Gênero Feminino registrado com sucesso!".format(gen))
else:
    print("Opção {} escolhida! Gênero Masculino registrado com sucesso!".format(gen))
