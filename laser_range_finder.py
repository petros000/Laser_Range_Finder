import gui_form_project
from atmosphere import Atmosphere
from laser import Laser
from receiver import Receiver
from target import Target
from functions import get_Range
import sys
from PyQt5 import QtWidgets


class Form_GUI(QtWidgets.QMainWindow, gui_form_project.Ui_MainWindow):

    def __init__(self):
        super().__init__()      # доступ к перменным, методам в form_LRF.py
        self.setupUi(self)      # инициализация дизайна
        self.input_data = {}
        self.__create_input_data()
        self.res = 0
        self.pushButton_Calculation.clicked.connect(self.calculation)

    def __create_input_data(self):
        self.input_data = {
            # параметры атмосферы
            'H_bot': int(self.spinBox_Height_bot.text()),
            'H_top': int(self.spinBox_Height_top.text()),
            "Temp": int(self.spinBox_Temperature.text()),
            "Vis": int(self.spinBox_Visibilit_range.text()),
            'lmd': float(self.doubleSpinBox_Wavelength.text().replace(',', '.')),

            # параметры цели
            'ro_tgt': float(self.doubleSpinBox_Reflection.text().replace(',', '.')),
            'S_tgt': float(self.doubleSpinBox_Area.text().replace(',', '.')),

            # параметры приемника
            "Dapp": float(self.doubleSpinBox_Diameter.text().replace(',', '.')),
            "tau": float(self.doubleSpinBox_Transmission_optics.text().replace(',', '.')),
            "sens": float(self.doubleSpinBox_Sensitivity.text().replace(',', '.')),
            "i_noise": float(self.doubleSpinBox_Noise_current.text().replace(',', '.')),
            "snr": float(self.doubleSpinBox_Signal_noise.text().replace(',', '.')),

            # параметры лазера
            "P_las": float(self.doubleSpinBox_Power.text().replace(',', '.')),
            "fi_las": float(self.doubleSpinBox_Divergence.text().replace(',', '.')),
        }

    def print_res(self, res):
        self.label_Range.setText(f'{str(res)} km')

    def calculation(self):
        self.__create_input_data()

        atmos = Atmosphere(self.input_data["H_bot"],
                           self.input_data["H_top"],
                           self.input_data["Vis"],
                           self.input_data["Temp"],
                           self.input_data["lmd"])

        las = Laser(self.input_data['fi_las'],
                    self.input_data['P_las'],
                    self.input_data['lmd'])

        targt = Target(self.input_data['ro_tgt'],
                      self.input_data['S_tgt'])

        receiv = Receiver(self.input_data['Dapp'],
                          self.input_data['sens'],
                          self.input_data['i_noise'],
                          self.input_data['tau'],
                          self.input_data['snr'])

        res = get_Range(las, targt, receiv, atmos)

        self.print_res(round(res / 1000, 1))


def start():
    app = QtWidgets.QApplication(sys.argv)
    window = Form_GUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
