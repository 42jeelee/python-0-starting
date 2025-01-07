import sys


argv = sys.argv
argc = len(argv)

try:
    assert argc == 2, "more than one argument is provided"

    value = argv[1]

    try:
        if int(value) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        raise AssertionError("argument is not an integer")
except AssertionError as e:
    print(f"AssertionError: {e}")
