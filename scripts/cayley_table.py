from sys import argv

BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"

BLACK_BG = "\033[1;40m"
RED_BG = "\033[1;41m"
GREEN_BG = "\033[1;42m"
YELLOW_BG = "\033[1;43m"
BLUE_BG = "\033[1;44m"
MAGENTA_BG = "\033[1;45m"
CYAN_BG = "\033[1;46m"
WHITE_BG = "\033[1;47m"

elements = list(map(int, argv[1].split(",")))
operation = argv[2]

def phi(a, b):
    if operation == "+":
        result = a + b
    elif operation == "*":
        result = a * b
    elif "mod" in operation:
        modulus = int(operation[4:])
        if operation[0] == "+":
            result = (a + b) % modulus
        else:
            result = (a * b) % modulus
    return str(result)

def cayley_table(elems, func):
    string = ""
    string += GREEN + (len(elems) + 1) * " _____ " + "\n"
    string += (len(elems) + 1) * "|     |" + "\n"
    string += "|  " + YELLOW + "*" + GREEN + "  |"
    for elem in elems:
        string += "|  " + WHITE + str(elem) + GREEN + "  |"
    string += "\n" + (len(elems) + 1) * "|_____|" + "\n"
    for elem in elems:
        string += (len(elems) + 1) * "|     |" + "\n"
        string += "|  " + WHITE + str(elem) + GREEN + "  |"
        for i in range(0, len(elems)):
            string += "|  " + phi(elem, elems[i]) + "  |"
        string += "\n" + (len(elems) + 1) * "|_____|" + "\n"

    return string

print(cayley_table(elements, phi) + BLACK)
