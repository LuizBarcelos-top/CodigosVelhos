#linha = str(input('Digite um número: '))
#divisa = linha.split()
def estado():
    print("Nome: %s, Símbolo: %s - %i pontos" % (nomeJogadorA, simboloJogadorA, pontosJogadorA))
    print("Nome: %s, Símbolo: %s - %i pontos" % (nomeJogadorB, simboloJogadorB, pontosJogadorB))


def iniciaLista():
    return ["-"] * 9


def desenha():
    conta = 0
    while conta <= 6:
        print("_________________________________\n")
        print("|    %s  |   %s  |   %s  |\n" % (tabela[conta], tabela[conta + 1], tabela[conta + 2]))
        conta = conta + 3
    print("_________________________________\n")


def indiceLista(linha, coluna):
    return linha * 3 + coluna


def posicaoVazia(linha, coluna):
    i = indiceLista(linha, coluna)

    if tabela[i] == "-":
        return True
    else:
        return False


def acertou(linha, coluna):
    pos1 = indiceLista(linha, 0)
    pos2 = indiceLista(linha, 1)
    pos3 = indiceLista(linha, 2)
    print(tabela)
    if tabela[pos1] == tabela[pos2] and tabela[pos2] == tabela[pos3]:
        print("1")
        return True
    else:
        pos1 = indiceLista(0, coluna)
        pos2 = indiceLista(1, coluna)
        pos3 = indiceLista(2, coluna)
        if tabela[pos1] == tabela[pos2] and tabela[pos2] == tabela[pos3]:
            print("2")
            return True
        else:
            if linha == coluna:
                pos1 = indiceLista(0, 0)
                pos2 = indiceLista(1, 1)
                pos3 = indiceLista(2, 2)
                if tabela[pos1] == tabela[pos2] and tabela[pos2] == tabela[pos3]:
                    print("3")
                    return True
                else:
                    print("4")
                    return False
            else:
                if coluna == 2 - linha:
                    pos1 = indiceLista(2, 0)
                    pos2 = indiceLista(1, 1)
                    pos3 = indiceLista(0, 2)
                    if tabela[pos1] == tabela[pos2] and tabela[pos2] == tabela[pos3]:
                        print("5")
                        return True
                    else:
                        print("6")
                        return False


def tentativa(simb, linha, coluna):
    desenha()
    i = indiceLista(linha, coluna)

    if posicaoVazia(linha, coluna):
        tabela[i] = simb
        desenha()
        if acertou(linha, coluna):
            return 1
        else:
            return 0
    else:
        return -1


nomeJogadorA = input("Digite o nome do primeiro jogador ")
simboloJogadorA = "X"
nomeJogadorB = input("Digite o nome do segundo jogador ")
simboloJogadorB = "O"
continua = 0
pontosJogadorA = 0
pontosJogadorB = 0
tabela = iniciaLista()
jogador = nomeJogadorA
simbolo = simboloJogadorA
while continua != 2:
    cod = 0
    tabela = iniciaLista()
    estado()
    while cod != 1:
        print("Jogada de: ", jogador)
        linha = int(input("Linha? "))
        coluna = int(input("Coluna? "))
        cod = tentativa(simbolo, linha, coluna)
        print(cod)
        if cod == -1:
            print("Posição Inválida. Tente novamente")
        else:
            if cod == 1:
                pontos = 1
            else:
                pontos = 0
            if jogador == nomeJogadorA:
                jogador = nomeJogadorB
                simbolo = simboloJogadorB
                pontosJogadorA = pontosJogadorA + pontos
            else:
                jogador = nomeJogadorA
                simbolo = simboloJogadorA
                pontosJogadorB = pontosJogadorB + pontos
    continua = int(input("Continua? (1- sim/ 2- não)"))

