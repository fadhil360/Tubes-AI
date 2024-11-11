from Creating import *
import datetime
import matplotlib.pyplot as plt

plotarray=[]
max_iteration = int(input("banyak iterasi (default = 1000) = "))
if max_iteration > 0:
    truth = 1
else:
    max_iteration = 1000
max_duration = int(input("duration (default = 120) = "))
if max_duration > 0:
    truth = 1
else:
    max_duration = 120
max_sidewaymove = int(input("sidewaymove (default = 5) = "))
if max_sidewaymove >= 0:
    truth = 1
else:
    max_sidewaymove = 5

def SidewayMove_hill_climbing(list):
    current_list = list[:]
    current_value = objectivefunction(current_list)
    i = 0
    sidewaymove = 0
    start = datetime.datetime.now()
    end = 0
    print(i, " : ", current_value)
    while i < max_iteration:
        plotarray.append(current_value)
        neighbor_list = highestneighbor(current_list)
        if current_value < objectivefunction(neighbor_list):
            current_value=objectivefunction(neighbor_list)
            current_list=neighbor_list
            i += 1
            print(i, " : ", current_value)
        elif (current_value == objectivefunction(neighbor_list)) and (sidewaymove<max_sidewaymove) :
            sidewaymove += 1
            current_value=objectivefunction(neighbor_list)
            current_list=neighbor_list
            i += 1
            print(i, " : ", current_value)
        else :
            break
        end = (datetime.datetime.now() - start).seconds
        if end >= max_duration:
            break
    return current_list


def main():
    start = datetime.datetime.now()
    initialList = [86, 122, 70, 93, 102, 125, 110, 120, 73, 76, 21, 106, 1, 117, 40, 25, 52, 61, 19, 11, 45, 57, 51, 109, 6, 4, 100, 3, 69, 33, 16, 65, 108, 12, 15, 99, 84, 60, 104, 53, 74, 24, 103, 75, 18, 118, 123, 98, 64, 91, 107, 17, 26, 113, 36, 2, 63, 5, 116, 27, 85, 67, 78, 112, 82, 31, 83, 95, 97, 50, 115, 39, 35, 41, 9, 77, 20, 105, 72, 42, 14, 13, 49, 56, 92, 79, 7, 34, 71, 68, 43, 80, 81, 46, 66, 62, 87, 54, 59, 29, 111, 22, 44, 48, 90, 94, 38, 119, 114, 10, 121, 28, 58, 32, 89, 101, 37, 23, 88, 30, 124, 96, 47, 8, 55]
    a = objectivefunction(initialList)
    print("CURRENT SCORE " + str(a))
    print(initialList)
    finalList = SidewayMove_hill_climbing(initialList)
    b = objectivefunction(finalList)
    print("FINAL SCORE " + str(b))
    print(finalList)
    end = (datetime.datetime.now() - start)
    print("Total waktu : ", end)
    plt.plot(plotarray)
    plt.show()

main()