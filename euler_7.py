
ls = []

def is_prime(n: int) -> bool:
    """
    Checking if n is prime number
    """
    global ls
    for i in ls:
        if n%i == 0:
            return False
    return True

def nth_prime(n: int) -> int:
    """
    Return nth prime number
    """
    global ls
    ls.append(2)
    i = 3
    while len(ls) < n:
        if is_prime(i):
            ls.append(i)
        i = i + 2
    return ls.pop()

if __name__ == "__main__":
    print("The 10001st prime number is", nth_prime(10001))
