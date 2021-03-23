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

print(M[0])
print(M[1])

while True:
    while True:
        A = input("Choose some card using the respective coords (ex: ´0,i´ or ´1,i´ | i length of the row): ")
        try:  
            a = int(A.split(",")[0])
            b = int(A.split(",")[1])
            if a >= 2 or a <= -1:
                print("The first number just could be: ´0´ or ´1´")
            elif b >= c or b <= -1:
                print("The second number after the ´,´ just can be between ´0´ and "+str(c-1))
            else:
                break
        except :
            print("if u want continue with this game just use numbers..")
    break

print(mc)
print(a)
print(b)
mc[a].pop(b)
mc[a].insert(b,M[a][b])
print(mc)

#points of the players
p1 = 0 
p2 = 0


