import random   
lista = []
n = 0
def sacar(n):
    n += 1
    for n in range(n):
        lista.insert(n+1,random.randrange(0,80))
        return lista
    

alea = sacar(n)


alea.append(alea)
print(alea)