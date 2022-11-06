
def large_multiplication(n: str, m: int) -> str:
    carry: int = 0
    steps = 3
    new_number:str = ""
    for i in range(len(n), 0, -steps):
        low_index = 0
        if i - steps > 0:
            low_index = i - steps
        temp = int(n[low_index: i])*m + carry
        carry = temp//(10**steps)
        if low_index == 0:
            temp = str(temp)
        else:
            temp = str(format(temp%(10**steps), '0'+str(steps))) 
        new_number = temp+new_number

    return new_number


def routes_count(n: int, p: int) -> int:
    """
    Return the sum of the digits of the number n^p
    """
    num: str = str(n)
    for i in range(1, p):
        num = large_multiplication(num, n)
    total: int = 0
    for i in num:
        total = total + int(i)
    return total

if __name__ == "__main__":
    print("The sum of the digits of the number 2^1000 is", routes_count(2, 1000))
