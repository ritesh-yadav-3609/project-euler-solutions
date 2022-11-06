def minFlips(target):
 
    curr = '1'
    count = 0
     
    for i in range(len(target)):
        # If curr occurs in the final string
        if (target[i] == curr):
            count += 1
             
            # Switch curr to '0' if '1'
            # or vice-versa
            curr = chr(48 + (ord(curr) + 1) % 2)
     
    return count
 
# Driver Code
if __name__ == "__main__":
     
    S = "0101100"
     
    print(minFlips(S))