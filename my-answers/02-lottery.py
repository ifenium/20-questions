# Solution to Lottery

from random import randint
num1 = randint(0, 9)
num2 = randint(0, 9)
num3 = randint(0, 9)

input('Press any key: ')
result = [num1, num2, num3]
print('{} {} {}'. format(num1, num2, num3))

if 7 in result:
    print('"Congratulations!"')

# Variant-01

# Variant-02
