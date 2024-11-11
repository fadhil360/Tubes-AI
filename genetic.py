from Creating import initial, objectivefunction;
from typing import List;
import random;
import datetime
import matplotlib.pyplot as plt
import numpy as np
# parent1=[86, 122, 70, 93, 102, 125, 110, 120, 73, 76, 21, 106, 1, 117, 40, 25, 52, 61, 19, 11, 45, 57, 51, 109, 6, 4, 100, 3, 69, 33, 16, 65, 108, 12, 15, 99, 84, 60, 104, 53, 74, 24, 103, 75, 18, 118, 123, 98, 64, 91, 107, 17, 26, 113, 36, 2, 63, 5, 116, 27, 85, 67, 78, 112, 82, 31, 83, 95, 97, 50, 115, 39, 35, 41, 9, 77, 20, 105, 72, 42, 14, 13, 49, 56, 92, 79, 7, 34, 71, 68, 43, 80, 81, 46, 66, 62, 87, 54, 59, 29, 111, 22, 44, 48, 90, 94, 38, 119, 114, 10, 121, 28, 58, 32, 89, 101, 37, 23, 88, 30, 124, 96, 47, 8, 55]
# parent2=[5, 72, 124, 60, 48, 12, 31, 52, 21, 71, 51, 44, 16, 22, 26, 106, 33, 42, 110, 81, 103, 37, 23, 34, 120, 9, 45, 119, 86, 14, 61, 56, 53, 43, 32, 85, 1, 104, 66, 19, 20, 73, 41, 79, 87, 90, 105, 46, 47, 24, 38, 6, 63, 114, 118, 69, 11, 94, 102, 68, 112, 57, 7, 76, 49, 80, 116, 92, 18, 59, 109, 77, 25, 113, 29, 2, 100, 122, 78, 40, 89, 13, 83, 84, 39, 74, 82, 125, 97, 123, 96, 108, 55, 70, 10, 27, 28, 50, 115, 75, 5, 3, 35, 65, 91, 107, 101, 111, 30, 15, 64, 117, 36, 88, 99, 98, 58, 54, 121, 17, 4, 67, 8, 62, 93]

# offspring= [50, 19, 19, 108, 108, 113, 101, 80, 7, 106, 51, 41, 96, 107, 125, 78, 10, 29, 11, 89, 45, 124, 5, 79, 37, 48, 115, 6, 33, 65, 2, 53, 105, 87, 61, 23, 102, 39, 93, 38, 70, 109, 77, 95, 75, 35, 76, 84, 4, 25, 15, 66, 31, 46, 1, 30, 52, 104, 12, 64, 73, 71, 63, 47, 43, 20, 83, 116, 22, 92, 8, 91, 40, 54, 62, 34, 42, 3, 18, 123, 100, 81, 86, 88, 97, 24, 122, 36, 55, 85, 60, 67, 90, 49, 117, 121, 13, 27, 68, 94, 98, 16, 26, 119, 58, 44, 72, 112, 99, 57, 118, 82, 21, 114, 69, 103, 74, 9, 59, 120, 32, 28, 17, 14, 110]

# print(offspring.count(19))
# print(offspring.index(19))
# print(offspring.count(56))

# listTest = [[1,2,3], [1,5,4], [3,2,1]]

def population(jumlahPopulasi):
    populationList = []
    fitnessFunction = []
    probability = []
    for i in range(0,jumlahPopulasi):
        individu = initial()
        populationList.append(individu)
        fitnessFunction.append(objectivefunction(populationList[i])+1)
    total_fitness = sum(fitnessFunction)
    probability = [fitness / total_fitness for fitness in fitnessFunction]
    
    return populationList , probability

def nextPopulation(populationarray):
    fitnessFunction = []
    probability = []
    populationList=populationarray
    for popu in populationarray:
        fitnessFunction.append(objectivefunction(popu)+1)
    total_fitness = sum(fitnessFunction)
    probability = [fitness / total_fitness for fitness in fitnessFunction]
    return populationList , probability
        
# def selection(jumlahParent, populationList, probability):
#     parents = []
#     scalePemilihan = []
#     scaleSum = 0
#     for i in range(0, len(probability)):
#         scaleSum = probability[i] * 100
#         scalePemilihan.append(scaleSum)

#     for i in range(0,jumlahParent):
#         selectionRandom = random.uniform(0, 100)
#         if selectionRandom <= scalePemilihan[i]:
#             parents.append(populationList[i])

