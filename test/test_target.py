from target import Target


def test_1_init():
    tgt = Target(0.5, 10)
    assert (tgt.ro == 0.5 and tgt.s == 10)


def test_2_init():
    tgt = Target(0, 10)
    assert (tgt.ro == 1 and tgt.s == 10)


def test_3_init():
    tgt = Target(-1, -1)
    assert (tgt.ro == 1 and tgt.s == 1)


def test_4_rad_pow():
    tgt = Target(1, 1)
    assert (tgt.get_radiation_power(100) == 31.8)


def test_5_rad_pow():
    tgt = Target(0, 0)
    assert (tgt.get_radiation_power(100) == 31.8)



