from math import pi


class Receiver:
    """Receiver characteristics"""
    def __init__(self, diameter, sensitivity, noise_current, transmission_optics, signal_noise_ratio=3):
        # diameter [mm]
        # noise_current [nA]
        self.d = 50 * 10**-3
        self.s = 0.6
        self.i_noise = 10 * 10**-9
        self.tau_opt = 0.8
        self.snr = 3

        if self.__is_valid_input(diameter):
            self.d = diameter * 10**-3
        if self.__is_valid_input(sensitivity) and sensitivity <= 1:
            self.s = sensitivity
        if self.__is_valid_input(noise_current):
            self.i_noise = noise_current * 10**-9
        if self.__is_valid_input(transmission_optics) and transmission_optics <= 1:
            self.tau_opt = transmission_optics
        if self.__is_valid_input(signal_noise_ratio):
            self.snr = signal_noise_ratio

    @staticmethod
    def __is_valid_input(x):
        if type(x) in (int, float) and x > 0:
            return True
        return False

    def get_power_signal(self, I, Range):
        # I [W/sr]
        # Range [m]
        P = I * pi / 4 * (self.d ** 2) / (Range ** 2) * self.tau_opt
        return P

    def get_SNR(self, P):
        snr = P * self.s / self.i_noise
        return snr



#vrec = Receiver(100, 0.5, 25, 0.8)
#vprint(rec.get_power_signal(100, 1_000))

