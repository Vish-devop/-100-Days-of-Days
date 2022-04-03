'''
Largest palindromic number in an array
#easy #gfg


Given an array of non-negative integers arr[].
The task is to find the largest number in the array 
which is palindrome. If no such number exits then print -1.

Input: arr[] = {1, 232, 54545, 999991}; 
Output: 54545

Input: arr[] = {1, 2, 3, 4, 5, 50}; 
Output: 5 
'''

'''
Approach: 
1.Sort the array in asc order.
2. Start traversing the array from the end.
3. The first number which is a palindrome is the required answer.
4. If no palidromic number is found then print -1.

'''

from unicodedata import name

from pip import main


def isPalindrome(n):
    #Finding the divisort to extract the leading digit.
    divisor=1
    while n/divisor>=10:
        divisor*=10
    while n!=0:
        leading=n//divisor
        trailing=n%10

    #if first and last digits are not same
    #then, return false.
        if leading!=trailing:
            return False
    #Removing the leading and trailing digits from 
    #the number.
        n=n%divisor//10
    #Reducing divisor by a factor of 2 as 2 digits are dropped.
        divisor//=100
    return True

def largestPalindrome(A,n):
    A.sort()
    for i in range(n-1,-1,-1):
        if isPalindrome(A[i]):
            return A[i]
    return -1

#driver code
if __name__=="__main__":
    A=[1,232,54545,999991]
    n=len(A)

    print(largestPalindrome(A,n))