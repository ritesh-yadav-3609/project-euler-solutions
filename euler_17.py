
def number_word(n: int, index: int) -> str:
    dictianry = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}
    postfix = ["", "", "", "Hundredand", "Thousandand", "Thousandand", "Lakh"]
    postfix[index]
    return dictianry[n]+postfix[index]


def letters_count_of_sequence(n: int) -> int:
    """
    Return the number of letters would be used in all the numbers from 1 to n
    """
    num = n
    dic = {0:0, 1:0, 2:0, 3:0, 4:0}
    count = 0
    start = steps = 1
    while start <= n:
        temp = 0
        if 20 <= start and start < 100:
            steps = 10
            temp = len(number_word(start, len(str(steps))))
        elif 100 <= start:
            steps = 10**(len(str(start))-1)
            temp = len(number_word(start//steps, len(str(steps)))) - 3
        index = len(str(steps))

        if 20 <= start and start+steps > n:
            count = count + temp
            print(start, temp, count)
            n = n%(steps)
            steps = steps//10
            if start < 20:
                steps=1
            start = steps
            continue
        elif start < 100:
            count = count + len(number_word(start,index))*steps + dic[index-1]
        else:
            count = count + len(number_word(start//steps,index))*steps + dic[index-1] - 3
        
        if not (10 <= start and start <= 20) and num == n:
            dic[index] = count
        
        if start < 100:
            print(number_word(start,index))
        else:
            print(number_word(start//steps,index))
        start = start + steps

    return count

if __name__ == "__main__":
    print("The number of letters would be used in all the numbers from 1 to 1000 (one thousand) inclusive were written out in words is", \
    letters_count_of_sequence(100000))
