from math import pi


class Target:
    """Target characteristics"""
    def __init__(self, reflection, area):
        # reflection - reflection coefficient target
        # area - target area, [m2]
        self.ro = reflection
        self.s = area

    def get_radiation_power(self, E):
        # E - laser power density, [W/m2]
        I = E / pi * self.ro * self.s
        return int(I)


t1 = Target(0.9, 2)
print(t1.get_radiation_power(2000))