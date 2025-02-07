def findRightMost1(n):
    # n ^ (n - 1) = zero everything else, rightmost 1 becomes 0, everything else becomes 1
    # n -> n - 1, rightmost 1 becomes 0, everything to the right becomes 1
    # n & (n ^ (n - 1)) -> binary number with only rightmost 1 set, everything else is 0
    
    return n & (n ^ (n - 1))

def findMSB(n):
    return (1 << n.bit_length()) - 1
    
def clearRightMost1(n):
    return n & n - 1

def setKthBit(n, k):
    return n | (1 << (k - 1))

def unsetKthBit(n, k):
    return n & ~(1 << (k - 1))

def toggleKthBit(n, k):
    return n ^ (1 << (k - 1))

def isPowerOfTwo(n):
    if n & (n - 1) == 0:
        return True
    else:
        return False
    
def findUniqueNumber(array):
    # IF NUMBERS ONLY REPEAT EVEN NUMBER OF TIMES
    # XOR all numbers in the sequence
    pass
    
    
def countSet(n):
    ans = n.bit_count()

    # alternatives:
    # bin(n), loop
    
    while n:
        ans += n & 1
        n >>= 1
        
    return ans

def has_even_parity (n):
    count = 0
    while n:
        count += n & 1
        n >>= 1 
    return count % 2 == 0

def clear_3rd_bit ( n):
    return n & ~( 1 << 3 )

def multiply_by_4 ( n):
    # return n << 1 + n # BUG : Incorrect operator precedence
    return n << 2