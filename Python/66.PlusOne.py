class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits)==0:
            return [1] 
        if digits[-1] != 9 :
            digits[-1]+= 1
            return digits
        else:
            digits=self.plusOne(digits[:-1])
            digits.append(0)
            return digits



if __name__ == "__main__":
    digits=[4,3,2,1]
    a=Solution()
    i=a.plusOne(digits)
    print(i)