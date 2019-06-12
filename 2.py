import random
import sys
import os
import sys
z=1
bsjugar = []
bjugadas = []
for i in range(1,81):
    bsjugar.append(i)
while z == 1:
    for n in range(1,16):
        a=int(input("Si desea otra bolilla presione (1):"))
        #b=int(input("Si desea reiniciar su juego presion (2):"))
        #c=int(input("Si desea salir del juego presion (3):"))
        juego = random.choice(bsjugar)
        bsjugar.remove(juego)
        bjugadas.append(juego)
        print("Bolilla:",juego)
        print("Bolillas que han salido: ",bjugadas)
        print()
    break
    