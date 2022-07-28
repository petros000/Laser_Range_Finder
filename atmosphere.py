class Atmosphere:
    """Calculation of atmospheric parameters"""
    def __init__(self, height_bot, height_top, season, visibility_range):
        self.h_bot = height_bot
        self.h_top = height_top
        self.season = season
        self.vis = visibility_range

    def get_transmission_coefficient(self, range, wavelength):
        pass

