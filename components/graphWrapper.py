from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore

class MPLGraph(FigureCanvas):
    def __init__(self, is3d=False):
        self.fig = Figure(figsize=(300, 300), dpi=120)
        FigureCanvas.__init__(self,self.fig)
        self.fig.canvas.setFocusPolicy( QtCore.Qt.ClickFocus )
        self.fig.canvas.setFocus()
        self.fig.canvas.mpl_connect('key_press_event', self.on_press)
        self.axes=self.fig.add_subplot(111,projection="3d")
    
    def newPlot(self,x,y,z=None):
        self.axes.plot(x,y,z, color='g')
        self.draw()

    def clearGraph(self):
        self.axes.clear()
        self.draw()

    def hide_background(self):
        self.axes.grid(False)
        self.axes.set_axis_off()
        self.draw()

    def moveX(self,amount):
        self.axes.set_xbound(self.axes.get_xbound()[0]+amount, self.axes.get_xbound()[1]+amount)
        self.draw()
    
    def moveY(self,amount):
        self.axes.set_ybound(self.axes.get_ybound()[0]+amount, self.axes.get_ybound()[1]+amount)
        self.draw()

    def moveZ(self,amount):
        self.axes.set_zbound(self.axes.get_zbound()[0]+amount, self.axes.get_zbound()[1]+amount)
        self.draw()

    def on_press(self,event):
        if event.key == 'a':
            self.moveX(100)
        if event.key == 'd':
            self.moveX(-100)
        if event.key == 'w':
            self.moveY(100)
        if event.key == 's':
            self.moveY(-100)


    