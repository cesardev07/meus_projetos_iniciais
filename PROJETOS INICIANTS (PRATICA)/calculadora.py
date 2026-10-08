# O programa precisa cobrir as quatro operações matemáticas
# (soma, subtração, multiplicação e divisão), impedir a divisão
# por zero de quebrar a execução, avisar quando a opção escolhida
# for inválida, e permitir que o usuário repita o processo várias
# vezes antes de encerrar o programa por vontade própria.
# Não é necessário criar interface gráfica, salvar histórico em
# arquivo, nem usar bibliotecas externas —
# tudo deve funcionar via terminal, com input() e print().





print("Bem-Vindo a Multicalculadora!")

while True:
    num1 = float(input("Escolha o primeiro número: "))
    num2 = float(input("Escolha o segundo número: "))
    escolha = int(input('''Escolha uma operação:
[1] SOMA
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO :
'''))

    if escolha == 1:
        print("A soma de {} e {} é igual a {}".format(num1, num2, num1 + num2))
    elif escolha == 2:
        print("A subtração de {} e {} é igual a {}".format(num1, num2, num1 - num2))
    elif escolha == 3:
        print("A multiplicação de {} e {} é igual a {}".format(num1, num2, num1 * num2))
    elif escolha == 4:
        if num2 == 0:
            print("Números inválidos para divisão! Escolha outros valores.")
            continue  # volta ao menu
        print("A divisão de {} e {} é igual a {:.2f}".format(num1, num2, num1 / num2))
    else:
        print("Opção inválida!")

    opcao = input("Você gostaria de continuar na Multicalculadora? S/N: ").strip().upper()
    if opcao != "S":
        print("Até Breve")
        break
    print("Então Vamos Lá!")