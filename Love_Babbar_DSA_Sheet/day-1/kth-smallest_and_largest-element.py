'''
Question: Find the kth largest and smallest element present in an array.

arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.

Approaches could be many to solve this question.
(1) simple sorting 
(2) using max-heap or min-heap
(3) using quick sort
(4) Hashmap 

'''

#I am using sorting approach, and the T.C. = )(nlogn) >> This is only the time_complexity of sorting the arrays.
#kth-smallest element from an array.
def kthSmallest(A):
    A.sort()  
    return A[k-1]

def kthLargest(A):
    A.sort(reverse=True) #sorting the array into descending order. 
    return A[k-1]
#driver_code
A=[7,10,4,3,20,15]
k=3
# kthSmallest()
print(kthSmallest(A))
print(kthLargest(A))