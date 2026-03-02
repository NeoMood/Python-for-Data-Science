from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Load image, zoom (slice), convert to grayscale, and display.
    """
    try:
        img = ft_load("animal.jpeg")

        assert img is not None, "Failed to load image"

        print(img)

        sliced_img = img[100:500, 450:850, :]

        r, g, b = (sliced_img[:, :, 0],
                   sliced_img[:, :, 1],
                   sliced_img[:, :, 2])

        gray_img = 0.2989 * r + 0.5870 * g + 0.1140 * b

        gray_img = gray_img.astype(np.uint8)

        gray_img = np.expand_dims(gray_img, axis=2)

        print(f"New shape after slicing: {gray_img.shape} "
              f"or ({gray_img.shape[0]}, {gray_img.shape[1]})")
        print(gray_img)
        plt.imshow(gray_img, cmap='gray')
        plt.show()

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        print("\nUser interrupted execution.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
