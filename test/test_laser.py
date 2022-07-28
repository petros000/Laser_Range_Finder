from laser import Laser


def test_1_init():
    las = Laser(0.5, 10, 1.5)
    assert (las.fi == 0.5 and las.P == 10 * 10**6 and las.lmd == 1.5)


def test_2_init():
    las = Laser(0, 10, 20)
    assert (las.fi == 1 and las.P == 10 * 10**6 and las.lmd == 20)


def test_3_init():
    las = Laser(-1, -1, 0)
    assert (las.fi == 1 and las.P == 1 * 10 ** 6 and las.lmd == 1.06)


def test_4_pow_dens():
    las = Laser(1, 1, 1.5)
    assert (round(las.get_power_density(1_000) / 100000, 1) == 150.5)


def test_5_pow_dens():
    las = Laser(-1, -1, -1)
    assert (round(las.get_power_density(1_000) / 100000, 1) == 150.5)
