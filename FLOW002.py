def reverseBits(n) :
    rev = 0
     
  
    while (n > 0) :


 
     # bitwise left shift 'rev' by 1
        rev = rev << 1
 
     # if current bit is '1'
        if (n & 1 == 1) :


            rev = rev ^ 1
 
     # bitwise right shift 'n' by 1
        n = n >> 1
     
     # required number
    return rev
     
# function to check whether binary
# representation of a number is
# palindrome or not
def isPalindrome(n) :
 
    # get the number by reversing
    # bits in the binary
    # representation of 'n'
    rev = reverseBits(n)
 
    return (n == rev)
 
def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)  
# Driver program to test above

if __name__ == "__main__":
    t= int(input())
    for i in range(t):
        a=int(input())
        c=str(input())
        n=binaryToDecimal(c)
        if (isPalindrome(n)) :
            print("Yes")
        else :
            print("No")