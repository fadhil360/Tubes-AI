import random
MAGICNUMBER=315
def initial():
    initialList=[]
    for x in range(1,126):
        initialList.append(x)
    random.shuffle(initialList)
    return initialList

def listtomatrix(List):
    matrixlist=[[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] ,[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] ,[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]]
    i=0
    j=0
    k=0
    for a in List:
        matrixlist[i][j][k]=a   
        if j<4 or k<4:
            if k<4 :
                k+=1
            else :
                j+=1
                k=0
        else :
            i+=1
            j=0
            k=0
    return matrixlist

def matrixtolist(matrix):
    initiallist=[]
    for i in matrix:
        for j in i:
            for k in j:
                initialList.append(k)
    return initialList

def objectivefunction(list):
    score=0
    # kiri kanan
    index=0
    for i in range(1,6):
        for j in range(1,6):
            sumlist=0
            for k in range(1,6):
                sumlist+=list[index]
                index+=1
            if(sumlist==MAGICNUMBER):
                score+=1 
    # depan belakang
    index=0
    x=0
    for i in range(1,6):
        for j in range(1,6):
            sumlist=0
            for k in range(1,6):
                sumlist+=list[index]
                index=index+25
            x+=1
            index=x
            if(sumlist==MAGICNUMBER):
                score+=1 
    # atas bawah
    index=0
    x=0
    z=0
    for i in range(1,6):
        for j in range(1,6):
            sumlist=0
            for k in range(1,6):
                sumlist+=list[index]
                index=index+5
            x+=1
            index=x+z
            if(sumlist==MAGICNUMBER):
                score+=1 
        z+=25
        x=0
        index=z
    #diagonal ruang 1
    sumlist=0
    sumlist=sumlist+list[0]+list[31]+list[62]+list[93]+list[124]
    if(sumlist==MAGICNUMBER):
        score+=1 
    #diagonal ruang 2
    sumlist=0
    sumlist=sumlist+list[4]+list[33]+list[62]+list[91]+list[120]
    if(sumlist==MAGICNUMBER):
        score+=1
    #diagonal ruang 3
    sumlist=0
    sumlist=sumlist+list[20]+list[41]+list[62]+list[83]+list[104]
    if(sumlist==MAGICNUMBER):
        score+=1
    #diagonal ruang 4
    sumlist=0
    sumlist=sumlist+list[24]+list[43]+list[62]+list[81]+list[100]
    if(sumlist==MAGICNUMBER):
        score+=1
    #diagonal depan belakang 1
    index=0
    z=0
    for j in range(1,6):
        sumlist=0
        for k in range(1,6):
            sumlist+=list[index]
            index+=6
        z+=25
        index=z
        if(sumlist==MAGICNUMBER):
            score+=1 
    #diagonal depan belakang 2
    index=4
    z=0
    for j in range(1,6):
        sumlist=0
        for k in range(1,6):
            sumlist+=list[index]
            index+=4
        z+=25
        index=z+4
        if(sumlist==MAGICNUMBER):
            score+=1 
    #diagonal kiri kanan 1
    index=0
    z=0
    for j in range(1,6):
        sumlist=0
        for k in range(1,6):
            sumlist+=list[index]
            index+=30
        z+=1
        index=z
        if(sumlist==MAGICNUMBER):
            score+=1 
    #diagonal kiri kanan 2
    index=20
    z=0
    for j in range(1,6):
        sumlist=0
        for k in range(1,6):
            sumlist+=list[index]
            index+=20
        z+=1
        index=z+20
        if(sumlist==MAGICNUMBER):
            score+=1 
    #diagonal atas bawah 1
    index=0
    z=0
    for j in range(1,6):
        sumlist=0
        for k in range(1,6):
            sumlist+=list[index]
            index+=26
        z+=5
        index=z
        if(sumlist==MAGICNUMBER):
            score+=1 
    #diagonal atas bawah 2
    index=4
    z=0
    for j in range(1,6):
        sumlist=0
        for k in range(1,6):
            sumlist+=list[index]
            index+=24
        z+=5
        index=z
        if(sumlist==MAGICNUMBER):
            score+=1 
    return score
def neighbor(list):
    neighbor = list[:]
    x = random.randint(0, 124)
    y = random.randint(0, 124)
    while x == y:
        y = random.randint(0, 124)
    # if x != y:
    #     a = neighbor[x]
    #     b = neighbor[y]
    #     neighbor[x] = b
    #     neighbor[y] = a
    neighbor[x], neighbor[y] = neighbor[y], neighbor[x]
    return neighbor
    
initialList=initial()
matrixlist =listtomatrix(initialList)
a=objectivefunction(initialList)
print("SCORE "+ str(a))
print(initialList)
for i in range(0,5):
    print(matrixlist[i][0])
    print(matrixlist[i][1])
    print(matrixlist[i][2])
    print(matrixlist[i][3])
    print(matrixlist[i][4])
    print("===============")
    
    
