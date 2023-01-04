class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            want = target - nums[i]  # 찾고싶은 숫자
            if want not in nums:
                continue

            elif i == nums.index(want):
                continue

            elif want in nums:
                want_idx = nums.index(want)  # 찾고싶은 숫자 인덱스
                if want_idx > i:
                    return [i, want_idx]
                else :
                    return [want_idx, i]
                break