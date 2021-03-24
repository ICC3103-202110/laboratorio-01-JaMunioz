import random

def Mostrar(matriz):
    print("")
    for i in matriz:
        for k in i:
            print("\t", k, end=" ")
        print()
    print("")

def Girar():
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
    return (a,b)
j1 = []
j2 = []
m = []

while True:
    try:
        c = int(input("How much pairs of card do you want for the game: ")) #both players have the indicated number of the cards 
        if c <= 1:
            print("The numbers of cards need be beetwin 2 pairs and n pairs ")
        else:
            break
    except:
        print("Error")

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

mm = len(m)
for i in range(mm):
    if i*i >= mm:
        v = i
        break

mc = []
M = []
r = 0
for i in range(v):
    mc.append([])
    M.append([])
    for k in range(v):
        mc[i].append("*")
        try: 
            M[i].append(m[r])
        except:
            M[i].append(" ")
        r += 1
R = []
for i in range(len(M[0])):
    R.append(" ")
print(R)
print(M)
print(mc)

while True:
    if M[-1] == R:
        M.pop(-1)
        mc.pop(-1)
    else:
        break
    
for i in range(1,len(M[0])+1):
    if M[-1][-i] == " ":
        mc[-1].remove("*")
        mc[-1].append(" ")
    else:
        break

Mostrar(M)
Mostrar(mc)

a,b = Girar()
mc[a].pop(b)
mc[a].insert(b,M[a][b])
Mostrar(mc)

a,b = Girar()
mc[a].pop(b)
mc[a].insert(b,M[a][b])
Mostrar(mc)
#points of the players
p1 = 0 
p2 = 0
