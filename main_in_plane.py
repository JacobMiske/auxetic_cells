# TRL
# Jacob Miske

from math import *
from itertools import *
import numpy as np
import matplotlib.pyplot as plt


class auxetic_cell:
    # Class to describe an individual auxetic bilayer cell
    def __init__(self, x, y):
        self.arm_length = 2                                       # [cm]
        self.arms = 4
        self.layers = 2
        self.center_x = x
        self.center_y = y
        self.top_layer_angle = 0                                  # [radians]
        self.bottom_layer_angle = 45                              # [radians]
        self.arm_angle = 2*(np.pi)/(float(self.arms)) # [radians]
        self.arm_positions = []
    def connect(self):
        # connects a cell to another cell
        print('not ready')
    def update_arm_positions(self):
        # rewrites arm positions based on connections
        print('not ready')
    def get_position_list(self):
        cell_positions = []
        cell_center = [self.center_x, self.center_y]
        cell_positions.append(cell_center)
        # assume equally spaced arms in angle
        # First four cell positions are for top layer
        for i in range(4):
            cell_i_position = [self.arm_length * np.sin(i * self.arm_angle + self.top_layer_angle),
                               self.arm_length * np.cos(i * self.arm_angle + self.top_layer_angle)]
            cell_positions.append(cell_i_position)
        # Second four cell positions are for bottom layer
        for j in range(4):
            cell_j_position = [self.arm_length * np.sin(j * self.arm_angle + self.bottom_layer_angle),
                               self.arm_length * np.cos(j * self.arm_angle + self.bottom_layer_angle)]
            cell_positions.append(cell_j_position)
        return cell_positions


def get_relu(a, b):
    # returns ReLU function response
    return lambda x: max(0, a*(x-b))


def plot_auxetic_cell(list_of_cell_positions):
    # for a cell, plot it's position in space
    plt.figure(0)
    center_x = list_of_cell_positions[0][0]
    center_y = list_of_cell_positions[0][1]
    xs = [i[0] for i in list_of_cell_positions]
    ys = [j[1] for j in list_of_cell_positions]
    for point in list_of_cell_positions[1:]:
        plt.plot([center_x, point[0]], [center_y, point[1]], 'b')
    plt.scatter(xs, ys)
    plt.show()
    plt.close()


if __name__ == '__main__':
    cell1 = auxetic_cell(x=0, y=0)
    cell1_positions = cell1.get_position_list()

    plot_auxetic_cell(list_of_cell_positions=cell1_positions)

    # Set fixed variable of the structures shape
    link_length = 2 # [cm]

    ReLU_example = get_relu(1, 1)
    ReLU_example(5)

    a11 = lambda x, y: get_relu(1, 0.564)(x)
    print(list(takewhile(lambda x: x > 0, accumulate(range(10, 2000), a11))))
    target = [0.6]