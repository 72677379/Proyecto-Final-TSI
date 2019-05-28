cartillas = int(input("¿Cúantos cartillas desea comprar?"))

#for i in range(cartillas):
if cartillas <= 3:
        pozo_total = cartillas * 5 
        print(pozo_total)
else:
    while cartillas > 3:
        if cartillas <= 3:
            pozo_total = cartillas * 5 
            print(pozo_total)
        else:
            preguntador = int(input("Deme un número menor o igual a 3:"))
            print(preguntador)