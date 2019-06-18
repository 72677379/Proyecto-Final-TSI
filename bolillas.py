import random
import sys
import os
import sys
import time

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
    print("el pozo total es : ",suma)            


def sacar_bolillas():
  z=1
  bsjugar = []
  bjugadas = []
  for i in range(1,81):
    bsjugar.append(i)
  while z == 1:
      for n in range(1,16):
        print("/*Presione (9) si desea obtener bolilla*/")
        print("/*Presione (0) si desea ver las bolillas salidas*/")
        print("/*Presione (2) para regresar al menu de inicio*/")
        a = int(input())
        if(a == 9):
          juego = random.choice(bsjugar)  #Elección de un número de forma aleatoria
          bsjugar.remove(juego)
          bjugadas.append(juego)
          print("\n Bolilla: ",juego,"\n")
          print("Las bolillas que han salido son:",bjugadas, "\n")
            
        elif(a== 0):
          print("Las bolillas que han salido son:",bjugadas, "\n")
          
        elif(a == 2): 
          return menu()
      break
  print("Procesando...")    
  time.sleep(6) 
  print("Lamentablemente no hubo un ganador.", "\n")
  
def menu():
  m = 1
  while (m != 0):
  
    print("1. Iniciar juego")
    #print("2. Reiniciar juego")
    print("0. Salir")
    m = int(input()) 
    if (m == 1):
      entrada()
      sacar_bolillas()
    #elif(m == 2):
      #return entrada()
    elif(m == 0):
      break
menu()
 