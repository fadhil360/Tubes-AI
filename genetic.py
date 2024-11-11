from Creating import initial, objectivefunction
from typing import List
import random
import datetime
import matplotlib.pyplot as plt
import numpy as np


def population(jumlahPopulasi):
    populationList = [initial() for _ in range(jumlahPopulasi)]
    fitnessFunction = np.array([objectivefunction(individu) + 1 for individu in populationList])
    total_fitness = fitnessFunction.sum()
    probability = fitnessFunction / total_fitness
    return populationList, probability

def nextPopulation(populationarray):
    fitnessFunction = np.array([objectivefunction(individu) + 1 for individu in populationarray])
    total_fitness = fitnessFunction.sum()
    probability = fitnessFunction / total_fitness
    return populationarray, probability

def selection(jumlahParent, populationList, probability):
    cumulative_probabilities = np.cumsum(probability) * 100
    parents = []

    for _ in range(jumlahParent):
        selectionRandom = random.uniform(0, 100)
        idx = np.searchsorted(cumulative_probabilities, selectionRandom)
        parents.append(populationList[idx])

    return parents

def crossover(parent1, parent2):
    crossoverPoint = random.randint(1, 125)
    offspring1 = parent1[:crossoverPoint] + parent2[crossoverPoint:]
    offspring2 = parent2[:crossoverPoint] + parent1[crossoverPoint:]
    return offspring1, offspring2

def mutation(offspring):
    missing_elements = list(set(range(1, 126)) - set(offspring))
    duplicated_elements = [i for i in range(1, 126) if offspring.count(i) > 1]

    for dup in duplicated_elements:
        replaceIndex = offspring.index(dup, offspring.index(dup) + 1)
        offspring[replaceIndex] = missing_elements.pop()
    
    return offspring

def display_3d_cube(data, end):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = np.meshgrid(range(5), range(5), range(5))
    values = np.array(data).flatten()
    max_val = max(values)
    idx = 0

    for xi, yi, zi in zip(x.flatten(), y.flatten(), z.flatten()):
        color = plt.cm.viridis(values[idx] / max_val)
        ax.text(xi, yi, zi, str(values[idx]), color=color, ha='center', va='center', fontsize=10)
        idx += 1

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    ax.set_zlim(0, 4)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.title("Final 3D Cube" if end == 1 else "Initial 3D Cube")
    plt.show()

def geneticAlgorithm():
    jumlahPopulasi = int(input("jumlahPopulasi = ")) * 2
    jumlahIterasi = int(input("jumlahIterasi = "))
    start = datetime.datetime.now()
    
    highest_offspring = -1
    plotarray = []
    highest_offspring_array = []

    populationList, probability = population(jumlahPopulasi)
    initialList = max(populationList, key=objectivefunction)

    for _ in range(jumlahIterasi):
        parents = selection(jumlahPopulasi, populationList, probability)
        offspringarray = []

        for x in range(0, len(parents) // 2):
            offspring1, offspring2 = crossover(parents[x], parents[x + len(parents) // 2])
            offspringarray.extend([offspring1, offspring2])

        nextoffspring = [mutation(off) for off in offspringarray]
        populationList, probability = nextPopulation(nextoffspring)

        highest_offspring_in_iteration = max(nextoffspring, key=objectivefunction)
        highest_fitness = objectivefunction(highest_offspring_in_iteration)

        if highest_fitness > highest_offspring:
            highest_offspring = highest_fitness
            highest_offspring_array = highest_offspring_in_iteration

        plotarray.append(highest_fitness)

    print("Nilai Objective function =", highest_offspring)
    print("Jumlah populasi =", jumlahPopulasi)
    print("Banyak iterasi =", jumlahIterasi)
    print("Durasi proses pencarian =", (datetime.datetime.now() - start))

    print(initialList)
    display_3d_cube(np.array(initialList).reshape((5, 5, 5)), end=2)
    print(highest_offspring_array)
    display_3d_cube(np.array(highest_offspring_array).reshape((5, 5, 5)), end=1)

    plt.plot(plotarray)
    plt.title("Objective Function vs. Iterations")
    plt.show()
geneticAlgorithm()
