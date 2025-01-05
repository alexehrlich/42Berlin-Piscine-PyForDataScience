from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def rgb2gray(rgb: np.ndarray) -> np.ndarray:
    """
    Converts an RGB image to grayscale using the luminosity method.
    """
    return (0.2989 * rgb[:, :, 0] +
            0.5870 * rgb[:, :, 1] +
            0.1140 * rgb[:, :, 2]).astype(int)


def transp(img: np.ndarray) -> np.ndarray:
    return [[row[i] for row in img] for i in range(len(img[0]))]


def main():
    try:
        img = ft_load("animal.jpg")
        print(img)
        mid_y = img.shape[0] // 2
        mid_x = img.shape[1] // 2
        zoomed = img[mid_y-200:mid_y+200, mid_x-200:mid_x+200, :]
        gray = rgb2gray(zoomed)
        print(f"The shape of the zoomed, gray image: {gray.shape}")
        print(gray)
        rotated = transp(gray)
        print(f"The shape of the rotated, gray image: {gray.shape}")
        plt.imshow(rotated, cmap='gray')
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
