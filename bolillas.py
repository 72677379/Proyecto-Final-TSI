import random
def ball_aleat(n):
    bolilla = []
    b = 80
    for i in range(n):
        bolilla.insert(i,random.randrange(0,b-1))
    return bolilla

alea = ball_aleat(15)
print(alea)

