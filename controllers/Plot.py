
from PyQt5.QtWebEngineWidgets import QWebEngineView
import plotly.offline as po
import plotly.graph_objs as go
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import numpy as np


class PlotLy():
    def __init__(self):

        z = np.linspace(0, 1, 100)
        x = z * np.sin(25 * z)
        y = z * np.cos(25 * z)
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
        fig.write_image("fig1.png")


        raw_html = '<html><head><meta charset="utf-8" />'
        raw_html += '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
        raw_html += '<body>'
        raw_html += po.plot(fig, include_plotlyjs=False, output_type='div')
        raw_html += '</body></html>'

        self.browser  = QWebEngineView()
        self.browser.setHtml(raw_html)
        self.browser.show()
        self.browser.raise_()
