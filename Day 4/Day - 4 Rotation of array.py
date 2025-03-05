class Solution:
    def rotateArr(arr,d):
        n=len(arr)
        
        for i in range(d):
            first=arr[0]
        for j in range(n-1):
            arr[j]=arr[j+1]
            arr[n-1]=first