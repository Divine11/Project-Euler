#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10001st prime number?

def isPrime(num):
    if num%2==0 or num%3==0:
        return False
    k = 5
    while k*k<=num:
        if num%k==0 or num%(k+2)==0:
            return False
        k += 6
    return True
    
prime_num = 2
i = 3
while prime_num<10001:
    if isPrime(i):
        prime_num+=1
    i=i+2
print(i-2)