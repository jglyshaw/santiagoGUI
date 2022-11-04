import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from views.GraphApp import GraphApp
from controllers.Graph3D import Graph3D
from controllers.Plot import PlotLy

class MainApp(QTabWidget):
   def __init__(self, parent = None):
      super(MainApp, self).__init__(parent)
      tab1 = PlotLy()
      self.tab2 = Graph3D()
      self.tab3 = GraphApp()
		
      self.addTab(tab1.browser,"Tab 1")
      self.addTab(self.tab2,"Tab 2")
      self.addTab(self.tab3,"GraphApp")
      self.setWindowTitle("Main App")
		

	
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainApp()
   window.show()
   sys.exit(app.exec())