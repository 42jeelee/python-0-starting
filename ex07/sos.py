import sys


def main():
    """
    Morse code converter
    only 1 args: text
    """
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/',
    }
    argv = sys.argv
    argc = len(argv)

    try:
        assert argc == 2, "the arguments are bad"

        result = ""
        for c in argv[1].upper():
            assert c in NESTED_MORSE, "the arguments are bad"
            result += NESTED_MORSE[c]
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    return 0


if __name__ == "__main__":
    main()
