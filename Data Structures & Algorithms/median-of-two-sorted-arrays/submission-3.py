class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)       
        def median(a,b):
            # if  a==[]:
            #     return b[0]
            if len(a)>len(b):
                return median(b,a)
            low=0
            n=len(a)+len(b)
            left=(n+1)//2
            high=len(a)
            # print(left)
            while(low<=high):
                mid1=(low+high)//2
                mid2=left-mid1
                l1,l2=float('-inf'),float('-inf')
                r1,r2=float('inf'),float('inf')
                # print(low,high,mid1)
                if mid1<len(a):
                    r1=a[mid1]
                if mid2<len(b):
                    r2=b[mid2]
                if mid1-1>=0:
                    l1=a[mid1-1]
                if mid2-1>=0:
                    l2=b[mid2-1]
                
                if l1<=r2 and l2<=r1:
                    if n%2!=0:
                        return max(l1,l2)
                    else:
                        return (max(l1,l2)+min(r1,r2))/2.0
                elif(l1>r2):
                    high=mid1-1
                elif l2>r1:
                    low=mid1+1
            return 0
        return median(nums1,nums2)


            
            
        

