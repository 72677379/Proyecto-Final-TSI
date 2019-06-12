import random
import sys
import os
import sys

def entrada():
    jugadores = int(input("¿Cuantos jugadores son? "))
    suma =0
    for x in range (1,jugadores+1):
      comprador = (input("¿Cual es su nombre? "))
      cartillas = int(input("¿Cúantos cartillas desea comprar? "))
      if cartillas <= 3:
        monto_persona = cartillas * 5
        suma=suma+monto_persona
        print("el pozo a pagar es: ",monto_persona)
        for i in range(1,cartillas + 1):
          miLista=list(range(1,80))  #creamos una lista del 1 al 80  
          random.shuffle(miLista)     #desordenamos la lista  
          
          print("Los números de su cartilla son: ", miLista[:15])     #mostramos únicamente los 15 primeros  
        
      else:
        while cartillas > 3:
            a=int(input("Ingrese un numero menor o igual a 3: "))
            if a<=3:
              monto_persona = a * 5
              suma=suma+monto_persona 
              print("el pozo a pagar es: ",monto_persona)
              for z in range(1, a + 1): 	
                miLista=list(range(1,80))  #creamos una lista del 1 al 80  
                random.shuffle(miLista)     #desordenamos la lista           
                print("Los números de su cartilla son: ", miLista[:15])     #mostramos únicamente los 15 primeros
              break 	        
    print("el poso total es : ",suma)            


def sacar_bolillas():
  z=1
  bsjugar = []
  bjugadas = []
  for i in range(1,81):
    bsjugar.append(i)
  while z == 1:
      for n in range(1,16):
        a=int(input("Presione (9) si desea obtener bolilla"))
        #b=int(input("Si desea reiniciar su juego presione (2):"))
        #c=int(input("Si desea salir del juego presione (3):"))
        if(a == 9):
          juego = random.choice(bsjugar)
          bsjugar.remove(juego)
          bjugadas.append(juego)
          print("Bolilla:",juego)
          print("Bolillas que han salido: ",bjugadas)
          print()
      break


while True:
  print("Ingrese (1) para obtener datos de los compradores")
  print("Ingrese (2) si desea ver bolilla salida")
  print("Ingrese (0) si desea salir")
  m = int(input()) 
  if (m == 1):
    entrada()
    

  elif (m == 2):
    sacar_bolillas()
  elif(m == 0):
    print("Hasta pronto, usted se ha rendido mascota imbecil pareces Paul")
    break
