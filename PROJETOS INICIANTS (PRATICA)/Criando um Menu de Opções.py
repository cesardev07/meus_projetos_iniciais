from time import sleep

n1 = int(input("Primeiro Valor: "))
n2 = int(input("Segundo Valor: "))
opcao = 0
while opcao != 5:
    print(''' 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA ''')
    opcao = int(input("Qual sua opção? "))

    sleep(2)
    if opcao == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é {}".format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 * n2
        print("O produto entre {} e {} é {}".format(n1,n2,produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("O Maior entre {} e {} é {}".format(n1,n2,maior))
    elif opcao == 4:
        print("Informe novamente os números: ")
        n1 = int(input("Primeiro Número: "))
        n2 = int(input("Segundo Número: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção Inválida! Tente Novamente")

print("Fim do Programa! Volte Sempre!")