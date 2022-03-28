'''
Question: You need to sort an array consisting of only 0s,1s,and 2s
but, without using any sort algorithm, and sort function.

>> One more thing to keep in mind, is that the representation of the output arr should be in this form:
1st all 0s then followed by 1s and then 2s.
--------------------------------------------------------------------------------------------------------

e.g.->
Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Approach: 
1) Count the number of 0s, 1s, and 2s in the given array.
2) Then store the 0s in beginning followed by 1s and then 2s.
'''

#sort function
def sort_arr(arr,n):
    cnt0,cnt1,cnt2=0,0,0
    #counting 0s,1s,2s in array
    for i in range(n):
        if arr[i]==0:
            cnt0+=1
        elif arr[i]==1:
            cnt1+=1
        else:
            cnt2+=1
    i=0
    #store 0s in beginning followed by 1s and then 2s.
    while cnt0>0:
        arr[i]=0
        i+=1
        cnt0-=1
    while cnt1>0:
        arr[i]=1
        i+=1
        cnt1-=1
    while cnt2>0:
        arr[i]=2
        i+=1
        cnt2-=1
    Printarr(arr,n)

#utility function for print
def Printarr(arr,n):
    for i in range(n):
        print(arr[i],end=",")
#driver code
arr=[0,1,2,0,1,2]
n=len(arr)
sort_arr(arr,n)
