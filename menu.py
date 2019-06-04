# Menu del juego
import random
def ball_aleat(n):
    cartilla = []
    for i in range(n):
        cartilla.insert(i,random.randrange(0,80))
    return cartilla
alea = ball_aleat(15)
def imprimir():
    print(alea)

while True:
    print("Bienvenido que desea hacer: ")
    print("Presione 1 si desea obtener un cartilla")
    print("Presione 2 si quiere que se muestre la cartilla")
    print("Presione 0 para salir")
    entrada = int(input())

    if entrada == 1 :
        print("Cartilla obtenida")

        print("¡Que desea hacer ahora?")
    
    if entrada == 2 :
        imprimir()

    if entrada == 0:
        break
    

    
    

