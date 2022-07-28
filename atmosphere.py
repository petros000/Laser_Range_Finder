from math import exp, log


class Atmosphere:
    """Calculation of atmospheric parameters"""
    def __init__(self, height_bot, height_top, visibility_range, temperature):
        self.h_bot = height_bot     # [m]
        self.h_top = height_top     # [m]
        self.vis = visibility_range     # [km]
        self.t = temperature        # [C]
        self.P0 = 1013              # [mbar]

    def aerosol_attenuation_indicator(self, height, wavelength):
        # alpha [1/m]
        alpha = 3.91 / (self.vis * 10**3) * (0.55 / wavelength) ** 1.3 * exp( height * 10**-3 * log(self.vis - 6.65) / 5)

        return alpha

    def molecular_attenuation_indicator(self, height, wavelength):
        # betta [1/m]
        # height [m]
        # wavelength [mkm]
        T_h = lambda x: self.t + 273 - 0.0065 * height      # [K]
        P_h = lambda x: self.P0 * (1 - height / 44308)**5.255  # [mbar]
        betta = 1.09 * 10**-6 * wavelength**-4 * P_h(height) / self.P0 * self.t / T_h(height)

        return betta

    def get_transmission_coefficient(self, distance, wavelength):
        # range [m]
        # wavelength [mkm]
        res = 1
        step_height = 50    # [m]
        n = round(abs(self.h_top - self.h_bot) / 50)
        step_distance = distance / (n + 1)    # [m]

        for i in range(n + 1):
            height_cur = i * step_height + self.h_bot
            alpha_cur = self.aerosol_attenuation_indicator(height_cur, wavelength)
            betta_cur = self.molecular_attenuation_indicator(height_cur, wavelength)
            coef_cur = exp(-(alpha_cur + betta_cur) * step_distance)
            res *= coef_cur

        return res


#atm1 = Atmosphere(0, 0, 10, 21)
#print(atm1.get_transmission_coefficient(10000, 1.06))

