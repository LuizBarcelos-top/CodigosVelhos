""" linha = str(input(''))
divisa = linha.split()
X = float(divisa[0])
Y = float(divisa[1])

if (X > 0) and (Y > 0):
    print('Q1')

elif (X > 0) and (Y < 0):
    print('Q4')

elif (X < 0) and (Y > 0):
    print('Q2')

elif (X < 0) and (Y < 0):
    print('Q3')

elif (X == 0 == Y):
    print('Origem')

elif (X == 0):
    print('Eixo X')

elif (Y == 0):
    print('Eixo Y')

x,y=map(float, input().split())
if (x==y==0):
    print("Origem")
elif(x==0):
    print("Eixo X")
elif(y==0):
    print("Eixo Y")
elif(x>0)and(y>0):
    print("Q1")
elif(x<0)and(y>0):
    print("Q2")
elif(x<0) and (y<0):
    print("Q3")
elif(x>0)and(y<0):
    print("Q4")
x,y=map(float, input().split())
print(f'{x} {y}')
"""



