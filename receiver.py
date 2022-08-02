class Receiver:
    """Receiver characteristics"""
    def __init__(self, diameter, sensitivity, noise_current):
        # diametr [mm]
        # noise_current [nA]
        self.d = 50
        self.s = 0.6
        self.i_noise = 10

        if self.__is_valid_input(diameter):
            self.d = diameter
        if self.__is_valid_input(sensitivity):
            self.s = sensitivity
        if self.__is_valid_input(noise_current):
            self.i_noise = noise_current

    @staticmethod
    def __is_valid_input(x):
        if type(x) in (int, float) and x > 0:
            return True
        return False

