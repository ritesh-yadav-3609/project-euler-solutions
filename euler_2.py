
def even_fibonacci_sum(n: int) -> int:
    """
    Calculating sum of the even-valued terms Fibonacci sequence 
    whose values do not exceeding n
    """
    a = 1
    b = 2
    s = 0
    t = b
    while s < n:
        if s%2 == 0:
            t = t + s
        s = a + b
        a = b
        b = s
    return t

if __name__ == "__main__":
    print("The sum of the even-valued terms Fibonacci sequence whose values do not exceed four million is", even_fibonacci_sum(4000000))
