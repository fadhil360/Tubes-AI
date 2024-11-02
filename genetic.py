# from Creating import *;
from typing import List;
import random;

parent1=[86, 122, 70, 93, 102, 125, 110, 120, 73, 76, 21, 106, 1, 117, 40, 25, 52, 61, 19, 11, 45, 57, 51, 109, 6, 4, 100, 3, 69, 33, 16, 65, 108, 12, 15, 99, 84, 60, 104, 53, 74, 24, 103, 75, 18, 118, 123, 98, 64, 91, 107, 17, 26, 113, 36, 2, 63, 5, 116, 27, 85, 67, 78, 112, 82, 31, 83, 95, 97, 50, 115, 39, 35, 41, 9, 77, 20, 105, 72, 42, 14, 13, 49, 56, 92, 79, 7, 34, 71, 68, 43, 80, 81, 46, 66, 62, 87, 54, 59, 29, 111, 22, 44, 48, 90, 94, 38, 119, 114, 10, 121, 28, 58, 32, 89, 101, 37, 23, 88, 30, 124, 96, 47, 8, 55]
parent2=[5, 72, 124, 60, 48, 12, 31, 52, 21, 71, 51, 44, 16, 22, 26, 106, 33, 42, 110, 81, 103, 37, 23, 34, 120, 9, 45, 119, 86, 14, 61, 56, 53, 43, 32, 85, 1, 104, 66, 19, 20, 73, 41, 79, 87, 90, 105, 46, 47, 24, 38, 6, 63, 114, 118, 69, 11, 94, 102, 68, 112, 57, 7, 76, 49, 80, 116, 92, 18, 59, 109, 77, 25, 113, 29, 2, 100, 122, 78, 40, 89, 13, 83, 84, 39, 74, 82, 125, 97, 123, 96, 108, 55, 70, 10, 27, 28, 50, 115, 75, 5, 3, 35, 65, 91, 107, 101, 111, 30, 15, 64, 117, 36, 88, 99, 98, 58, 54, 121, 17, 4, 67, 8, 62, 93]

offspring= [50, 19, 19, 108, 108, 113, 101, 80, 7, 106, 51, 41, 96, 107, 125, 78, 10, 29, 11, 89, 45, 124, 5, 79, 37, 48, 115, 6, 33, 65, 2, 53, 105, 87, 61, 23, 102, 39, 93, 38, 70, 109, 77, 95, 75, 35, 76, 84, 4, 25, 15, 66, 31, 46, 1, 30, 52, 104, 12, 64, 73, 71, 63, 47, 43, 20, 83, 116, 22, 92, 8, 91, 40, 54, 62, 34, 42, 3, 18, 123, 100, 81, 86, 88, 97, 24, 122, 36, 55, 85, 60, 67, 90, 49, 117, 121, 13, 27, 68, 94, 98, 16, 26, 119, 58, 44, 72, 112, 99, 57, 118, 82, 21, 114, 69, 103, 74, 9, 59, 120, 32, 28, 17, 14, 110]

print(offspring.count(19))
print(offspring.index(19))
print(offspring.count(56))

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
            replace = temp.pop(0)
            offspring[offspring.index(i)] = replace

    return offspring

offspring1, offspring2 = crossover(parent1, parent2)
print(offspring1)
print()
print(offspring2)
print()
offspring1 = mutation(offspring1)
offspring2 = mutation(offspring2)
print(offspring1)
print()
print(offspring2)
