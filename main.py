import forca
import adivinhacao


def imprimirCabecalho():
    print("***************************")
    print("Escolha seu jogo!")
    print("***************************")


def selecionarJogo() -> int:
    jogo = int(input("Selecione um jogo? (1) Adivinhação (2) Forca: "))
    return jogo


def jogos():
    imprimirCabecalho()
    jogo = selecionarJogo()

    match jogo:
        case 1:
            adivinhacao.adivinhacao()
        case 2:
            forca.forca()


jogos()
