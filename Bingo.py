import random 
def entrada():
    str(input("Ingrese su nombre: "))
    int(input("Ingrese su número de cartilla: "))

cartilla = []
def ball_aleat(n):
    for i in range(n):
        cartilla.insert(i,random.randrange(0,80))
    return cartilla

entrada()
aleatorios = ball_aleat(15)
print("Su cartilla es: ",aleatorios)
