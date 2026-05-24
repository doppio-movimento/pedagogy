from math import gcd
from random import randint


# Returns a list of two randomly selected primes
def get_two_primes():
    index1 = randint(0, 99)
    index2 = randint(0, 99)

    while index1 == index2:
        index1 = randint(0, 99)
        index2 = randint(0, 99)

    prime1 = PRIMES[index1]
    prime2 = PRIMES[index2]

    return [prime1, prime2]


# Compute Carmichael's Totient Function of n = p * q
def c_totient(p, q):
    x = p - 1
    y = q - 1
    return (x * y) // gcd(x, y)


# Generate a number e between 2 and lambda(n) such that
# gcd(e, lambda(n)) = 1.
def public_key_exponent(c):
    e = randint(3, c - 1)
    while gcd(e, c) != 1:
        e = randint(3, c - 1)
    return e


# Compute the inverse of a number modulo n
def inverse_mod_n(val, modulus):
    if gcd(val, modulus) != 1:
        raise ValueError("Modular inverse does not exist for the given input")

    mod_map = {}
    dividend = modulus
    divisor = val
    quotient = int(dividend / divisor)
    remainder = dividend % divisor
    mod_map[remainder] = -quotient * divisor
    if remainder == 1:
        return int((divisor - (divisor - 1) * mod_map[remainder]) / val) % modulus
    while remainder != 1:
        dividend = divisor
        divisor = remainder
        quotient, remainder = int(dividend / divisor), dividend % divisor
        mod_map[remainder] = (
            mod_map[dividend] if dividend in mod_map.keys() else dividend
        ) - mod_map[divisor] * quotient
    if dividend in mod_map.keys():
        return int((mod_map[dividend] - mod_map[divisor] * quotient) / val) % modulus
    else:
        return int((dividend - mod_map[divisor] * quotient) / val) % modulus


# Find the b^e mod n using a basic algorithm
def exponentiate_mod_n(b, e, n):
    result = 1
    exponentiations = 0
    while exponentiations < e:
        result = (b * result) % n
        exponentiations += 1
    return result


# Convert a message to ASCII codes
def ascii_string(message):
    ascii = []
    for char in message:
        ascii.append(ord(char))
    return ascii


PRIMES = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
    317,
    331,
    337,
    347,
    349,
    353,
    359,
    367,
    373,
    379,
    383,
    389,
    397,
    401,
    409,
    419,
    421,
    431,
    433,
    439,
    443,
    449,
    457,
    461,
    463,
    467,
    479,
    487,
    491,
    499,
    503,
    509,
    521,
    523,
    541,
]
