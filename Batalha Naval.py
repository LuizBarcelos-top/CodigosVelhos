from random import randint

grade = []

for i in range(0, 5):
    grade.append(["O"]*5)

def print_grade(grade):
    for i in grade:
        print (" ".join(i))

print_grade(grade)

def random_fileira(grade):
    return randint(0,len(grade)-1)
def random_coluna(grade):
    return randint(0, len(grade[0]) -1)

navio_fileira = random_fileira(grade)
navio_coluna = random_coluna(grade)


convidado_fileira = int(input('Convidado Fileira: '))
convidado_coluna = int(input('Convidado Coluna: '))

print (navio_coluna)
print (navio_fileira)

for turn in range(4):
    print('Vire', turn+1)

    if convidado_fileira == navio_fileira and convidado_coluna == navio_coluna:
        print('Parabéns! Você acertou o meu navio')
    else:
        if convidado_fileira > range(5) or convidado_coluna > range(5):
            print('Caramba, isso nem é o oceano')
        elif grade[convidado_fileira] [convidado_coluna]=='x':
            print('Você já acertou esse')
        else:
            print('Você errou!')
            grade[convidado_fileira] [convidado_coluna]='x'
            if turn ==3:
                print('Game Over')

        print_grade(grade)




