from receiver import Receiver


def test_1_init():
    rec = Receiver(100, 1.0, 100, 1.0)
    assert (rec.d == 100 * 10**-3 and rec.s == 1.0 and rec.i_noise == 100 * 10**-9 and rec.tau_opt == 1.0)


def test_2_init():
    rec = Receiver(0, 10, 0, 0.9)
    assert (rec.d == 50 * 10**-3 and rec.s == 0.6 and rec.i_noise == 10 * 10**-9 and rec.tau_opt == 0.9)


def test_3_init():
    rec = Receiver(-1, -1, -1, 20)
    assert (rec.d == 50 * 10**-3 and rec.s == 0.6 and rec.i_noise == 10 * 10**-9 and rec.tau_opt == 0.8)


def test_4_power_signal():
    rec = Receiver(100, 0.5, 25, 0.8)
    assert (round(rec.get_power_signal(100, 1_000), 9) == 6.28 * 10 ** -7)


def test_5_SNR():
    rec = Receiver(100, 1, 25, 1)
    P = rec.get_power_signal(10, 1_000)
    assert (round(rec.get_SNR(P), 2) == 3.14)


