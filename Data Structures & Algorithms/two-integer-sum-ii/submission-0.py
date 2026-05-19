class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            val=target-numbers[i]
            low=0
            high=n-1
            while(low<=high):
                mid=(low+high)//2
                if mid!=i and numbers[mid]==val:
                    return [i+1,mid+1] if mid>i else [mid+1,i+1]
                elif numbers[mid]>val:
                    high=mid-1
                else:
                    low=mid+1
        

                
