import sys
from apps.GraphApp import GraphApp
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
w = GraphApp()
w.show()
app.exec()