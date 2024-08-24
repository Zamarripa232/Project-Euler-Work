# p0003.py
# Problem 0003
# Largest Prime Factor

# first step, what is a prime factor
# alright, so which prime numbers can multiply to make 600851475143
# Then figure out which is the biggest, return that value
# I don't need to reinvent the wheel here, I can google formulas
# and other people's code snippets!
#
# I made use of:
# https://stackoverflow.com/questions/32871539/integer-factorization-in-python


from math import gcd

target = 600851475143

def factorization(n):

    factors = []

    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for count in range(cycle_size):
                if factor > 1: break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)

            cycle_size *= 2
            x_fixed = x

        return factor

    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next

    return factors

print('Largest prime factor of target is ' + str(max(factorization(target))))
