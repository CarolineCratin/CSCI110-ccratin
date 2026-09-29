import cold

def test_num():
    assert(cold.low([3, 5, 6, -4]) == 1)

def test_num2():
    assert(cold.low([7,-5,65,-8765,9,-3]) == 3)

def test_num3():
    assert(cold.low([0, 6]) == 0)