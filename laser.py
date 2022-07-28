from math import tan, pi, radians


class Laser:
    """Laser characteristics"""
    def __init__(self, divergence, power, wavelength):
        # divergence, fi - radiation divergence (расходимость излучения), [angular minute], [уг.мин]
        # P - radiation power impulse (импульсная мощность излучения), [MW], [МВт]
        # wavelength - [mkm]
        self.fi = 1
        self.P = 1 * 10 ** 6
        self.lmd = 1.06

        if self.__is_valid_input(divergence) :
            self.fi = divergence
        if self.__is_valid_input(power):
            self.P = power * 10**6
        if self.__is_valid_input(wavelength):
            self.lmd = wavelength

    @staticmethod
    def __is_valid_input(x):
        if type(x) in (int, float) and x > 0:
            return True
        return False

    def get_power_density(self, R):
        """return power density without Atmosphere"""
        # R - range, [m]
        # E - power density, [W/m2]
        S = pi / 4 * (tan(radians(self.fi/60)) * R) ** 2 # square
        E = self.P / S
        return E


# l1 = Laser(2, 6)
# print(l1.get_power_density(10000))

