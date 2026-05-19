class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)        
        def getKthsmol(A,B,k):
            if len(A)>len(B):
                return getKthsmol(B,A,k)
            
            if A==[]:
                return B[k-1]
            if k==1:
                return min(A[0],B[0])
            i=min(len(A),k//2)
            j=min(len(B),k//2)
            if A[i-1]<B[j-1]:
                return getKthsmol(A[i:],B,k-i)
            else:
                return getKthsmol(A,B[j:],k-j)
        left=(m+n+1)//2
        right=(m+n+2)//2
        return (getKthsmol(nums1,nums2,left) + getKthsmol(nums1,nums2,right))/2.0

            
            
        

