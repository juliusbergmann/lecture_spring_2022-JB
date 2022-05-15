# Assignment for OSESM 2022
# This program calculates the needed gap between multiple rows of PV-modules

import math

# length of panel in m
module_length = 1.755
# angle of module in degree
module_angle = 10


def calculate_module_height(length, angle):
    return length * math.sin(angle * 2 * math.pi / 360)


module_height = calculate_module_height(module_length, module_angle)


print(module_height)

