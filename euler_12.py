import datetime
from math import sqrt

def divisors_count(n: int) -> int:
    """
    Return number of divisors for n
    """
    count = 2
    inc = 2
    if n%2 == 0:
        count = count + 2
        inc = 1
    for i in range(3, int(sqrt(n))+1, inc):
        if n%i == 0:
            count = count + 2
    if int(sqrt(n))**2 == n:
        count = count - 1
    return count

def sum_of_numbers(n: int) -> int:
    """
    Calculating sum of the first n nature numbers
    """
    return (n*(n+1))//2

def triangle_number(d: int) -> int:
    """
    Return value of the first triangle number to have over n divisors
    """
    i = d
    d1 = datetime.datetime.now()
    while divisors_count(sum_of_numbers(i)) < d:
        i = i + 1
    d2 = datetime.datetime.now()
    print(d2-d1)
    return i

if __name__ == "__main__":
    print("The value of the first triangle number to have over five hundred divisors is", triangle_number(500))
