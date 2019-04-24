#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(lis):
    n = len(lis)
    for i in range(0,n//2):
        if lis[i]!=lis[n-i-1]:
            return False
    return True

maxi = 0
for i in range(100,1000):
    for j in range(i,1000):
        if isPalindrome(str(i*j)) and (i*j)>maxi:
            maxi = i*j

print(maxi)
