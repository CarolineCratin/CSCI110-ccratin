import nsum

def test_sum():
    assert nsum.sum([1,2,3]) == 6

def test_noth():
    assert nsum.sum([]) == 0

def test_again():
    assert nsum.sum([600,50,2]) == 652