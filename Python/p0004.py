# p0004.py
# Problem 0004
# Largest Palindrome Product
#
# tl;dr Find the largest palindrome made from
# the product of two 3-digit numbers.

pdList = []

def isPalindrome(n):
    '''Checks if a number can be read both directions'''

    ## turns out I could have also did list[::-1]
    flipN = list(str(n))
    flipN.reverse()
    flipN = int(''.join(flipN))
    return n == flipN

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if isPalindrome(product):
            pdList.append(product)
print(max(pdList))
