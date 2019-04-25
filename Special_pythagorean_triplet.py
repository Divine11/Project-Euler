# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from functools import reduce
lis = [(a,b,c) for a in range(1,500) for b in range(a+1,500) for c in range(b+1,500) if (a**2+b**2==c**2) and a+b+c==1000]
p = reduce((lambda x,y: x*y),lis)
print(p)