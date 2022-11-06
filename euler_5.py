
from math import sqrt

def is_prime(n: int) -> bool:
    """
    Checking if n is prime number
    """
    for i in range(3, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def highest_power_number_below(n, r):
    """
    Calculating highest power of n below r
    """
    num = n
    for i in range(1, r):
        if num * n > r: 
            break
        num = num * n
    return num

def smallest_divisible_number(n: int) -> int:
    """
    Smallest positive number that is evenly divisible by all of the numbers below n
    """
    total = highest_power_number_below(2, n)
    for i in range(3, n+1):
        if is_prime(i):
            total = total * highest_power_number_below(i, n)
    return total

if __name__ == "__main__":
    print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is", smallest_divisible_number(20))
