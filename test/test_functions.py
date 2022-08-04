from functions import get_Range
from atmosphere import Atmosphere
from laser import Laser
from receiver import Receiver
from target import Target


def test_1_get_Range():

    atmos = Atmosphere(5000, 5500, 20, 20, 1.06)
    las = Laser(1.5, 3.5, 1.06)
    targt = Target(0.25, 1.5)
    receiv = Receiver(50, 0.6, 10, 0.5, 3)

    assert (round(get_Range(las, targt, receiv, atmos) / 1000, 0) == 15)