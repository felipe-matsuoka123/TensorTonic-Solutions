import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    x = np.asarray(x)
    m = np.max(x, axis=-1, keepdims=True)
    
    probabilities = np.exp(x - m) / np.sum(np.exp(x - m), axis=-1, keepdims=True)
    
    return  probabilities