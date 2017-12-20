
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class AnimatedTimeSeries:

    def __init__(self, xrange, yrange):

        self._xrange = xrange
        self._yrange = yrange
        self._xdata = []
        self._ydata = []
        self.fig, self.axis = plt.subplots()
        self.ln, = plt.plot([],[], 'ro', animated=True)

    def _clear(self):
        self.axis.set_xlim(self._xrange[0], self._xrange[1])
        self.axis.set_ylim(self._yrange[0], self._yrange[1])
        self._xdata.clear()
        self._ydata.clear()
        return self.ln,

    def _refresh(self,frame):
        print("refreshing {0}".format(frame))
        self.ln.set_data(self._xdata, self._ydata)
        return self.ln,

    def consume(self,value):
        x,y = value
        print("consuming x={0} and y={1}".format(x,y))
        self._xdata.append(x)
        self._ydata.append(y)

    def start(self,frames=64,interval=20):
        ani = FuncAnimation(self.fig, self._refresh, frames=frames,init_func=self._clear, blit=True, interval=interval)
        plt.show()
       