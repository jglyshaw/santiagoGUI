from PyQt5.QtWidgets import *

class View1(QVBoxLayout):

    def __init__(self): 
        super(View1, self).__init__()
       
        button = QPushButton('Top')
        self.addWidget(button)

        self.addWidget(QPushButton('Bottom'))

        layout2 = QVBoxLayout()
        layout2.addWidget(QPushButton('button1'))
        layout2.addWidget(QPushButton('button2'))
