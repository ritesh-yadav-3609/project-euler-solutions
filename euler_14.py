
def chain(n: int) -> int:
    chain_length = 1
    while n != 1:
        chain_length = chain_length + 1
        if n%2 == 0:
            n = n//2
        else:
            n =  3*n + 1
    return chain_length

def number_of_chain(n: int) -> int:
    """
    Return value of starting number, under n, produces the longest chain is
    """
    chain_length = 0
    num = 0
    for i in range(1, n):
        temp = chain(i)
        if chain_length < temp:
            num = i
            chain_length = temp
    return num

if __name__ == "__main__":
    """
    The following iterative sequence is defined for the set of positive integers:
        n → n/2 (n is even)
        n → 3n + 1 (n is odd)
    """
    print("The starting number, under one million, produces the longest chain is", number_of_chain(1000000))
