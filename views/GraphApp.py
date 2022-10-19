

from PyQt6.QtWidgets import *
from controllers.Graph3D import Graph3D
from controllers.MLEngine import MLEngine
import matlab.engine
import random

class GraphApp(QWidget):
    def __init__(self): 
        super(GraphApp, self).__init__()
        self.setWindowTitle("GraphApp")
        self.window = QGridLayout()
        self.MLEngine = MLEngine()
        self.setLayout(self.window)
        self.neuron = self.MLEngine.createNeuron(189, 't')
        self.initUI()


    def initUI(self):
        #buttons
        button = QPushButton("Graph")
        button.clicked.connect(self.graphNeuron)

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


    def graphNeuron(self):
        nodes = self.MLEngine.nodes(self.neuron)
        x = []
        y = []
        z = []
        for id, x1,y1,z1 in nodes:
            x.append(x1)
            y.append(y1)
            z.append(z1)

        self.graph.scatterPlot(x,y,z)


        x = []
        y = []
        z = []
        for i in range(20):
            x.append(random.randrange(1,1000))
            y.append(random.randrange(1,1000))
            z.append(random.randrange(1,1000))
        self.graph.linePlot(x,y,z)

       

