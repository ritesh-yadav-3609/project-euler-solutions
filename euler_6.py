
def square_of_sum_of(n: int) -> int:
    """
    Calculating square of the sum of n nature numbers
    """
    return n*(n+1)*((2*n)+1)//6

def sum_of_squares_of(n: int) -> int:
    """
    Calculating sum of the squares of n nature numbers
    """
    return ((n*(n+1))//2)**2

def difference(n: int) -> int:
    """
    Difference between the sum of the squares of and the square of the sum first one nth natural numbers
    """
    return sum_of_squares_of(n) - square_of_sum_of(n)

if __name__ == "__main__":
    print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is", difference(100))
