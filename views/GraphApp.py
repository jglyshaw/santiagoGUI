

from PyQt6.QtWidgets import *
from controllers.Graph3D import Graph3D
from controllers.MLEngine import MLEngine

class GraphApp(QWidget):
    def __init__(self): 
        super(GraphApp, self).__init__()
        self.setWindowTitle("GraphApp")
        self.window = QGridLayout()
        self.setLayout(self.window)
        self.initUI()

        self.MLEngine = MLEngine()
        self.neuron = self.MLEngine.createNeuron(185, 't')


    def initUI(self):
        #buttons
        button = QPushButton("Nodes")
        button.clicked.connect(self.graphNodes)

        graph2 = QPushButton("Edges")
        graph2.clicked.connect(self.graphEdges)

        clear = QPushButton("Clear")
        clear.clicked.connect(lambda : self.graph.clearGraph())

        move = QPushButton("Hide Grid")
        move.clicked.connect(lambda : self.graph.hide_background())
        
        #graph component
        self.graph = Graph3D()

        #add widgets
        self.window.addWidget(self.graph,0,0)
        self.window.addWidget(button,1,0)
        self.window.addWidget(clear,4,0)
        self.window.addWidget(move,3,0)
        self.window.addWidget(graph2,2,0)


    def graphNodes(self):
        nodes = self.MLEngine.nodesDictionary(self.neuron)
        x = []
        y = []
        z = []
        for id in nodes:
            x1,y1,z1 = nodes[id]
            x.append(x1)
            y.append(y1)
            z.append(z1)
        self.graph.scatterPlot(x,y,z)

       
    def graphEdges(self):
        nodes = self.MLEngine.nodesDictionary(self.neuron)
        edges = self.MLEngine.edgesList(self.neuron, nodes)

        self.graph.linePlot(edges)
        self.graph.fig.canvas.setFocus()
       


