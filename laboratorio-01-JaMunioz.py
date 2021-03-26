import random

def Mostrar(matriz): #For see the matrix.
    print("")
    for i in matriz:
        for k in i:
            print("\t", k, end=" ")
        print()
    print("")

def Girar(m,i): #Choose one card with the respective coord.
    while True:
        while True:
            A = input("Choose some card using the respective coords "
                      "(If you want see the options again type i): ")
            while True:
                if A == "i":
                    Mostrar(i)
                    break
                else:
                    break
            try:
                a = int(A.split(",")[0])
                b = int(A.split(",")[1])
                if a >= len(m) or a <= -1:
                    print("The number before the ´,´ just can be "
                          "between ´0´ and ´"+str(len(m)-1)+"´")
                elif b >= len(m[0]) or b <= -1:
                    c = 0
                    for i in range(len(m[a])):
                        if m[a][i] == " ":
                            c += 1 
                    print("The number after the ´,´ just can be "
                          "between ´0´ and ´"+str(len(m[a])-1-c)+"´")
                else:
                    break
            except:
                if A != "i":
                    print("if u want continue with this game "
                          "just use numbers..")
        break
    return (a,b)
j1 = []
j2 = []
m = []

while True:
    try:
        c = int(input("How much pairs of card do you want for the game: ")) 
        if c <= 1:
            print("The numbers of cards need be beetwin 2 pairs and n pairs ")
        else:
            break
    except:
        print("Error")

for i in range(c):
    j1.append(i+1)
    j2.append(i+1)
for i in range(c): #randomizer of the Maze
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

ma = 0
index = []
for i in range(len(mc)):
    index.append([])
    for k in range(len(mc[0])):
        if mc[i][k] == " ":
            index[i].append(" ")
        else:
            index[i].append(str(i)+","+str(k))
            ma += 1 #This is for know when the game its finished.

print("\n")
print("This are the options..")
Mostrar(index)
k = 0 #Conditional for know if the player take one point,
      #for repeat his turn.
p1 = 0 #Points of player 1.
p2 = 0 #Point of platyer 2.
p = 0 #id: if this number is par its playing the player 1,
      #else, its playing the player 2.
stop = 0
while True:

    if (p%2 == 0) and (k == 0):
        print("Its turn of the player 1..")
    elif (p%2 != 0) and (k == 0):
        print("Its turn of the player 2..")
    elif (p%2 == 0) and (k == 1):
        print("Well done, play again player 1..")
    else:
        print("Well done, play again player 2..")

    Mostrar(mc)
    k = 0
    while True: 
        a,b = Girar(mc,index)
        if mc[a][b] == " ":
            print("In this coord dont have any card, "
            "give some new coord for continue..")
        else:
            break
    mc[a].pop(b)
    mc[a].insert(b,M[a][b])
    index[a].pop(b)
    index[a].insert(b," ")
    A = M[a][b]
    Mostrar(mc)

    while True: 
        c,d = Girar(mc,index)
        if mc[c][d] == " ":
            print("In this coord dont have any card, "
            "give some new coord for continue..")
        elif a == c and b == d:
            print("u was give the same coord again..")
        else:
            break
    mc[c].pop(d)
    mc[c].insert(d,M[c][d])
    index[c].pop(d)
    index[c].insert(d," ")
    B = M[c][d]
    Mostrar(mc)

    if A == B and p % 2 == 0:
        p1 += 2
        mc[a].pop(b)
        mc[a].insert(b," ")
        mc[c].pop(d)
        mc[c].insert(d," ")
        k = 1
    elif A == B and p % 2 != 0:
        p2 += 2
        mc[a].pop(b)
        mc[a].insert(b," ")
        mc[c].pop(d)
        mc[c].insert(d," ")
        k = 1
    else:
        mc[a].pop(b)
        mc[a].insert(b,"*")
        index[a].pop(b)
        index[a].insert(b,str(a)+","+str(b))
        mc[c].pop(d)
        mc[c].insert(d,"*")
        index[c].pop(d)
        index[c].insert(d,str(c)+","+str(d))
        print("No coincidences")


    if (p1+p2) == int(ma):
        if p1 == p2:
            print("Its a tie, both players have "+str(p1/2)+" points.")
            stop = 1
        elif p % 2 == 0:
            p += 2
            print("The winner is the first player. Score: "+str(p1/2))
            print("and.. the score of the second player was: "+str(p2/2))
            stop = 1
        else:
            p += 2
            print("The winner is the second player. Score: "+str(p2/2))
            print("and.. the score of the first player was: "+str(p1/2))
            stop = 1
    if k == 0:
        p += 1
    else:
        p += 2
    if stop == 1:
        break