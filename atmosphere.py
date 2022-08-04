from math import exp, log


class Atmosphere:
    """Calculation of atmospheric parameters"""
    def __init__(self, height_bot, height_top, visibility_range, temperature, wavelength):

        self.h_bot = 0   # [m]
        self.h_top = 1000   # [m]
        self.vis = 20   # [km]
        self.t = 21     # [C]
        self.P0 = 1013  # [mbar]
        self.lmd = 1.06     # [mkm]

        if self.__is_valid_input(height_bot):
            self.h_bot = height_bot     # [m]
        if self.__is_valid_input(height_top):
            self.h_top = height_top     # [m]
        if self.__is_valid_input(visibility_range):
            self.vis = visibility_range     # [km]
        if type(temperature) in (int, float):
            self.t = temperature        # [C]
        if self.__is_valid_input(wavelength):
            self.lmd = wavelength       # [mkm]

    @staticmethod
    def __is_valid_input(x):
        if type(x) in (int, float) and x > 0:
            return True
        return False

    def aerosol_attenuation_indicator(self, height):
        # alpha [1/m]
        alpha = 3.91 / (self.vis * 10**3) * (0.55 / self.lmd) ** 1.3 * exp(- height * 10**-3 / (5 / log(self.vis - 6.65)))

        return alpha

    def molecular_attenuation_indicator(self, height):
        # betta [1/m]
        # height [m]
        T_h = lambda x: self.t + 273 - 0.0065 * height      # [K]
        P_h = lambda x: self.P0 * (1 - height / 44308)**5.255  # [mbar]
        betta = 1.09 * 10**-6 * self.lmd ** -4 * P_h(height) / self.P0 * (self.t + 273) / T_h(height)

        return betta

    def get_transmission_coefficient(self, distance):
        # range [m]
        res = 1
        step_height = 50    # [m]
        n = round(abs(self.h_top - self.h_bot) / 50)
        step_distance = distance / (n + 1)    # [m]

        for i in range(n + 1):
            height_cur = i * step_height + self.h_bot
            alpha_cur = self.aerosol_attenuation_indicator(height_cur)
            betta_cur = self.molecular_attenuation_indicator(height_cur)
            coef_cur = exp(-(alpha_cur + betta_cur) * step_distance)
            res *= coef_cur

        return res


atm1 = Atmosphere(0, 500, 20, -50, 1.06)
print(atm1.get_transmission_coefficient(25_000))
# print(atm1.aerosol_attenuation_indicator(5000))
print(atm1.molecular_attenuation_indicator(25_000))
