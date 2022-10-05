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
        x = [random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20)]
        y = [random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20)]
        height = random.randint(1,100)
        z = [random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20)]
        self.graph.axes.plot(x,y,z)
        self.graph.draw()


    
  
