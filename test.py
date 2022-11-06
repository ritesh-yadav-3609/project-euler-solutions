def printLargestString(s):
    sorted(s, reverse=True)
    print(s)
    d = {}
    for i in s:
        if i in d.keys():
            d[i] = d[i]+1
        else:
            d[i] = 1
    for k in d.keys():
        print(k,d[k])



def output(s: str) -> int:
    one_count = 0
    zero_count = 0
    is_break = True
    for i,b in enumerate(s):
        if b == "0" and is_break:
            is_break = False
            one_count = one_count + 1
            if i<len(s)-1 and s[i+1]=='0':
                one_count = one_count + 1
        elif b == "1":
            is_break = True
    is_break = True
    for i,b in enumerate(s):
        if b == "1" and is_break:
            is_break = False
            zero_count = zero_count + 1
            if i<len(s)-1 and s[i+1]=='1':
                zero_count = zero_count + 1
        elif b == "0":
            is_break = True
    print("output", zero_count, one_count)
    return zero_count if zero_count < one_count else one_count


if __name__ == "__main__":
    s = "1100011"
    print(output(s))
    # test_count = int(input())
    # for i in range(0,test_count):
    #     test_case = input()
    #     print(output(test_case))
