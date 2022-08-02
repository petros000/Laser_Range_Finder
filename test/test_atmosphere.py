from atmosphere import Atmosphere


def test_1_init():
    atm = Atmosphere(5000, 5500, 20, 21, 1.06)
    assert (atm.h_top == 5500 and
            atm.h_bot == 5000 and
            atm.vis == 20 and
            atm.t == 21 and
            atm.lmd == 1.06)


def test_2_init():
    atm = Atmosphere(-10, -100, 0, 0, -1)
    assert (atm.h_bot == 0 and
            atm.h_top == 1000 and
            atm.vis == 20 and
            atm.t == 0 and
            atm.lmd == 1.06)


def test_3_aerosol():
    atm = Atmosphere(5000, 5500, 20, 21, 1.06)
    assert (round(atm.aerosol_attenuation_indicator(5000) * 10**6, 2) == 6.24)


def test_4_molecul():
    atm = Atmosphere(5000, 5500, 20, 21, 1.06)
    assert (round(atm.molecular_attenuation_indicator(5000) * 10**8, 2) == 3.70)


def test_5_coeff():
    atm = Atmosphere(5000, 5500, 20, 21, 1.06)
    assert (round(atm.get_transmission_coefficient(25_000), 2) == 0.87)
