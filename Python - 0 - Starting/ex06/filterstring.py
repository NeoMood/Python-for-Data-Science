import sys
from ft_filter import ft_filter


def filterstring(string, n):
    """
    Filter words from a string that are longer than n characters.

    Args:
        string (str): The input string to filter
        n (int): The minimum length threshold

    Returns:
        list: List of words longer than n characters
    """
    assert isinstance(string, str), "the arguments are bad"
    assert isinstance(n, int), "the arguments are bad"
    return list(ft_filter(
        lambda x: len(x) > n,
        string.split()
    ))


def main():
    try:
        assert (
            len(sys.argv) == 3 and sys.argv[2].isdigit()
        ), "the arguments are bad"
        print(filterstring(
            sys.argv[1],
            int(sys.argv[2])
        ))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
