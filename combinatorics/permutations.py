from sys import argv
from math import factorial


# Flattens a list of lists
# for example [["go", "og"], ["rg", "gr"]] ---flatten---> ["go", "og", "rg", "gr"]
def flatten(l):
    return [item for sublist in l for item in sublist]

# Combines a character with every string in a list
def clcat(ch, l):
    strings = []
    input_list = l
    while True:
        try:  # try to combine char with all words in list
            for string in input_list:
                new_string = ch + string 
                strings.append(new_string)
            break
        except TypeError:
            input_list = flatten(input_list)
    return strings 


def permutations(string):
    if len(string) == 1:
        return string 
    elif len(string) == 2:
        return [string, string[::-1]]
    else:
        return list(
            map(
                lambda t: clcat(t[1], permutations(string[: t[0]] + string[t[0] + 1 :])),
                enumerate(string),
            )
        )

def sanity_check_passed(perms, string):
    return len(set(perms)) == factorial(len(string)) 

perms = flatten(permutations(argv[1]))
if sanity_check_passed(perms, argv[1]):
    for index, perm in enumerate(perms):
        print(f"{index + 1}: {perm}")
    print(f"\nThe total number of permutations of {argv[1]} is {factorial(len(argv[1]))}\n")
else:
    for perm in perms:
        print(perm)
    print("There is something wrong with your code")
