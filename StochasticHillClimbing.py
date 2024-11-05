from Creating import *
import random
import datetime
import cProfile
import re
max_iteration = int(input("banyak iterasi = "))
max_duration = int(input("duration = "))


def stochastic_hill_climbing(list):
    current_list = list[:]
    current_value = objectivefunction(current_list)
    i = 0
    start = datetime.datetime.now()
    end = 0
    while i < max_iteration:
        print(i, " : ", current_value)
        neighbor_list = neighbor(current_list)
        neighbor_value = objectivefunction(neighbor_list)
        while current_value >= neighbor_value:
            neighbor_list = neighbor(current_list)
            neighbor_value = objectivefunction(neighbor_list)
            end = (datetime.datetime.now() - start).seconds
            if end >= max_duration:
                break
        
        if neighbor_value>current_value :
            current_list = neighbor_list
            neighbor_list = neighbor(current_list)
            current_value = objectivefunction(current_list)
            neighbor_value = objectivefunction(neighbor_list)
        
        if end >= max_duration:
            break
        i += 1
    return current_list


def main():
    start = datetime.datetime.now()
    initialList = initial()
    a = objectivefunction(initialList)
    print("CURRENT SCORE " + str(a))
    print(initialList)
    finalList = stochastic_hill_climbing(initialList)
    b = objectivefunction(finalList)
    print("FINAL SCORE " + str(b))
    print(finalList)
    end = (datetime.datetime.now() - start)
    print("Total waktu : ", end)

cProfile.run("main()")