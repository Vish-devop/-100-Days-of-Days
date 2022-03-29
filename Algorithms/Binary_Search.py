'''
Binary Search works on "sorted array"
so, if the array is not sorted then 1st sort the array then apply this algorithm.
Binary Search follows "Divide and conquer approach"
'''
'''
Algorithm:
1. Check if the left <= right:
2. #Base case: middle=left + (right-left)//2
3. Now, check if key is present at middle element -> return mid
4. After, that check if key is greater than mid element then,
decrement the right pointer by 1
5. If, the key is less than the middle element, then 
increment the left pointer by 1.
6. Until we find the middle element equals to key.
'''
# def binarySearch(arr, l, r, x):
# 	while l <= r:
# 		mid = l + (r - l) // 2
# 		# Check if x is present at mid
# 		if arr[mid] == x:
# 			return mid
# 		# If x is greater, ignore left half
# 		elif arr[mid] < x:
# 			l = mid + 1
# 		# If x is smaller, ignore right half
# 		else:
# 			r = mid - 1
# 	# If we reach here, then the element
# 	# was not present
# 	return -1

# # Driver Code
# arr = [2, 3, 4, 10, 40]
# x = 10
# # Function call
# result = binarySearch(arr, 0, len(arr)-1, x)

# if result != -1:
# 	print("Element is present at index -: % d " % result)
# else:
# 	print("Element is not present in array")


#Recusive approach:
def binarySearch(arr,l,r,key):
    if r>=l:
        mid=l+(r-l)//2

        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return binarySearch(arr,l,mid-1,key)
        elif arr[mid]<key:
            return binarySearch(arr,mid+1,r,key)
    else:
        return -1
    

#driver code
arr=[2,3,4,10,40]
key=10
result=binarySearch(arr,0,len(arr)-1,key)
if result != -1:
	print("Element is present at index -: % d " % result)
else:
	print("Element is not present in array")

