

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
        self.setLayout(self.window)
        self.initUI()

        self.MLEngine = MLEngine()
        self.neuron = self.MLEngine.createNeuron(182, 't')


    def initUI(self):
        #buttons
        button = QPushButton("Graph")
        button.clicked.connect(self.graphNeuron)

        graph2 = QPushButton("Graph2")
        graph2.clicked.connect(self.graphNeuron2)

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
        self.window.addWidget(graph2,4,0)


    def graphNeuron(self):
        nodes = self.MLEngine.nodes(self.neuron)
        x = []
        y = []
        z = []

        for id in nodes:
            x1,y1,z1 = nodes[id]
            x.append(x1)
            y.append(y1)
            z.append(z1)

        self.graph.scatterPlot(x,y,z)

       
    def graphNeuron2(self):
        nodes = self.MLEngine.nodes(self.neuron)
        edges = self.MLEngine.edges(self.neuron, nodes)
      
        x = []
        y = []
        z = []
        for edge in edges:
            
            x.append(edge[0][0])
            x.append(edge[1][0])
            y.append(edge[0][1])
            y.append(edge[1][1])
            z.append(edge[0][2])
            z.append(edge[1][2])
        self.graph.linePlot(x,y,z)

       


