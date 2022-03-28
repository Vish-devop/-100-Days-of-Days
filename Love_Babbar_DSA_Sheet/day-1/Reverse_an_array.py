#Question:
'''
Given an array A of size N, print the reverse of it.

Input:
First line contains an integer denoting the test cases 'T'. T testcases follow. Each testcase contains two lines of input. First line contains N the size of the array A. The second line contains the elements of the array.

Output:
For each testcase, in a new line, print the array in reverse order.

Constraints:
1 <= T <= 100
1 <= N <=100
0 <= Ai <= 100

Example:
Input:
1
4
1 2 3 4
Output:
4 3 2 1
'''

#approach (1) - Iterative approach

# def reverseList(A,start,end):
#     while start<end:
#         A[start],A[end]=A[end],A[start]
#         start+=1
#         end-=1

#approach (2) - Recursive approach
# def reverseList(A,start,end):
#     if start>end:
#         return
#     A[start],A[end]=A[end],A[start]
#     reverseList(A,start+1,end-1)

#approach(3) - Using slicing operator
def reverseList(A):
    print(A[::-1])
#driver code
A=[1,2,3,4]
reverseList(A)
print(A)

