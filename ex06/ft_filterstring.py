import sys
from ft_filter import ft_filter


def main():
    """
    only 2 args: text and word_len
    print the words that are longer or equal to word_len
    """
    argv = sys.argv
    argc = len(argv)

    try:
        assert argc == 3, "the arguments are bad"
        text = argv[1]

        try:
            word_len = int(argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        print(list(ft_filter(lambda x: len(x) >= word_len, text.split())))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    return 0


if __name__ == "__main__":
    main()
