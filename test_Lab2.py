import Lab2 as l2

def test_find_min_max():
    expected_result = [1,7]
    input = [1,2,3,4,5,6,7]
    result = l2.find_min_max(input)

    assert (result == expected_result)

def test_calc_average():
    expected_result = 3.5
    input = [1,2,3,4,5,6]
    result = l2.calc_averge(input)

    assert(result == expected_result)

def test_calc_median_temperature_():
    expected_result = 4
    input = [1,2,3,4,5,6,7]
    result = l2.calc_median_temperature(input)

    assert(result == expected_result)