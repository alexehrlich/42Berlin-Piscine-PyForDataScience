import array
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    np_img = np.array(array)
    inverted = 255 - np_img
    plt.imshow(inverted)
    plt.show()
    return inverted


def ft_red(array) -> array:
    """
    Turns of the blue and green channel of the image received.
    """
    red = array[:, :, 0]
    green = np.zeros_like(red)
    blue = np.zeros_like(red)
    red_rgb = np.stack((red, green, blue), axis=2)
    plt.imshow(red_rgb)
    plt.show()
    return red_rgb


def ft_green(array) -> array:
    """
    Turns of the blue and red channel of the image received.
    """
    green = array[:, :, 1]
    red = np.zeros_like(green)
    blue = np.zeros_like(green)
    green_rgb = np.stack((red, green, blue), axis=2)
    plt.imshow(green_rgb)
    plt.show()
    return green_rgb


def ft_blue(array) -> array:
    """
    Turns of the red and green channel of the image received.
    """
    blue = array[:, :, 2]
    red = np.zeros_like(blue)
    green = np.zeros_like(blue)
    blue_rgb = np.stack((red, green, blue), axis=2)
    plt.imshow(blue_rgb)
    plt.show()
    return blue_rgb


def ft_grey(array) -> array:
    """
    Converts an RGB image to grayscale using the luminosity method.
    """
    gray = (0.2989 * array[:, :, 0] +
            0.5870 * array[:, :, 1] +
            0.1140 * array[:, :, 2]).astype(int)
    plt.imshow(gray, cmap='grey')
    plt.show()
    return gray
