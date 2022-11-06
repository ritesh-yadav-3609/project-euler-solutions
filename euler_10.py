import datetime
from math import sqrt

def is_prime(n: int) -> bool:
    """
    Checking if n is prime number
    """
    for i in range(3, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def sum_of_prime_below(n: int) -> int:
    """
    Return sum of all the primes below n
    """
    total = 2
    i = 3
    d1 = datetime.datetime.now()
    while i < n:
        if is_prime(i):
            total = total + i
        i = i + 2
    d2 = datetime.datetime.now()
    print(d2-d1)
    return total

if __name__ == "__main__":
    print("The sum of all the primes below two million is", sum_of_prime_below(2000000))
