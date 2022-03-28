'''
Questions is: Finding the maximum and minimum element in an array.

It's a pretty easy question.
'''
#aprroach (1) - Iterative approach.
# Here, I would be using sliding window,
#1st variable at 1st index and 2nd variable at 2nd index of an array
# and increment the 1st and increment the 2nd while checking the condition.

#Code:

# def maxi_mini(A):
#     max=A[0]
#     min=A[0]
     
#     for i in range(1,n-1):
#         if max<A[i]:
#             max=A[i]
#         elif A[i]>min:
#             min=A[i]
#     return (min,max)

#approach(2) : Using Built-ins 
def maxi_mini(A):
    return (max(A),min(A))

#driver code
A=[1,2,3,5,1,3]
n=len(A)
print(maxi_mini(A))
# print(a,b)
        
