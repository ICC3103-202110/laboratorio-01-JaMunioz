import random
j1 = []
j2 = []
m1 = []
m2 = []
c = int(input("How much card do u want for the players: ")) #both players have the indicated number of the cards 
for i in range(c):
    #j1.append(random.randint(1,i)) En caso de generar i cartas al azar, pueden repetirse
    #j2.append(random.randint(1,i))
    j1.append(i+1)
    j2.append(i+1)
for i in range(c): #randomizer of the presents cards
    r = (random.randint(0,c-1-i))
    m1.append(j1[r])
    j1.pop(r)
    r = (random.randint(0,c-1-i))
    m2.append(j2[r])
    j2.pop(r)

p1 = 0
p2 = 0