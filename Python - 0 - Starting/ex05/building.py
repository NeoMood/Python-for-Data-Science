import sys


def analyze_text(text):
    """
    Analyze the given text and print statistics about its characters.

    Args:
        text (str): The text to analyze

    Prints:
        - Total character count
        - Number of upper case letters
        - Number of lower case letters
        - Number of punctuation marks
        - Number of spaces
        - Number of digits
    """
    try:
        char_count = len(text)
        upper_count = sum(1 for c in text if c.isupper())
        lower_count = sum(1 for c in text if c.islower())
        punct_count = sum(1 for c in text if c in
                          "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
        space_count = sum(1 for c in text if c.isspace())
        digit_count = sum(1 for c in text if c.isdigit())

        print(f"The text contains {char_count} characters:")
        print(f"{upper_count} upper letters")
        print(f"{lower_count} lower letters")
        print(f"{punct_count} punctuation marks")
        print(f"{space_count} spaces")
        print(f"{digit_count} digits")
    except Exception:
        print("AssertionError: an error occurred while analyzing the text")
        sys.exit(1)


def main():
    """
       Main function to handle user input and error handling.
    """
    try:
        if len(sys.argv) > 2:
            print("AssertionError: more than one argument is provided")
            sys.exit(1)

        if len(sys.argv) == 1:
            try:
                text = input("What is the text that you want to count?\n")
            except (EOFError, KeyboardInterrupt):
                print("\nAssertionError: no input provided")
                sys.exit(1)
        else:
            text = sys.argv[1]

        if not isinstance(text, str):
            print("AssertionError: input must be a string")
            sys.exit(1)

        if not text:
            print("AssertionError: empty text provided")
            sys.exit(1)

        analyze_text(text)

    except Exception:
        print("AssertionError: an unexpected error occurred")
        sys.exit(1)


if __name__ == "__main__":
    main()
