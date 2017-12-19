from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
import numpy as np

def poly_reverse(x_train ,y_train, degree=2, x_range=(0,10)):
    """
        Execute a polynomial interpolation
        of the given input array. This method
        use the non-linear regression model
        also called ridge regression
    """

    #Built a set of sequential transformation
    x = x_train[:,np.newaxis]
    model = make_pipeline(PolynomialFeatures(degree),Ridge())
    model.fit(x,y_train)
    plot_x_area = np.linspace(x_range[0],x_range[1],100)[:,np.newaxis]
    plot_y_area = model.predict(plot_x_area)

    return plot_x_area,plot_y_area
