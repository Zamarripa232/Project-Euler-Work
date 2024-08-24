# p0001.py
# Problem 0001
# Multiples of 3 or 5

sum = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
print(sum)
