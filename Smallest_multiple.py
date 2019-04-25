#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#this method is used to find gcd
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
#this method is used to find lcm
def lcm(a,b):
    return (a*b)//gcd(a,b)

lc = 2520
for i in range(11,21):
    lc = lcm(lc,i)

print(lc)


