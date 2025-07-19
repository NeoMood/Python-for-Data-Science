import sys

if len(sys.argv) == 1:
    sys.exit(0)

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided\n")
    sys.exit(1)

try:
    argument = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer\n")
    sys.exit(1)

if argument % 2 == 0:
    print("I'm Even.\n")
else:
    print("I'm Odd.\n")
