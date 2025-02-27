from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.cumsum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.cumsum[i+1] = self.cumsum[i] + nums[i]
        print(self.cumsum)

    def sumRange(self, left: int, right: int) -> int:
        return self.cumsum[right + 1] - self.cumsum[left]

# Example usage:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left, right)


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)

print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)