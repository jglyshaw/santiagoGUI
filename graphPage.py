import random
from graphWrapper import MplCanvas
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class GraphPage(QMainWindow):
    def __init__(self): 
        super(GraphPage, self).__init__()
        
        self.setWindowTitle("Graph Page")
        self.window = QGridLayout()
        
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.window)
        self.setCentralWidget(self.mainWidget)
        self.initUI()


    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        button = QPushButton("Graph")
        button.clicked.connect(self.graph)


        clear = QPushButton("Clear")
        clear.clicked.connect(self.clear)
        self.graph = MplCanvas(is3d=True)
        self.window.addWidget(self.graph,0,0)
        self.window.addWidget(button,1,0)
        self.window.addWidget(clear,2,0)

    def clear(self):
        self.graph.axes.clear()
        self.graph.draw()

    def graph(self):
        x = [0,1,2,3,4]
        y = [random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)]
        height = random.randint(1,4)
        z = [height,height,height,height,height]
        self.graph.axes.plot(x,y,z)
        self.graph.draw()


    
  
