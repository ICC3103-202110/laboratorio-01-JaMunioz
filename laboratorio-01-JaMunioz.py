import random
j1 = []
j2 = []
m = []
M = [[],[]]
mc = [[],[]]

c = int(input("How much card do u want for the game: ")) #both players have the indicated number of the cards 
for i in range(c):
    j1.append(i+1)
    j2.append(i+1)
for i in range(c): #randomizer of the presents cards
    r = (random.randint(0,c-1-i))
    m.append(j1[r])
    j1.pop(r)
    r = (random.randint(0,c-1-i))
    m.append(j2[r])
    j2.pop(r)
    mc[0].append("*")
    mc[1].append("*")

for i in range(c*2):
        if i >= c:
            M[1].append(m[i])
        else:
            M[0].append(m[i])

print(m)
print(M)
print(mc)
A = input("Choose some card using the respective coords (ex: 0,i or 0,i | i length of the row): ")
a = A.split(",")[0]
b = A.split(",")[1]
print(a)
print(b)
mc[a].pop(b)
mc[a].insert(b,M[a][b])
print(mc)
#points of the players
p1 = 0 
p2 = 0


