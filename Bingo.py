import random
def entrada():
    n = int(input("¿Cuantos jugadores son? "))
    for x in range (1,n+1):
        x = str(input("Ingrese su nombre: "))
        x = str(input("Ingre su numero de cartilla: "))

cartilla = []
def ball_aleat(n):
    for i in range(n):
        cartilla.insert(i,random.randrange(0,80))
    return cartilla

entrada()
aleatorios = ball_aleat(24)
print(aleatorios)
