import sys

if len(sys.argv) == 1:
    print()
    sys.exit(0)

try:
    assert len(sys.argv) == 2, (
        "AssertionError: more than one argument is provided"
    )
    try:
        argument = int(sys.argv[1])
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")
    if argument % 2 == 0:
        print("I'm Even.\n")
    else:
        print("I'm Odd.\n")
except AssertionError as e:
    print(e, "\n")
    sys.exit(1)
