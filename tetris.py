#Tetris

from tkinter import *

#dimensões
lado = 20
q_largura = 10
q_altura  = 20
largura = lado*q_largura
altura = lado*q_altura


class Peca:

    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        #self.grade[][]
        #self.size
        if(tipo == 1):
            self.grade = [[0,1,0], [0,1,1], [0,0,1]]
            self.size = 3


    #def vira(self):

    def desce(self):
        for i in range(self.size):
            for j in range(self.size):
                if Tela.grade[self.y+1][self.x]*self.grade[i][j] != 0:
                    return 0
        self.y = self.y + 1
        return 1

    #def direita(self):

    #def esquerda(self):


class Tela:
    def __init__(self):
        self.grade = [[0 for i in range(q_largura)] for j in range(q_altura)]

    #def elimina(self):

    #def desceLinha(self):

    #def addPecas(self):

    #def desenha(self):



class Game:

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura, height=altura, bg='black')
        self.canvas.pack()
        self.p = Peca(3, 1, 1)
        self.nump = 0
        self.t = Tela()


        #self.window.bind



    #def gira(self, event):

    #def moveEsquerda(self, event):

    #def moveDireita(self, event):

    def desenha(self):
        for i in range(self.p.size):
            print('')
            for j in range(self.p.size):
                print(self.p.grade[j][i], end='')
                if self.p.grade [j][i] != 0 :

                    self.canvas.create_polygon([(self.p.x+j)*lado, (self.p.y+i)*lado, (self.p.x+j)*lado+lado, (self.p.y+i)*lado, (self.p.x+j)*lado+lado, (self.p.y+i)*lado+lado, (self.p.x+j)*lado, (self.p.y+i)*lado+lado], fill='green')





    def run(self):

        while(True):
            self.canvas.delete('all')

            self.desenha()
            self.p.desce(self.t)

            self.canvas.after(150)
            self.window.update_idletasks()
            self.window.update()

g = Game()
g.run()







