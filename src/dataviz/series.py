
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class Serie(object):
    
    def __init__(self,name,color='b'):
        
        self._x = []
        self._y = []
        self.name = name
        self.color= color

    def addItem(self,x_item,y_item):
        
        self._x.append(x_item)
        self._y.append(y_item)

    def clear(self):
        
        self._x.clear()
        self._y.clear()
    
    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def consume(self,value):
        x,y = value
        self.addItem(x,y)

    def __str__(self):
        
        return "serie {0} data {1}".format(self._name,len(self._y))
    

class AnimatedTimeSeries:

    def __init__(self, xrange, yrange, series=[]):

        self._xrange = xrange
        self._yrange = yrange
        self._series  = series
        self.fig, self.axis = plt.subplots(len(series),sharex=True)
        self._plots = []

    def _clear(self):

        for i, ax in enumerate(self.axis):
            serie = self._series[i]
            ax.set_xlim(self._xrange[0], self._xrange[1])
            ax.set_ylim(self._yrange[0], self._yrange[1])
            ax.set_title(serie.name)
            self._plots.append(*ax.plot([],[],serie.color, animated=True))

        return self._plots

    def _refresh(self,frame):
        
        for i , plot in enumerate(self._plots):
            plot.set_data(self._series[i].getX(),self._series[i].getY())

        return self._plots


    def start(self,frames=64,interval=10):
        ani = FuncAnimation(self.fig, self._refresh, frames=frames,init_func=self._clear, blit=True, interval=interval,repeat=False)
        plt.show()
       