class Solution:
    result = []
    def arrayNesting(self, nums):
        self.nums = nums
        if len(self.result) == 0:
            self.result.append(self.nums[0])
        if self.nums[self.result[-1]] not in self.result:
            self.result.append(self.nums[self.result[-1]])
            self.arrayNesting(self.nums)
        return len(set(self.result))


example = Solution()
print(example.arrayNesting([0,1,2]))