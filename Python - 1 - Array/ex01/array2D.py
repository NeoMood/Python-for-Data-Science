import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape, and returns a truncated version
    based on the provided start and end arguments.

    Args:
        family: A 2D list.
        start: Start index for slicing.
        end: End index for slicing.

    Returns:
        The truncated 2D list.

    Raises:
        AssertionError: If validation checks fail.
    """
    try:
        assert isinstance(family, list), "Input must be a list."
        assert len(family) > 0, "List cannot be empty."
        assert isinstance(family[0], list), "Input must be a list of lists."

        row_len = len(family[0])
        for row in family:
            assert isinstance(row, list), "All elements must be lists."
            assert len(row) == row_len, "All rows must be the same size."

        arr = np.array(family)
        print(f"My shape is : {arr.shape}")

        new_arr = arr[start:end]
        print(f"My new shape is : {new_arr.shape}")

        return new_arr.tolist()

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []
    except KeyboardInterrupt:
        print("\nUser interrupted execution.")
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
