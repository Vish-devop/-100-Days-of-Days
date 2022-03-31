'''
Question: Given heights of n towers and a value k.
We need to either increase or decrease the height of every tower by k
where k>0. The task is to minimize the difference between the heights of the longest
and the shortest tower after modifications and output this difference.


e.g.->
i/p: arr[]={1,15,10}, and k=6
o/p: 5 (maximum dufference)
'''
# asked in adobe.

'''
Algorithm: 
1. sort the array and make each height of tower maximum.
2. We do this by decreasing the height of all the towers 
towards the right by k and increasing all the heights of the towers 
towards the left by k.
3. Now, check whether it has the maximum height or not by comparing it with the last element towards the right side 
which is a[n]-k. 
4. Since, the array is sorted if the tower's height is greater than the a[n]-k, then it's the tallest tower available.

'''
def mindiff(arr,n,k):
    arr.sort()
    ans=arr[n-1]-arr[0] #maximum possible height difference.

    tempmin=arr[0]
    tempmax=arr[n-1]

    for i in range(1,n):
        tempmin=min(arr[0]+k,arr[i]-k)

        #Minimum element when we add k to whole array
        #Maximum element when we substract k from whole array
        tempmax=max(arr[i-1]+k,arr[n-1]-k)
        ans=min(ans,tempmax-tempmin)
    return ans

#Driver code
k=6
n=6
arr=[7,4,8,8,8,9]
ans=mindiff(arr,n,k)
print("maximum height is: ",ans)