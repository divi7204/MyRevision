'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        for i in range(length):
            j = i+1
            try: 
                for j in range(length):
                    if nums[i]==nums[j]:
                        return True
            except:
                return False
obj = Solution()
print(obj.hasDuplicate([1,2,3,3]))