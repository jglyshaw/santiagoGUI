from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class MplCanvas(FigureCanvas):
    def __init__(self, is3d=False):
        self.fig=Figure()
        self.degreesVertical = 0
        self.degreesHoriztonal = 0
        FigureCanvas.__init__(self,self.fig)
        
        self.fig.clear()

        if is3d:
            self.axes=self.fig.add_subplot(111,projection="3d")
        else:
            self.axes=self.fig.add_subplot(111)

        self.toolbar = NavigationToolbar(self, self)


 