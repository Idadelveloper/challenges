class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        numbs = len(self.nums)
        count = 0
        result = []
        while count < numbs:
            for i in self.nums:
                if count == self.nums.index(i):
                    continue
                if self.nums[count] + i == self.target:
                    result = [count, self.nums.index(i)]
                    return result
            count += 1
        if len(result) < 2:
            result = None

        return result
        

example = Solution()
print(example.twoSum([3, 3], 6))