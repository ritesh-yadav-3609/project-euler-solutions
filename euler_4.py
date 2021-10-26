
def is_palindrome(n: int) -> bool:
    """
    Checking if n is palindrome
    """
    return str(n) == str(n)[::-1]

def largest_palindrome_product(n: int) -> int:
    """
    Largest palindrome made from the product of two numbers below n 
    """
    num = 0
    r = n - 10**(len(str(n))//2)
    for i in range(n, r, -1):
        for j in range(i, r, -1):
            if is_palindrome(i*j) and num < (i*j):
                num = i*j
    return num
    
if __name__ == "__main__":
    print("The largest palindrome made from the product of two 3-digit numbers is", largest_palindrome_product(9))
    


