class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
    
       # nums.sort()
        #return nums[len(nums)//3]
        c1=c2=0
        cand1=cand2=None
        for num in nums:
            if cand1==num:
                c1+=1
            elif cand2==num:
                c2+=1
            elif c1==0:
                cand1=num
                c1=1
            elif c2==0:
                cand2=num
                c2=1
            else:
                c1-=1
                c2-=1
        k=[]
        if nums.count(cand1)>len(nums)//3:
            k.append(cand1)
        if nums.count(cand2)>len(nums)//3:
            k.append(cand2)
        return k