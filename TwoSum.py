class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        seen = {}
        
        
        for indicies,numbers in enumerate(nums):
            
            remainder = target - nums[indicies]
            
            if remainder in seen:
                return [indicies, seen[remainder]]
            
            else:
                seen[numbers] = indicies
            