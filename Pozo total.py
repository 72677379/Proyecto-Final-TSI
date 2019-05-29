cartillas = int(input("¿Cúantos cartillas desea comprar?"))

if cartillas <= 3:
        pozo_total = cartillas * 5 
        print("el pozo a pagar es  : ",pozo_total)
else:
    while cartillas > 3:
        a=int(input("Ingrese un numero menor o igual a 3 : "))
        if a<=3:
            pozo_total = a * 5 
            print("el pozo a pagar es  : ",pozo_total)
            break 