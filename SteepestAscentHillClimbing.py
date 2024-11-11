from Creating import *
import datetime
import matplotlib.pyplot as plt

plotarray=[]
max_duration = 120


def SteepestAscent_hill_climbing(list):
    current_list = list[:]
    current_value = objectivefunction(current_list)
    global i
    i = 0
    start = datetime.datetime.now()
    end = 0
    print(i, " : ", current_value)
    while True:
        neighbor_list = highestneighbor(current_list)
        if current_value < objectivefunction(neighbor_list):
            current_value=objectivefunction(neighbor_list)
            current_list=neighbor_list
            i += 1
            print(i, " : ", current_value)
            plotarray.append(current_value)
        else :
            break
        end = (datetime.datetime.now() - start).seconds
        if end >= max_duration:
            break
    return current_list
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
        plt.title("Final 3D Cube Visualization with SteepestAscent")
    else:
        plt.title("Initial 3D Cube Visualization with SteepestAscent")

    plt.show()

def main():
    start = datetime.datetime.now()
    initialList = initial()
    a = objectivefunction(initialList)
    print("CURRENT SCORE " + str(a))
    print(initialList)
    finalList = SteepestAscent_hill_climbing(initialList)
    b = objectivefunction(finalList)
    print("FINAL SCORE " + str(b))
    print(finalList)
    end = (datetime.datetime.now() - start)
    print("Total waktu : ", end)
    print("Total iterasi : ", i)
    initial_array = np.array(initialList).reshape((5, 5, 5))
    display_3d_cube(initial_array,2)
    final_array = np.array(finalList).reshape((5, 5, 5))
    display_3d_cube(final_array,1)
    plt.plot(plotarray)
    plt.show()

main()