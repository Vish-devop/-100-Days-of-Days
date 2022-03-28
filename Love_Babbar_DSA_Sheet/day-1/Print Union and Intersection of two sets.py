'''
Question : Print the Union and Intersection of two sets.
'''
#Approach(1) : 
# To use in-built functions like union and intersectoin that only works on sets.
'''
arr1 = {7, 1, 5, 2, 3, 6} 
arr2 = {3, 8, 6, 20, 7}
print(arr1.union(arr2))
print('\n')
print(arr1.intersection(arr2))
'''

#Approach(2) - Hashing version
'''
Union:
1. Initialize the hash set hs.
2. Traverse the arr1 and copy all the elements of arr1 into hashset, and do same with arr2.
3. Print the set hs.

Intersection:
1. Intialize the hash set hs.
2. Traverse the arr1 and copy all the elements of arr1 into hash set.
3. For every element of x in arr2 do the following things:
3.1) Search x in hs, if x is present then print it.
'''
def printunion(arr1,arr2,n1,n2):
    hs=set()
    for i in range(0,n1):
        hs.add(arr1[i])
    for i in range(0,n2):
        hs.add(arr2[i])
    print("Union:")
    for i in hs:
        print(i,end=' ')

def intersection(arr1,arr2,n1,n2):
    hs=set()
    for i in range(0,n1):
        hs.add(arr1[i])
    print("\n Intersection:")
    for i in range(0,n2):
        if arr2[i] in hs:
            print(arr2[i],end=' , ')

#driver Code
arr1 = [7, 1, 5, 2, 3, 6] 
n1=len(arr1)
arr2 = [3, 8, 6, 20, 7]
n2=len(arr2)
printunion(arr1,arr2,n1,n2)
intersection(arr1,arr2,n1,n2)