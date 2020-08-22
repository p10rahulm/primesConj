import numpy as np
import math


def get_primes_upto(n):
    """ Returns  a list of primes <= n """
    n += 1
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [1, 2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


def is_prime(n):
    # We use 1 as prime for the purpose of this algo
    if n == 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True


def test_get_primes_upto():
    print("Testing function get_primes_upto()")
    for iterate in range(1, 12):
        print('%d: %s' % (iterate, get_primes_upto(iterate)))
    print("Finished testing function get_primes_upto()\n\n")


def test_is_prime():
    print("Testing function is_prime()")
    for iterate in range(1, 12):
        print('%d: %s' % (iterate, is_prime(iterate)))
    print("Finished testing function is_prime()\n\n")


# test_is_prime()
# test_get_primes_upto()

def check_A_equals_2BplusC(A, candidate_BC):
    for B in candidate_BC:
        for C in candidate_BC:
            if A == 2 * B + C:
                return B, C
    return 0, 0


def checkConjecture(upperLimit):
    conjectureFalse = 0
    for iterateA in range(3, upperLimit):
        if is_prime(iterateA):
            candidate_BC = get_primes_upto(iterateA // 2)
            B, C = check_A_equals_2BplusC(iterateA, candidate_BC)
            if B == 0 or C == 0:
                print("ERROR!!! A = ", iterateA, " has no solutions A = 2B+C where B,C in ", candidate_BC)
                conjectureFalse = iterateA
            else:
                print("%d = 2 x %d + %d" % (iterateA, B, C))
    return conjectureFalse


if __name__ == "__main__":
    limit = 100000
    conjectureFalse = checkConjecture(limit)
    if not conjectureFalse:
        print("Conjecture is true for primes between 3 and ", limit)
    else:
        print("Conjecture failed at %d for primes between 3 and %d"%(conjectureFalse, limit))
