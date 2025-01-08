import sys


def print_info(text: str):
    """
    :param text:
    A function that outputs information about text.
    """
    str_len = len(text)
    upper_letters = sum(1 for c in text if c.isupper())
    lower_letters = sum(1 for c in text if c.islower())
    punctuation_characters = ".,!?;:'\"()[]{}-_/\\|&%$#@^*+=~`<>"
    punctuation_marks = sum(1 for c in text if c in punctuation_characters)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {str_len} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{punctuation_marks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    0 or 1 args: text
    0 args: after asking for text
    print the info about the text
    """
    argv = sys.argv
    argc = len(argv)

    try:
        if argc == 2:
            text = argv[1]
            print_info(text)
        elif argc == 1:
            try:
                text = input("What is the text to count?\n")
                print_info(text + "\n")
            except EOFError:
                pass
        else:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")

    return 0


if __name__ == "__main__":
    main()
