import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import pandas as pd
__all__ = ['rand_array','smooth_image','my_mat_solve','test']
def smooth_image(a, sigma=1):
 return gaussian_filter(a, sigma=sigma)

def rand_array(shape):
    return np.random.rand(*shape)
def my_mat_solve(A, b):
    return A.inv()*b

def test():
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    return df