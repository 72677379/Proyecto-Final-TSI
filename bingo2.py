import random 
def entrada():
    n = int(input("¿Cuantos jugadores son?"))
    for x in range (1,n+1):
        x =str(input("Ingrese su nombre: "))
        x = str(input("Ingrese su numero de cartilla: "))
        L=[random.randint(0, 15)]
        i=1
        while i<15:
            x=random.randint(0,15)
            for j in range(0, len(L)):
                if L[j]==x:
                    break
            else:
                L.append(x)
                i+=1
        print("su numero es ",L)



entrada()


L=[random.randint(0, 15)]
i=1
while i<15:
  x=random.randint(0,15)
  for j in range(0, len(L)):
    if L[j]==x:
      break
  else:
    L.append(x)
    i+=1
print(L)