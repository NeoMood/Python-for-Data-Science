from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Load image, cut a square part, make it black and white,
    transpose it manually, and display.
    """
    try:
        img = ft_load("animal.jpeg")
        print(img)

        assert img is not None, "Failed to load image"

        sliced_img = img[100:500, 450:850, :]

        r, g, b = (sliced_img[:, :, 0],
                   sliced_img[:, :, 1],
                   sliced_img[:, :, 2])

        gray_img = 0.2989 * r + 0.5870 * g + 0.1140 * b
        gray_img = gray_img.astype(np.uint8)

        gray_zoomed = np.expand_dims(gray_img, axis=2)
        print(f"The shape of image is: {gray_zoomed.shape} "
              f"or ({gray_zoomed.shape[0]}, {gray_zoomed.shape[1]})")
        print(gray_zoomed)

        rows, cols = gray_img.shape
        transposed_data = np.zeros((cols, rows), dtype=int)

        for i in range(rows):
            for j in range(cols):
                transposed_data[i][j] = gray_img[j][i]

        print(f"New shape after Transpose: {transposed_data.shape}")
        print(transposed_data)

        plt.imshow(transposed_data, cmap='gray')
        plt.show()

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        print("\nUser interrupted execution.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
