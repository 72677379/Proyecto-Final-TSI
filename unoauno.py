import random
L=[random.randint(0, 15)]
i=1
while i<15:
  x=random.randint(0,15)
  for j in range(0, len(L)):
    if L[j]==x:
      break
  else:
    L.append(x)
    i+=1
print(L)
m=1
acumulador=[]

for i in range(1,16):
    print(f"la {m}era bolilla es : ")
    x=random.randint(1,16)
    
    print([x])
    m=m+1
    acumulador=acumulador + [x]

print("el codigo ganador es ",acumulador)