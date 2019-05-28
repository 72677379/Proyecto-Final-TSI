from  random import*
def listaAleatorios(n):
      lista = []
      for i in range(n):
          lista[i] = randint(1,80)
      return lista

print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())

aleatorios=listaAleatorios(n)
print(aleatorios)