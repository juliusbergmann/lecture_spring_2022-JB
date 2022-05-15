# Assignment for OSESM 2022
# This program calculates the needed gap between multiple rows of PV-modules

import math
# angle of the sun in degree
sun_angle = 18.5
# length of panel in m
module_length = 1.755
# angle of module in degree
module_angle = 10


def calculate_module_height(length, angle):
    return length * math.sin(angle * 2 * math.pi / 360)


module_height = calculate_module_height(module_length, module_angle)


def calculate_row_gap(height, angle_sun):
    return height / math.tan(angle_sun * 2 * math.pi / 360)


row_gap = calculate_row_gap(module_height, sun_angle)

print("The minimum gap between rows of panels with\n"
      "a module length of", module_length, "m and an construction angle of", module_angle,
      "° \nis", '{0:.3f}'.format(row_gap), "m.")

