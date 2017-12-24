
import os
import numpy as np
from matplotlib import pyplot as plt
from plagma import transformer as tr
from plagma import reverser as rv
from simulator import virtualSensor as v
from dataviz import series
from threading import Event
from storage.queue import azureService as az
from json import load

def try_interpolate(deg=5):
    
    # x acis
    x_plot = np.linspace(0, 10, 100)
    x = np.linspace(0, 10, 100)

    # only random subset of data took from x
    rand = np.random.RandomState(0)
    rand.shuffle(x)
    x_train = np.sort(x[:20])
    y_train = tr.simple_sinusoid(x_train)

    # interpolate from subset
    X, Y = rv.poly_reverse(x_train,y_train,degree=deg)

    #plot all curves
    plt.plot(x_plot, tr.simple_sinusoid(x_plot), c='g')
    plt.scatter(x_train,tr.simple_sinusoid(x_train))
    plt.plot(X, Y, c='r')
    plt.title("Interpolation vs Real Function")
    plt.show()


def try_animated_interpolation():
    
    #cancellation token
    canceller = Event()

    #consumer
    animator = series.AnimatedTimeSeries((0,120),(-100,100))

    #data producer
    sensor = v.VirtualSensor("1",animator.consume,event=canceller)
    sensor.start()

    #start visualization in real time
    animator.start(frames=12000)

    #stop data production when ploting windows is closed
    canceller.set()


def animate_on_azure(accountName,accountKey):
    
    #consumer
    queue = az.AzureQueue(accountName,accountKey)
    consumer = lambda v : queue.push_message("sensor",str(v))

    #cancellation token
    canceller = Event()

    #data producer
    sensor = v.VirtualSensor("1",consumer,event=canceller)
    sensor.start()


def load_azure_settings(filename):

    with open(filename) as _file:
        return load(_file)


if __name__ == "__main__":


    settings = load_azure_settings(os.path.os.path.dirname(__file__)+"/appsettings.json")
    account = settings['storage_account']
    key = settings['storage_account_key']

    animate_on_azure(account,key)
