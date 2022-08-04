def enfeite():
    print('-=-'*60)
lista = []
num = int(input('Valor: '))
while num > 0:
    lista.append(num)
    num = int((input('Valor: ')))
m = lista[0]
print('M = {}'.format(m))
ind = 0
ocorre = 0
for i in range (1, len(lista)):
    if lista[i]<m:
        m = lista[i]
        print('M = {}'.format(m))
        ind = [i]
        ocorre = 1
    elif lista [i] == m:
        ocorre += 1
        ind.append(i)
print('IND = {}'.format(ind))
print('Ocorre = {}'.format(ocorre))
print('M = {}'.format(m))
