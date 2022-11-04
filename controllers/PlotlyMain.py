import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QTextEdit, QWidget
from Plot import PlotLy

app = QApplication(sys.argv)

w = QMainWindow()

browser = PlotLy()

central_widget = QWidget()
w.setCentralWidget(browser.browser)
w.show()

sys.exit(app.exec_())