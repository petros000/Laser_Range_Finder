from math import pi


class Target:
    """Target characteristics"""
    def __init__(self, reflection, area):
        # reflection - reflection coefficient target
        # area - target area, [m2]
        self.ro = 1
        self.s = 1

        if self.__is_valid_input(reflection) and reflection <= 1:
            self.ro = reflection
        if self.__is_valid_input(area):
            self.s = area

    @staticmethod
    def __is_valid_input(x):
        if type(x) in (int, float) and x > 0:
            return True
        return False

    def get_radiation_power(self, E):
        # E - laser power density, [W/m2]
        I = E / pi * self.ro * self.s
        return I



#t1 = Target(0.9, 2)
#print(t1.get_radiation_power(2000))