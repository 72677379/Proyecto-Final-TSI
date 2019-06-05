import random 
def entrada():
    jugadores = int(input("¿Cuantos jugadores son? "))
    for x in range (1,jugadores+1):
      comprador = str(input("¿Cual es su nombre? "))
      cartillas = int(input("¿Cúantos cartillas desea comprar? "))
      if cartillas <= 3:
        monto_persona = cartillas * 5 
        print("el pozo a pagar es: ",monto_persona)
        for i in range(1,cartillas + 1):
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
                break
          print("Los números de su cartilla son: ", L)
      else:
        while cartillas > 3:
            a=int(input("Ingrese un numero menor o igual a 3: "))
            if a<=3:
              monto_persona = a * 5 
              print("el pozo a pagar es: ",monto_persona)
              for i in range(1,a + 1):
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
                      break
                print("Los números de su cartilla son:", L)
              break
            else:
              a=int(input("Ingrese un numero menor o igual a 3: "))
              monto_persona = a * 5 
              print("el pozo a pagar es: ",monto_persona)
              for i in range(1,a + 1):
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
                      break
                print("los números de su cartilla son:", L)
              break             
                
entrada()

