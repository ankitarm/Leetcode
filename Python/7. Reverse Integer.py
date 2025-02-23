class Solution(object):
    def reverseInt(self,num):
        '''
        sign = -1 if num < 0 else 1
        num = abs(num)
        reverse_num = 0
        while num != 0:
            digit = num % 10
            num = num // 10
            reverse_num = reverse_num*10 + digit
            if reverse_num > 2**31 -1 or reverse_num < -2**31:
                return 0
        return sign * reverse_num
        '''
        if num < 0:
            reverse_num = int(str(num)[1:][::-1])*-1
        else:
            reverse_num = int(str(num)[::-1])
        if reverse_num > 2 ** 31 - 1 or reverse_num < -2 ** 31:
            return 0
        return reverse_num


if __name__ == "__main__":
    num = -123
    a = Solution()
    k = a.reverseInt(num)
    print(k)
