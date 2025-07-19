import sys
import ft_filter


def filterstring(string, n):
    """
    Filter words from a string that are longer than n characters.

    Args:
        string (str): The input string to filter
        n (int): The minimum length threshold

    Returns:
        list: List of words longer than n characters
    """
    try:
        if not isinstance(string, str):
            raise TypeError("First argument must be a string")
        if not isinstance(n, int):
            raise TypeError("Second argument must be an integer")
        return list(ft_filter.ft_filter(lambda x: len(x) > n, string.split()))
    except Exception:
        print("AssertionError: the arguments are bad")
        sys.exit(1)


def main():
    try:
        if len(sys.argv) != 3 or not sys.argv[2].isdigit():
            print("AssertionError: the arguments are bad")
            sys.exit(1)
        print(filterstring(sys.argv[1], int(sys.argv[2])))
    except Exception:
        print("AssertionError: the arguments are bad")
        sys.exit(1)


if __name__ == "__main__":
    main()
