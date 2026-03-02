from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its format, and its pixels content in RGB format.

    Args:
        path: The path to the image file.

    Returns:
        The image as a numpy array.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("File not found.")

        with Image.open(path) as img:
            img_rgb = img.convert('RGB')

            arr = np.array(img_rgb)

            print(f"The shape of image is: {arr.shape}")
            return arr

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []
    except KeyboardInterrupt:
        print("\nUser interrupted execution.")
        return []
    except Image.UnidentifiedImageError:
        print("Error: Cannot identify image file (corrupted or unsupported).")
        return []
    except PermissionError:
        print("Error: Permission denied.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    """
    Main function.
    """
    pass


if __name__ == "__main__":
    main()
