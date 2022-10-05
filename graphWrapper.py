from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, is3d=False):
        self.fig=Figure()
        FigureCanvas.__init__(self,self.fig)
        
        self.fig.clear()

        if is3d:
            self.axes=self.fig.add_subplot(111,projection="3d")
        else:
            self.axes=self.fig.add_subplot(111)