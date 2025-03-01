class Solution:
    def getSecondLargest(self, arr):
        n=len(arr)
        if n<2:
            return -1
        first=second=float('-inf')
        for num in arr:
            if num> first:
                second=first
                first=num
            elif num > second and num!=first:
                second=num
        return second if second!=float('-inf') else -1