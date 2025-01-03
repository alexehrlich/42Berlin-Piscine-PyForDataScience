import matplotlib.image as mpimg
import os
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Loads an image for a given path. matplotlib works with np.ndarray
    internally but with RGB color format.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    
    if os.path.isdir(path):
        raise IsADirectoryError(f"Path is a directory: {path}")

    try:
        img = mpimg.imread(path)

        if not isinstance(img, np.ndarray):
            raise ValueError(f"Invalid image format at path: {path}")

        print(f"The shape of the image is: {img.shape}")
        return img
    except Exception as e:
        raise ValueError(f"Failed do open image at {path}. {e}")

