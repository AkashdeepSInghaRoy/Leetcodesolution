class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)                                  #by comparing length of the list and the set we are deciding the ambiguity
        