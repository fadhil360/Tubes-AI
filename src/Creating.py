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
    listm=[]
    for i in matrix:
        for j in i:
            for k in j:
                listm.append(k)
    return listm


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

def highestneighbor(list):
    neighbor = list[:]
    highestpoint = -1
    topneighbor = []
    
    for i in range(0, 125):
        for j in range(i + 1, 125):
            neighbortemp = neighbor[:]
            
            # Swap elements
            neighbortemp[i], neighbortemp[j] = neighbortemp[j], neighbortemp[i]
            
            # Check if this new neighbor is better
            current_value = objectivefunction(neighbortemp)
            if current_value >= highestpoint:
                topneighbor = neighbortemp[:]
                highestpoint = current_value
    return topneighbor

    
    
