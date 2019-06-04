import random 
def entrada():
    jugadores = int(input("¿Cuantos jugadores son? "))
    for x in range (1,jugadores+1):
      comprador = str(input("¿Cual es su nombre? "))
      cartillas = int(input("¿Cúantos cartillas desea comprar? "))

      while cartillas > 3:
            a=int(input("Ingrese un numero menor o igual a 3 : "))
            if a<=3:
              monto_persona = (a * 5)*jugadores
              print("el monto total a pagar es : ",monto_persona)
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
                    print(jugadores, "Su codigo de cartilla es: ",L)
                    break
              break 

    if cartillas <= 3:
        monto_persona = (cartillas * 5)*jugadores
        print("el monto total a pagar es  : ",monto_persona)
    else:
        while cartillas > 3:
            a=int(input("Ingrese un numero menor o igual a 3 : "))
            if a<=3:
              monto_persona = (a * 5)
              print("el monto tatal a pagar es : ",monto_persona)
              
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
                    print("Su codigo de cartilla es: ",L)
                    break

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
print("Estas son las bolillas obtenidas", L)