v1=int(input('Digite o primeiro valor: '))
v2=int(input('Digite o segundo valor: '))
soma = v1 + v2
subtrai = v1 - v2
multiplica = v1 * v2
divide = v1 / v2
x,y = divmod(v1, v2)
w =(v1**v2)

print('Soma {} e {} = {} '.format(v1,v2,soma))
print('Subtrai {} de {} = {} '.format(v1,v2,subtrai))
print('Multiplica {} por {} = {} '.format(v1,v2,multiplica))
print('Divide {} por {} = {} '.format(v1,v2,divide))
print("{} dividido por {} = {} e Resto da divisão de {} por {} = {} ".format(v1,v2,x,v1,v2,y))
print("%i elevado a %i = %i " % (v1,v2,w))

