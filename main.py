import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from apps.GraphApp import GraphApp

class MainApp(QTabWidget):
   def __init__(self, parent = None):
      super(MainApp, self).__init__(parent)
      self.tab1 = QWidget()
      self.tab2 = QWidget()
      self.tab3 = GraphApp()
		
      self.addTab(self.tab1,"Tab 1")
      self.addTab(self.tab2,"Tab 2")
      self.addTab(self.tab3,"GraphApp")
      self.setWindowTitle("Main App")
		

	
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainApp()
   window.show()
   sys.exit(app.exec())