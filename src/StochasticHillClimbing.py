from Creating import *
import datetime
import matplotlib.pyplot as plt

plotarray = []
max_duration = int(input("duration (default = 120) = "))
if max_duration > 0:
    truth = 1
else:
    max_duration = 120


def stochastic_hill_climbing(list):
    global i
    i = 0
    current_list = list[:]
    current_value = objectivefunction(current_list)
    i = 0
    start = datetime.datetime.now()
    end = 0
    while True:
        plotarray.append(current_value)
        neighbor_list = neighbor(current_list)
        neighbor_value = objectivefunction(neighbor_list)
        if neighbor_value > current_value:
            current_list = neighbor_list
            current_value = objectivefunction(current_list)
        end = (datetime.datetime.now() - start).seconds
        i += 1
        print(i, " : ", current_value)

        if end >= max_duration:
            break
    return current_list


def display_3d_cube(data, end):
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
    if end == 1:
        plt.title("Final 3D Cube Visualization with Stochastic")
    else:
        plt.title("Initial 3D Cube Visualization with Stochastic")

    plt.show()


def display_3d_cube(data, end):
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
    if end == 1:
        plt.title("Final 3D Cube Visualization with Stochastic")
    else:
        plt.title("Initial 3D Cube Visualization with Stochastic")

    plt.show()


def main():
    start = datetime.datetime.now()
    initialList = initial()
    finalList = stochastic_hill_climbing(initialList)

    a = objectivefunction(initialList)
    print("START SCORE " + str(a))
    print(initialList)

    b = objectivefunction(finalList)
    print("FINAL SCORE " + str(b))
    print(finalList)

    end = (datetime.datetime.now() - start)
    print("Total waktu : ", end)
    initial_array = np.array(initialList).reshape((5, 5, 5))
    display_3d_cube(initial_array, 2)
    final_array = np.array(finalList).reshape((5, 5, 5))
    display_3d_cube(final_array, 1)
    plt.plot(plotarray)
    plt.show()
    print("Total iterasi : ", i)


main()
