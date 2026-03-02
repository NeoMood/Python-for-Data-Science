
import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values from lists of heights and weights.

    Args:
        height: List of heights in meters (int or float).
        weight: List of weights in kg (int or float).

    Returns:
        List of BMI values.

    Raises:
        AssertionError: If validation checks fail.
    """
    try:
        assert len(height) == len(weight), "Lists must be the same size."

        for h, w in zip(height, weight):
            assert isinstance(h, (int, float)), \
                "Elements must be int or float."
            assert isinstance(w, (int, float)), \
                "Elements must be int or float."
            assert h > 0, "Height must be positive."

        np_height = np.array(height)
        np_weight = np.array(weight)
        bmi = np_weight / (np_height ** 2)
        return bmi.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return None
    except KeyboardInterrupt:
        print("\nUser interrupted execution.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if BMI values are above a given limit.

    Args:
        bmi: List of BMI values (int or float).
        limit: Threshold value (int).

    Returns:
        List of booleans (True if above limit, False otherwise).
    """
    try:
        for val in bmi:
            assert isinstance(val, (int, float)), \
                "BMI values must be int or float."

        np_bmi = np.array(bmi)
        return (np_bmi > limit).tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return None
    except KeyboardInterrupt:
        print("\nUser interrupted execution.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """
    Main function.
    """
    pass


if __name__ == "__main__":
    main()
