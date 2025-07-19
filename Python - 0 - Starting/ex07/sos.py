import sys


def string_to_morse(string):
    """
    Convert a string to Morse code.
    Args:
        string (str): The input string to convert
    Returns:
        str or None: Morse code representation of the input string,
                    or None if invalid characters are present
    """
    NESTED_MORSE = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----', ' ': '/'
    }

    for char in string.lower():
        if char not in NESTED_MORSE:
            return None
    return ' '.join(NESTED_MORSE[char] for char in string.lower())


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        result = string_to_morse(sys.argv[1])
        assert result is not None, "the arguments are bad"
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
