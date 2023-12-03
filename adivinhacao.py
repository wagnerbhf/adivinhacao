import random


def imprimirCabecalho():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


def selecionarDificuldade() -> int:
    nivel = int(input("Qual nível de dificuldade? (1) Fácil (2) Médio (3) Difícil"))
    return nivel


def gerar_numero_secreto() -> int:
    nivel = selecionarDificuldade()
    numero_secreto = random.randrange(1, 34)  # (1) Fácil

    match nivel:
        case 2:
            numero_secreto = random.randrange(1, 67)  # (2) Médio
        case 3:
            numero_secreto = random.randrange(1, 101)  # (3) Difícil

    return numero_secreto


def chutar() -> int:
    chute = int(input("Digite o seu número: "))
    print("Você digitou ", chute)
    return chute


def adivinhacao():
    imprimirCabecalho()
    numero_secreto = gerar_numero_secreto()
    chute = chutar()

    while numero_secreto != chute:
        if int(chute) < numero_secreto:
            print("Você errou! O seu chute foi menor do que o número secreto")
        else:
            print("Você errou! O seu chute foi maior do que o número secreto")

        chute = chutar()

    print("Você acertou")
