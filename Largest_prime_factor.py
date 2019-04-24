#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def isPrime(num):
    if num<=1:
        return False
    if num<=3:
        return True
    if num%2==0 or num%3==0:
        return False
    k =5
    while k*k<=num:
        if num%k==0 or num%(k+2)==0:
            return False
        k += 6
    return True

for i in range(2,12784073939):
    if 600851475143%i==0 and isPrime((600851475143//i)):
        print(600851475143//i)
        break
