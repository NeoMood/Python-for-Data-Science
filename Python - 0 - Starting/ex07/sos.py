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
    morse_code_dict = {
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
        if char not in morse_code_dict:
            return None
    return ' '.join(morse_code_dict[char] for char in string.lower())


def main():
    try:
        if len(sys.argv) != 2:
            print("AssertionError: the arguments are bad")
            sys.exit(1)
        result = string_to_morse(sys.argv[1])
        if result is None:
            print("AssertionError: the arguments are bad")
            sys.exit(1)
        print(result)
    except Exception:
        print("AssertionError: the arguments are bad")
        sys.exit(1)


if __name__ == "__main__":
    main()
