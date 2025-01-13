class Solution(object):
    def abc(self, str):
        left = 0
        right = len(str)-1
        str1 = list(str)
        vowels = set('aeiouAEIOU')
        while left < right:
            while left< right and str1[left] not in vowels:
                left += 1
            while left< right and str1[right] not in vowels:

                right -= 1
            #if left < right:
            str1[left], str1[right] = str1[right], str1[left]
            left +=1
            right -=1


        return ''.join(str1)






if __name__=="__main__":
    str = "aleminopu"
    a=Solution()
    k=a.abc(str)
    print(k)