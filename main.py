from science import Attvud
from math import sqrt
from random import triangular
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Setup(Attvud):
    def __init__(self):
        super().__init__()
        self.science_wd = Attvud()

    def open_window(self):
        self.science_wd.show()

    def result(self):
        L = self.Lenght_box.text()
        l = self.Lenght_a_box.text()
        M = self.Mass_box.text()
        m = self.Extra_mass_box.text()

        g = 9.81
        t = sqrt((L ** 2 * (2 * M + m)) / (g * m * 2 * l))
        randt = triangular(t * 0.95, t * 1.05)
        self.Time_result.setText(str(randt)[:5] + ' c.')


#app = QtWidgets.QApplication(sys.argv)
#st = Setup()
#st.show()
#sys.exit(app.exec_())
