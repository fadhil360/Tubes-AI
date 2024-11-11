from Creating import *
import random
import datetime
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import datetime
import math

max_iteration = int(input("banyak iterasi (default = 1000) = "))
if max_iteration <= 0:
    max_iteration = 1000
max_duration = int(input("duration (default = 120) = "))
if max_duration <= 0:
    max_duration = 120
max_temperature = int(input("temperature (default = 12000) = "))
if max_temperature <= 0:
    max_temperature = 12000
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
        i += 1
        if end >= max_duration:
            break

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

# Visualization code


def display_3d_cube(data):
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
    plt.title("3D Cube Visualization with Simulated Annealing Results")

    plt.show()


# Run the simulated annealing process and visualize results
initialList = initial()
print("Initial list:", initialList)
finalList = Simulated_Annealing(initialList)
print("Final list:", finalList)

# Reshape finalList to 5x5x5 for visualization
final_array = np.array(finalList).reshape((5, 5, 5))
display_3d_cube(final_array)
