import sys
import matplotlib
import random
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class GraphPage(QVBoxLayout):
    def __init__(self): 
        super(GraphPage, self).__init__()
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        
        button = QPushButton('Graph')
        button.clicked.connect(self.graph)

        button3 = QPushButton('Clear')
        button3.clicked.connect(self.clear)

        self.addWidget(button)
        self.addWidget(button3)
        self.addWidget(self.sc)

    def clear(self):
        self.sc.axes.clear()
        self.sc.draw()

    def graph(self):
        self.sc.axes.plot([0,1,2,3,4], [random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)])
        self.sc.draw()


    
  
