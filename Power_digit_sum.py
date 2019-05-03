# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

def exp(a,n):
    res = 1
    while n>0:
        if n&1==1:
            res *= a
        n = n>>1
        a *= a
    return res

def sum_of_digits_of_number(num):
    s = 0
    while num>0:
        s += num%10
        num //=10
    return s

print(sum_of_digits_of_number(exp(2,1000)))