#     return parents 

def selection(jumlahParent, populationList, probability):
    parents = []
    cumulative_probabilities = []
    cumulative_sum = 0
    
    # Create cumulative probabilities
    for p in probability:
        cumulative_sum += p * 100  # Scale to 0-100 range
        cumulative_probabilities.append(cumulative_sum)
    
    # Select parents based on roulette wheel
    for _ in range(jumlahParent):
        selectionRandom = random.uniform(0, 100)
        
        # Find the selected individual based on the random spin
        for i, cum_prob in enumerate(cumulative_probabilities):
            if selectionRandom <= cum_prob:
                parents.append(populationList[i])
                break

    # Ensure we have the correct number of parents
    if len(parents) < jumlahParent:
        raise ValueError("Selection did not yield the required number of parents.")
    
    return parents


def crossover(parent1, parent2):
    crossoverPoint = random.randint(1, 125)

    offspring1 = parent1[:crossoverPoint] + parent2[crossoverPoint:]
    offspring2 = parent2[:crossoverPoint] + parent1[crossoverPoint:]

    return offspring1, offspring2

def mutation(offspring):
    temp = []

    for i in range(1,126):
        if(offspring.count(i)==0):
            temp.append(i)

    for i in range(1, 126):
        if(offspring.count(i)==2):
            replaceIndex = offspring.index(i, offspring.index(i)+1)
            offspring[replaceIndex] = temp.pop(0)

    return offspring
def display_3d_cube(data,end):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Create a 5x5x5 grid
    x, y, z = np.meshgrid(range(5), range(5), range(5))

    # Flatten data for easier iteration
    values = np.array(data).flatten()
    idx = 0

    for xi, yi, zi in zip(x.flatten(), y.flatten(), z.flatten()):
        # Set a unique color based on the value
        color = plt.cm.viridis(values[idx] / max(values))
        ax.text(xi, yi, zi, str(values[idx]), color=color,
                ha='center', va='center', fontsize=10)
        idx += 1

    # Set plot limits and labels
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    ax.set_zlim(0, 4)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])
    if end==1:
        plt.title("Final 3D Cube Visualization with Genetic")
    else:
        plt.title("Initial 3D Cube Visualization with Genetic")

    plt.show()

def geneticAlgorithm(): # sementara
    jumlahPopulasi=int(input("jumlahPopulasi = "))
    jumlahIterasi=int(input("jumlahIterasi = "))
    jumlahPopulasi*=2 #agar semua ada pasangan
    start = datetime.datetime.now()
    offspringarray=[]
    nextoffspring=[]
    highestoffspring=0
    highestoffspringarray=[]
    populationList, probability = population(jumlahPopulasi)
    for off in populationList:
        if highestoffspring<objectivefunction(off):
            highestoffspring=objectivefunction(off)
            initialList=off
    for i in range(jumlahIterasi):
        if len(nextoffspring)!=0:
            populationList, probability =nextPopulation(nextoffspring)
        parents = selection(jumlahPopulasi, populationList, probability)
        for x in range(0,int(len(parents)/2)):
            offspring1, offspring2 = crossover(parents[x], parents[x+int(len(parents)/2)])
            offspringarray.append(offspring1)
            offspringarray.append(offspring2)
            nextoffspring=[]
            for off in offspringarray:
                off = mutation(off)
                nextoffspring.append(off)
    for off in nextoffspring:
        if highestoffspring<objectivefunction(off):
            highestoffspring=objectivefunction(off)
            highestoffspringarray=off
    print("Nilai Objective function= ",highestoffspring)
    print("Jumlah populasi= ",jumlahPopulasi)
    print("Banyak iterasi= ",jumlahIterasi)
    print("Durasi proses pencarian= ",(datetime.datetime.now() - start))
    initial_array = np.array(initialList).reshape((5, 5, 5))
    display_3d_cube(initial_array,2)
    final_array = np.array(highestoffspringarray).reshape((5, 5, 5))
    display_3d_cube(final_array,1)
    # print(objectivefunction(offspring1))
    # print(objectivefunction(offspring2))
    # print(objectivefunction(offspring3))
    # print(objectivefunction(offspring4))


geneticAlgorithm()
# offspring1, offspring2 = crossover(parent1, parent2)
# offspring1 = mutation(offspring1)
# offspring2 = mutation(offspring2)
# print(offspring1)
# print(offspring2)
