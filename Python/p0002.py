# p0002.py
# Problem 0002
# Even Fibonacci Numbers

termA = 1
termB = 2
termC = 0

# Starts at 2 since the loop begins with the
# third number in the sequence.
evenSum = 2

while termC < 4000000:
    termC = termA + termB
    
    # Check whether termC is even or not
    if termC % 2 == 0:
        evenSum += termC
    
    # Proceed with Fibonacci stuff
    termA = termB
    termB = termC

print(evenSum)