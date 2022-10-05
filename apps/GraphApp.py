import random
from components.graphWrapper import MPLGraph
from PyQt5.QtWidgets import *

class GraphApp(QMainWindow):
    def __init__(self): 
        super(GraphApp, self).__init__()
        self.setWindowTitle("GraphApp")
        self.window = QGridLayout()
        
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.window)
        self.setCentralWidget(self.mainWidget)
        self.initUI()


    def initUI(self):

        #menubar
        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        #buttons
        button = QPushButton("Graph")
        button.clicked.connect(self.graph)

        clear = QPushButton("Clear")
        clear.clicked.connect(lambda : self.graph.clearGraph())
        
        #graph component
        self.graph = MPLGraph(is3d=True)

        #add widgets
        self.window.addWidget(self.graph,0,0)
        self.window.addWidget(button,1,0)
        self.window.addWidget(clear,2,0)


    def graph(self):
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