import trik

def test_swithing_everything():
    assert(trik.switches("ABABCBA") == 3)

def test_swithing_nothin():
    assert(trik.switches("NUHUH") == 1)

def test_swithing_A():
    assert(trik.switches("A") == 2)