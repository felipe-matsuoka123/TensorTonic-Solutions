import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    x = np.asarray(x)
    sigmoid_value = 1 / (1 + np.power(np.e, -x))
    return sigmoid_value