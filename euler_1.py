
def ap_sum(a: int, n:int) -> int:
    """
    Calculating sum of all the multiples of a upto nth terms using A.P.
    """
    return n*(2*a+(n-1)*a)//2

def sum_of_multiple(n1: int, n2: int, top: int) -> int:
    """
    Calculating sum of all the multiples of n1 or n2 below top using AUB formula ot set
    """
    return ap_sum(n1, top//n1) + ap_sum(n2, top//n2) - ap_sum(n1*n2, top//(n1*n2))

if __name__ == "__main__":
    print("The sum of all the multiples of 3 or 5 below 1000 is", sum_of_multiple(3, 5, 1000-1))
