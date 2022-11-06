
def product_of_pythagorean_triplet(n: int) -> int:
    """
    Return value of product of Pythagorean triplet for which a + b + c = n
    """
    for a in range(1, n//3):
        for b in range(a+1, n//2):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a*b*c

if __name__ == "__main__":
    print("Value of product of Pythagorean triplet for which a + b + c = 1000 is", product_of_pythagorean_triplet(1000))
