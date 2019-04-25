# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def get_sum_of_primes(num):
    is_prime = [True]*(num+1)
    is_prime[0] = False
    is_prime[1] = False
    p = 2
    summation = 0
    while p*p <=num:
        if is_prime[p]==True:
            #print(p)
            for i in range(p*p,num+1,p):
                is_prime[i]=False
        p+=1
    #print(is_prime)
    for i in range(2,num+1):
        if is_prime[i]==True:
            #print(i)
            summation+=i
    return summation

print(get_sum_of_primes(2000000))
        