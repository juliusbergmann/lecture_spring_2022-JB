from main import calculate_module_height, calculate_row_gap
import numpy as np
import math


def test_calculate_module_height():
    np.testing.assert_equal(calculate_module_height(1.755, 10), 1.755 * math.sin(10 * 2 * math.pi / 360))


def test_calculate_row_gap():
    np.testing.assert_equal(calculate_row_gap(1, 45), 1 / math.tan(45 * 2 * math.pi / 360))
