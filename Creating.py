import numpy as np
import random
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


def objectivefunction(arr):
    MAGICNUMBER = 315 # Define your MAGICNUMBER here
    score = 0

    # Reshape the input list into a 5x5x5 3D numpy array
    cube = np.array(arr).reshape(5, 5, 5)

    # Check left-right slices
    for i in range(5):
        for j in range(5):
            if cube[i, j, :].sum() == MAGICNUMBER:
                score += 1

    # Check front-back slices
    for i in range(5):
        for j in range(5):
            if cube[i, :, j].sum() == MAGICNUMBER:
                score += 1

    # Check top-bottom slices
    for i in range(5):
        for j in range(5):
            if cube[:, i, j].sum() == MAGICNUMBER:
                score += 1

    # Check space diagonals
    if np.sum([cube[i, i, i] for i in range(5)]) == MAGICNUMBER:
        score += 1
    if np.sum([cube[i, 4 - i, i] for i in range(5)]) == MAGICNUMBER:
        score += 1
    if np.sum([cube[4 - i, i, i] for i in range(5)]) == MAGICNUMBER:
        score += 1
    if np.sum([cube[4 - i, 4 - i, i] for i in range(5)]) == MAGICNUMBER:
        score += 1

    # Check front-back diagonals
    for j in range(5):
        if np.sum([cube[i, i, j] for i in range(5)]) == MAGICNUMBER:
            score += 1
        if np.sum([cube[i, 4 - i, j] for i in range(5)]) == MAGICNUMBER:
            score += 1

    # Check left-right diagonals
    for j in range(5):
        if np.sum([cube[i, j, i] for i in range(5)]) == MAGICNUMBER:
            score += 1
        if np.sum([cube[4 - i, j, i] for i in range(5)]) == MAGICNUMBER:
            score += 1

    # Check top-bottom diagonals
    for j in range(5):
        if np.sum([cube[j, i, i] for i in range(5)]) == MAGICNUMBER:
            score += 1
        if np.sum([cube[j, 4 - i, i] for i in range(5)]) == MAGICNUMBER:
            score += 1

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
a=objectivefunction([1, 42, 22, 53, 100, 81, 10, 68, 117, 44, 33, 46, 45, 98, 93, 28, 6, 48, 7, 18, 95, 120, 9, 97, 60, 38, 54, 125, 94, 70, 116, 83, 73, 39, 4, 40, 
121, 84, 59, 11, 103, 66, 16, 43, 87, 56, 27, 85, 80, 67, 82, 118, 30, 110, 2, 113, 119, 105, 102, 72, 104, 13, 76, 55, 79, 29, 108, 78, 24, 58, 
112, 115, 19, 122, 14, 25, 50, 37, 107, 96, 111, 99, 51, 31, 23, 88, 12, 65, 35, 41, 86, 21, 124, 92, 75, 5, 57, 64, 52, 34, 61, 17, 101, 89, 47, 71, 62, 36, 26, 15, 106, 32, 109, 74, 91, 69, 114, 49, 3, 77, 8, 90, 20, 123, 63])
print("SCORE "+ str(a))
print(initialList)
for i in range(0,5):
    print(matrixlist[i][0])
    print(matrixlist[i][1])
    print(matrixlist[i][2])
    print(matrixlist[i][3])
    print(matrixlist[i][4])
    print("===============")
    
    
