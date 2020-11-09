# Name: Shah Mir Ali Bin Kamran

import random           # for selecting a random number
from math import log    # for pi function
import sys


def check_number(numk):
    """
    Simply runs the miller rabin function to check if the number is prime or not. It loops using the range - pi function
    in slides.
    :param numk: the input
    :return: prints to terminal if number is prime using miller rabin check
    """

    num_maxi = pow(2, int(numk))
    num_max = num_maxi - 1  # Max value of the range
    num_min = pow(2, int(numk) - 1)  # Min value of the range
    # Number of primes in this range
    primes = (num_max / log(num_max)) - (num_min / log(num_min))  # use of prime function as in the slides
    primes = round(primes)

    rang = num_max - num_min  # Selecting a random number in the above range

    loop = rang - primes + 1  # loop this many times no prime found

    number = random.randrange(num_min, num_max)
    i = 0
    run = miller_rabin(number)
    while run is False and i < loop + 1:
        number = random.randrange(num_min, num_max)
        run = miller_rabin(number)
        i += 1
    if run is True:
        print(number)
    else:
        print("No prime found")


def miller_rabin(n, k=64):
    """

    :param n: the number that is tested
    :param k: determining the accuracy of the test
    :return: if the number is prime or not. True/False
    """

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


if __name__ == "__main__":

    argument_00 = sys.argv[0]
    number = int(sys.argv[1])

    check_number(number)
