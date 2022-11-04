

from PyQt5.QtWidgets import *
from controllers.Graph3D import Graph3D
from controllers.MLEngine import MLEngine
from controllers.Plot import PlotLy

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
        self.graph = PlotLy()

        #add widgets
        self.window.addWidget(self.graph.browser,0,0)
        self.window.addWidget(button,1,0)
        self.window.addWidget(clear,4,0)
        self.window.addWidget(move,3,0)
        self.window.addWidget(graph2,2,0)


    def graphNodes(self):

        self.graph.graph()

       
    def graphEdges(self):
        nodes = self.MLEngine.nodesDictionary(self.neuron)
        edges = self.MLEngine.edgesList(self.neuron, nodes)

        self.graph.linePlot(edges)
        self.graph.fig.canvas.setFocus()
       


