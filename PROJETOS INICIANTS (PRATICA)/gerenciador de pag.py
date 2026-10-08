print("Bem-Vindo à {}!\nAqui teremos do que precisa!".format("MKN STORE"))
preço = float(input("Insira o Valor de seu Carrinho: R$ "))
print ('''Selecione a forma de pagamento:
[1] À vista (dinherio/cheque)
[2] À vista (cartão)
[3] 2x em Cartão
[4] 3x ou mais em Cartão''')
opçao = int(input("Qual a opção escolhida? "))

if opçao == 1:
    print("Opção 1 Escolhida! o Valor da compra será de R$ {}!,\ncom desconto APLICADO de 10%!".format(preço - (preço * 0.10)))
elif opçao == 2:
    print("Opção 2 Escolhida! o Valor da compra será de R$ {}!,\ncom desconto APLICADO de 5%!".format(preço - (preço * 0.05)))
elif opçao == 3:
    parc = preço / 2
    print("Opção 3 Escolhida! No Valor da compra NÃO HAVERÁ APLICAÇÃO DE TAXAS! Sendo parcelada em 2x será R$ {}, do Valor total: R$ {}!".format(parc, preço))
elif opçao == 4:
    parce = int(input("Quantas parcelas? "))
    totalparce = preço / parce
    print("Opção 4 Escolhida! No Valor da compra HAVERÁ\nAPLICADAÇÃO DE TAXA de 20% de JUROS!,\nsendo PARCELADA EM {}x com Valor de R$ {:.2f}\nsendo o Valor Total da Compra R$ {}!".format(parce,totalparce,preço + (preço * 0.20)))
else:
    total = 0
    print ("Opção Selecionada Inválida! Tente Novamente!")