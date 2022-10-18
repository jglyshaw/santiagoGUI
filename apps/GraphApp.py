

from PyQt6.QtWidgets import *
from components.Graph3D import Graph3D
import matlab.engine
import random

class GraphApp(QWidget):
    def __init__(self): 
        super(GraphApp, self).__init__()
        self.setWindowTitle("GraphApp")
        self.window = QGridLayout()
        # self.eng = matlab.engine.start_matlab()
        self.setLayout(self.window)
        self.initUI()


    def initUI(self):
        #buttons
        button = QPushButton("Graph")
        button.clicked.connect(self.graphData)

        clear = QPushButton("Clear")
        clear.clicked.connect(lambda : self.graph.clearGraph())

        move = QPushButton("Hide Grid")
        move.clicked.connect(lambda : self.graph.hide_background())
        
        #graph component
        self.graph = Graph3D()

        #add widgets
        self.window.addWidget(self.graph,0,0)
        self.window.addWidget(button,1,0)
        self.window.addWidget(clear,2,0)
        self.window.addWidget(move,3,0)


    def graphData(self):
        a  = 0
        b = 4000
        x = []
        y = []
        z = []

        for i in range(2000): 
            a += 1
            b -= 1
            x.append(random.randint(a,b))
            y.append(random.randint(a,b))
            z.append(a)

        self.graph.newPlot(x,y,z)

    def graphData2(self):
        x = list(self.eng.data()[0])
        y = list(self.eng.data()[1])
        z = list(self.eng.data()[2])

        self.graph.newPlot(x,y,z)


if __name__ == "__main__":
    app = QApplication([])
    w = GraphApp()
    w.show()
    app.exec()