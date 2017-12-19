import numpy as np
from matplotlib import pyplot as plt
from plagma import transformer as tr
from plagma import reverser as rv

if __name__ == "__main__":

    # x acis
    x_plot = np.linspace(0, 10, 100)
    x = np.linspace(0, 10, 100)

    # only random subset of data took from x
    rand = np.random.RandomState(0)
    rand.shuffle(x)
    x_train = np.sort(x[:20])
    y_train = tr.simple_sinusoid(x_train)

    # interpolate from subset
    X, Y = rv.poly_reverse(x_train,y_train,degree=5)

    #plot all curves
    plt.plot(x_plot, tr.simple_sinusoid(x_plot), c='g')
    plt.scatter(x_train,tr.simple_sinusoid(x_train))
    plt.plot(X, Y, c='r')
    plt.title("Interpolation vs Real Function")
    plt.show()

