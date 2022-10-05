import random
from components.graphWrapper import MplCanvas
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


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
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
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
        self.graph = MplCanvas(is3d=True)

        #add widgets
        self.window.addWidget(self.graph,0,0)
        self.window.addWidget(button,1,0)
        self.window.addWidget(clear,2,0)


    def graph(self):
        a = 1
        b = 200
        x = [random.randint(a,b),random.randint(a,b),random.randint(a,b),random.randint(a,b),random.randint(a,b)]
        y = [random.randint(a,b),random.randint(a,b),random.randint(a,b),random.randint(a,b),random.randint(a,b)]
        z = [random.randint(a,b),random.randint(a,b),random.randint(a,b),random.randint(a,b),random.randint(a,b)]
        self.graph.newPlot(x,y,z)