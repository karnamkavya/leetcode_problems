class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #nums.sort()
        #return nums[len(nums)//2]
        c=0
        cand=0
        for num in nums:
            if c==0:
                cand=num
                c+=1
            elif num==cand:
                c+=1
            else:
                c-=1
        return cand