from sys import argv

from crypto_ops import (ascii_string, c_totient, exponentiate_mod_n,
                        get_two_primes, inverse_mod_n, public_key_exponent)

message = argv[1]

[p1, p2] = get_two_primes()

n = p1 * p2  # modulus for private and public key
c = c_totient(p1, p2)
e = public_key_exponent(c)
d = inverse_mod_n(e, c)

print(
    f"The modulus is {n}. It's binary representation is {bin(n).replace('0b', '')}. The key length is {len(bin(n).replace('0b', ''))}."
)

print(f"The Carmichael Totient Function of {n} is {c}")

print(f"The public key exponent is {e}. The final public key is ({n}, {e}).")
print(f"The private key exponent is {d}. The final private key is ({n}, {d}).")

ascii = ascii_string(message)

encrypted = []

for m in ascii:
    encrypted.append(exponentiate_mod_n(m, e, n))

encrypted_message = ""
for e in encrypted:
    encrypted_message += chr(e)

print(encrypted_message)

decrypted = []

for c in encrypted:
    decrypted.append(exponentiate_mod_n(c, d, n))

decrypted_message = ""
for d in decrypted:
    decrypted_message += chr(d)

print(decrypted_message)
