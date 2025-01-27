class Solution(object):
    def maxvowels(self,s,k):
        vowels = ('aeiouAEIOU')
        curr_count = 0
        #counting vowel in first window
        for i in range(k):
            if s[i] in vowels:
                curr_count+=1
            max_vow = curr_count
        #loop from k to end keeping track of window
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr_count+=1
            if s[i-k] in vowels:
                curr_count-=1
            max_vow = max(curr_count,max_vow)
        return max_vow

if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    a = Solution()
    k = a.maxvowels(s, k)
    print(k)
