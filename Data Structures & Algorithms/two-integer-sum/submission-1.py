class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, v in enumerate(nums):
            comp = target - v
            if comp in m:
                return [m[comp], i]
            m[v] = i
        return []
