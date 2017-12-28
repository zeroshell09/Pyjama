import numpy as np

def simple_sinusoid(x):
    """
        process given numpy based array using sinus function
        param x: the integer to encrypt
        Return the processed result
    """
    return x * np.sin(x)