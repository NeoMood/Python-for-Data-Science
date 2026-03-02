import numpy as np
import matplotlib.pyplot as plt


def _display(array: np.ndarray, title: str):
    """Helper to display image."""
    try:
        plt.imshow(array)
        plt.title(title)
        plt.axis('off')
        plt.show()
    except KeyboardInterrupt:
        pass
    except Exception:
        pass


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    res = 255 - array
    _display(res, "Figure VIII.2: Invert")
    return res


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the red color channel.
    """
    res = array.copy()
    res[:, :, 1] = res[:, :, 1] * 0
    res[:, :, 2] = res[:, :, 2] * 0
    _display(res, "Figure VIII.3: Red")
    return res


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green color channel.
    """
    res = array.copy()
    res[:, :, 0] = res[:, :, 0] - res[:, :, 0]
    res[:, :, 2] = res[:, :, 2] - res[:, :, 2]
    _display(res, "Figure VIII.4: Green")
    return res


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue color channel.
    """
    res = array.copy()
    res[:, :, 0] = 0
    res[:, :, 1] = 0
    _display(res, "Figure VIII.5: Blue")
    return res


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale.
    """
    res = array.copy()
    s = np.sum(array, axis=2) / 3

    res[:, :, 0] = s
    res[:, :, 1] = s
    res[:, :, 2] = s

    _display(res, "Figure VIII.6: Grey")
    return res
