'''
Question: Program to cyclically rotate an array by one

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}
'''

'''
Approach (1) :
1. Using slicing operator.
'''
# def rotate(arr):
#     arr[:]=arr[-1:]+arr[:-1]
#     print(arr)
'''
Approach (2):
2. Using sliding window.
a. Initializing the first and last pointer on array.
b. checking whether first != last pointer, if so then,
c. swap the first and last index of the array element 
and increment the i variable put on 1st index and j variable on last index will remain on its position.
'''
def rotate(arr,n):
    i=1
    j=n-1
    while i!=j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
    for i in range(0,n):
        print(arr[i],end=' ')

#driver Code
arr=[1,2,3,4,5]
n=len(arr)
rotate(arr,n)
# print(arr,n)