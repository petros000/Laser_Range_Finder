class Receiver:
    """Receiver characteristics"""
    def __init__(self, diameter, sensitivity, noise_current):
        self.d = diameter
        self.s = sensitivity
        self.i_noise = noise_current
