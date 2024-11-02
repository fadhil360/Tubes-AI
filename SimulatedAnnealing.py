from Creating import *
import random
import datetime
import math

max_iteration = int(input("banyak iterasi = "))
max_duration = int(input("duration = "))
max_temperature = int(input("temperature = "))
stuck = 0


def Simulated_Annealing(list):
    global stuck
    current_list = list[:]
    current_value = objectivefunction(current_list)
    i = 0
    start = datetime.datetime.now()
    end = 0
    while i < max_iteration:
        print(i, " : ", current_value)
        neighbor_list = neighbor(current_list)
        neighbor_value = objectivefunction(neighbor_list)
        temperature = max_temperature

        while current_value >= neighbor_value:
            neighbor_list = neighbor(current_list)
            neighbor_value = objectivefunction(neighbor_list)

            if neighbor_value < current_value:
                if temperature != 0:
                    annealing = math.exp(
                        (current_value - neighbor_value) / temperature)
                chance = random.randint(0, 1000)
                if chance != 0:
                    chance = chance/1000
                if chance >= annealing:
                    stuck += 1
                    break
                temperature -= 1

            end = (datetime.datetime.now() - start).seconds
            if end >= max_duration:
                break

        current_list = neighbor_list
        neighbor_list = neighbor(current_list)
        current_value = objectivefunction(current_list)
        neighbor_value = objectivefunction(neighbor_list)
        if end >= max_duration:
            break
        i += 1
    print(i, " : ", current_value)
    return current_list


start = datetime.datetime.now()
initialList = initial()
a = objectivefunction(initialList)
print("CURRENT SCORE " + str(a))
print(initialList)
finalList = Simulated_Annealing(initialList)
b = objectivefunction(finalList)
print("FINAL SCORE " + str(b))
print(finalList)
end = (datetime.datetime.now() - start)
print("Total waktu : ", end)
print("Total stuck : ", stuck)
