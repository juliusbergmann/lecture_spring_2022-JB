from main import calculate_module_height, calculate_row_gap
import numpy as np
import math


def test_calculate_module_height():
    np.testing.assert_equal(calculate_module_height(1.755, 10), 1.755 * math.sin(10 * 2 * math.pi / 360))
    # assert (calculate_module_height(1.755, 10) < 0.304755) and (
    #    calculate_module_height(1.755, 10) > 0.30475)


def test_calculate_row_gap():
    assert (calculate_row_gap(1, 45) > 0.999999) and (
        calculate_row_gap(1, 45) < 1.0000001)
