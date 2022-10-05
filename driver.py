from graph import GraphPage
from PyQt5.QtWidgets import *

def changeLayout(layout):
    QWidget().setLayout(window.layout())
    window.setLayout(layout)

app = QApplication([])
window = QWidget()

graph = GraphPage()
window.setLayout(graph)
window.setGeometry(200,200,1000,600)
window.show()

app.exec()







