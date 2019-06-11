import random

def bolila(): 
  miLista = list(range(1,80))
  random.shuffle(miLista)
  
  miLista.append(miLista[:1])
  print(miLista)

bolila()

