from main import calculate_module_height, calculate_row_gap


def test_calculate_module_height():
    assert (calculate_module_height(1.755, 10) < 0.304755) and (calculate_module_height(1.755, 10) > 0.30475)


def test_calculate_row_gap():
    assert (calculate_row_gap(1, 45) > 0.999999) and (calculate_row_gap(1, 45) < 1.0000001)
