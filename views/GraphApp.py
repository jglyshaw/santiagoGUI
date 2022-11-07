

from PyQt5.QtWidgets import *
from controllers.Graph3D import Graph3D
from controllers.MLEngine import MLEngine
from controllers.Plot import PlotLy
from matplotlib import cm
import numpy as np

class GraphApp(QWidget):
    def __init__(self): 
        super(GraphApp, self).__init__()
        self.setWindowTitle("GraphApp")
        self.window = QGridLayout()
        self.setLayout(self.window)
        self.initUI()

        self.mlEngine = MLEngine()
        


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
        neuron = self.mlEngine.createNeuron(182, 't')
        nodes = self.mlEngine.nodesDictionary(neuron)
        edges = self.mlEngine.edgesList(neuron, nodes)
        x = []
        y = []
        z = []
        for id in nodes:
            x1,y1,z1,area1 = nodes[id]
            x.append(x1)
            y.append(y1)
            z.append(z1)
        self.graph.scatterPlot(x,y,z)

        # for line in edges:
        #     a = line[0]
        #     b = line[1]
        #     self.graph.linePlot([a[0],b[0]],[a[1],b[1]],[a[2],b[2]])
        # self.graph.linePlot(edges)
        surface = self.mlEngine.eng.GetSurface(neuron)


        x = np.asarray(surface[0][0])
        y = np.asarray(surface[0][1])
        z = np.asarray(surface[0][2])
        i = 0
        for segment in surface:
            if i == 0:
                i += 1
                continue
            x = np.concatenate((x, segment[0]))
            y = np.concatenate((y, segment[1]))
            z = np.concatenate((z, segment[2]))
        self.graph.surfacePlot(x, y, z)

        self.graph.update()


        print("done1")
        print("done")


       
    def graphEdges(self):
        self.graph.move()
       


