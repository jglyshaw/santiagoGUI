import random
from graphWrapper import MplCanvas
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class GraphPage(QMainWindow):
    def __init__(self): 
        super(GraphPage, self).__init__()
        
        self.setWindowTitle("Graph Page")
        self.window = QGridLayout()
        
        mainWidget = QWidget()
        mainWidget.setLayout(self.window)
        self.setCentralWidget(mainWidget)
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

        button3 = QPushButton("Clear")
        button3.clicked.connect(self.clear)

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)

        self.window.addWidget(self.sc,0,0)
        self.window.addWidget(button,0,1)
        self.window.addWidget(button3,0,2)
        self.window.addWidget(button3,2,0)

    def clear(self):
        self.sc.axes.clear()
        self.sc.draw()

    def graph(self):
        self.sc.axes.plot([0,1,2,3,4], [random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)])
        self.sc.draw()


    
  
