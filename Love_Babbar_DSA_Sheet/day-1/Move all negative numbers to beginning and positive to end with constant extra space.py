'''
Question: Move all negative numbers to beginning and positive to end with constant extra space

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5

'''

'''
Approach(1):
a) Using pivot element seperation of quckSort
'''
'''
Approach(2):
a) Using 2-pointers
i. Put left and right pointer on index 0 and last index of array.
ii. Check if left and right pointers are -ve and +ve then simply increment left pointer.
iii. Check if left element is +ve and right element is -ve then simply swap the elements and simultanesouly increment and decrement the leftand right pointers.
iv. Else if left element is +ve and right element is also +ve, then simply decrement right pointer.
v. Repeat above steps until left<=right pointer.
'''
def shiftall(A,left,right):
    while left<=right:
        if A[left]<0 and A[right]<0:
            left+=1
        elif A[left]>0 and A[right]<0:

            A[left],A[right]=A[right],A[left]
            left+=1
            right-=1
        elif A[left]>0 and A[right]>0:
            right-=1
        else:
            left+=1
            right-=1

def print_arr(A,n):
    for i in range(0,n):
        print(A[i],end='->') 

# def sortall(A,n):
#     j=0
#     for i in range(0,n):
#         if A[i]<0:
#             temp=A[i]
#             A[i]=A[j]
#             A[j]=temp
#             j+=1
#     print(A)
#driver Code
A=[-12,11,-13,-5,6,-7,5,-3,-6]
n=len(A)
shiftall(A,0,n-1)
print_arr(A,n)
# sortall(A,n)

