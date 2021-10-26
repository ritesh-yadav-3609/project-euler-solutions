from math import sqrt

prime = 0

def prime_factor(n: int) -> int:
    """
    Calculating largest prime factor of n
    """
    global prime
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            prime_factor(i)
            prime_factor(n//i)
            return prime
    if prime < n:
        prime = n

if __name__ == "__main__":
    print("The largest prime factor of the number 600851475143 is", prime_factor(600851475143))
