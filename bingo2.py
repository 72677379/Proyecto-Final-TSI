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
          miLista=list(range(1,80))  #creamos una lista del 1 al 80  
          random.shuffle(miLista)     #desordenamos la lista  
          
          print("Los números de su cartilla son: ", miLista[:15])     #mostramos únicamente los 15 primeros  
      else:
        while cartillas > 3:
            a=int(input("Ingrese un numero menor o igual a 3: "))
            if a<=3:
              monto_persona = a * 5 
              print("el pozo a pagar es: ",monto_persona)
              for z in range(1, a + 1): 	
                miLista=list(range(1,80))  #creamos una lista del 1 al 80  
                random.shuffle(miLista)     #desordenamos la lista           
                print("Los números de su cartilla son: ", miLista[:15])     #mostramos únicamente los 15 primeros
              break 	        
                
entrada()