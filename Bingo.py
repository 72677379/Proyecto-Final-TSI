import random 
def entrada():
    jugadores = int(input("¿Cuantos jugadores son?"))
    
    str(input("Ingrese su nombre: "))
    

cartilla = []
def ball_aleat(n):
    for i in range(n):
        cartilla.insert(i,random.randrange(0,80))
    return cartilla

entrada()
aleatorios = ball_aleat(15)
print(aleatorios)
