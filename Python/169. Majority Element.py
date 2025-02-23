class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num  # Set new candidate
            count += (1 if num == candidate else -1)

        return candidate  # Since majority element is guaranteed to exist

if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    a = Solution()
    k = a.majorityElement(nums)
    print(k)

