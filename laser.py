from math import tan, pi, radians


class Laser:
    """Laser characteristics"""
    def __init__(self, fi, power, wavelength):
        # fi - radiation divergence (расходимость излучения), [angular minute], [уг.мин]
        # P - radiation power impulse (импульсная мощность излучения), [MW], [МВт]
        # wavelength - [mkm]
        self.fi = fi
        self.P = power * 10**6

    def get_power_density(self, R):
        """return power density without Atmosphere"""
        # R - range, [m]
        # E - power density, [W/m2]
        S = pi / 4 * (tan(radians(self.fi/60)) * R) ** 2 # square
        E = self.P / S
        return int(E)


#l1 = Laser(2, 6)
#print(l1.get_power_density(10000))

