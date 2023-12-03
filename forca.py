import random


def imprimirCabecalho():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")


def imprimirTrofeu():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprimir_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def ler_arquivo():
    palavras = []
    arquivo = open("palavras.txt", "r")

    for linha in arquivo:
        palavras.append(linha.strip().lower())

    arquivo.close()
    return palavras


def gerar_palavra_secreta():
    palavras = ler_arquivo()
    idx = random.randrange(0, len(palavras))
    palavra_secreta = palavras[idx]
    return palavra_secreta


def chutar():
    chute = input('Qual letra? ').lower()
    return chute[0]


def forca():
    imprimirCabecalho()

    enforcou = False
    acertou = False

    palavra_secreta = gerar_palavra_secreta()
    letras_acertadas = []

    tamanho_palavra_secreta = len(palavra_secreta)
    qtde_letras_acertadas = 0

    while not enforcou and not acertou:
        chute = chutar()

        qtde_letras = palavra_secreta.count(chute)

        if qtde_letras > 0:
            letras_acertadas.append(chute)
            qtde_letras_acertadas = qtde_letras_acertadas + qtde_letras

        for letra in palavra_secreta:
            if letra in letras_acertadas:
                print(letra, end=" ")
            else:
                print('_', end=" ")

        print("")

        if tamanho_palavra_secreta == qtde_letras_acertadas:
            acertou = True

    imprimirTrofeu()
