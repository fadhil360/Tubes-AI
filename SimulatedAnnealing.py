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

plotarray=[]
temperaturplot=[]
temperaturploti=[]
max_duration = int(input("duration (default = 120) = "))
if max_duration > 0:
    truth = 1
else:
    max_duration = 120
max_temperature = int(input("temperature (default = 12000) = "))
if max_temperature > 0:
    truth = 1
else:
    max_temperature = 12000
stuck = 0


def Simulated_Annealing(list):
    global stuck
    global i
    i = 0
    current_list = list[:]
    current_value = objectivefunction(current_list)
    temperature = max_temperature  # Set suhu awal
    cooling_rate = 0.99  

    start = datetime.datetime.now()
    end = 0
    while True:
        print(i, " : ", current_value)
        plotarray.append(current_value)

        # Pilih tetangga secara acak
        neighbor_list = neighbor(current_list)
        neighbor_value = objectivefunction(neighbor_list)

        # Hitung probabilitas untuk menerima solusi yang lebih buruk
        if neighbor_value < current_value:
            annealing = math.exp((neighbor_value - current_value) / temperature)
            temperaturplot.append(annealing)
            temperaturploti.append(i)

            # Acak nilai peluang untuk memutuskan apakah solusi yang lebih buruk diterima
            chance = random.random()  # Menghasilkan nilai antara 0 dan 1
            if chance < annealing:
                current_list = neighbor_list  # Terima solusi lebih buruk
                current_value = neighbor_value
            else:
                stuck += 1  # Hitung jumlah stuck
        else:
            # Jika tetangga lebih baik, terima langsung
            current_list = neighbor_list
            current_value = neighbor_value

    
        temperature *= cooling_rate
        end = (datetime.datetime.now() - start).seconds


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
print("Frekuensi stuck : ", stuck/i)
print("Total iterasi : ", i)
# Visualization code


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
        plt.title("Final 3D Cube Visualization with Simulated Annealing")
    else:
        plt.title("Initial 3D Cube Visualization with Simulated Annealing")

    plt.show()



# Reshape finalList to 5x5x5 for visualization
initial_array = np.array(initialList).reshape((5, 5, 5))
display_3d_cube(initial_array,2)
final_array = np.array(finalList).reshape((5, 5, 5))
display_3d_cube(final_array,1)
plt.plot(plotarray)
plt.title("Plot objective function terhadap banyak iterasi")
plt.show()
plt.scatter(temperaturploti,temperaturplot)
plt.title("Plot temperature terhadap banyak iterasi")
plt.show()
