class Solution(object):
    def issubseq(self,s,t):
        i = 0
        j = 0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        return i == len(s)



if __name__ == "__main__":
    s = "abc"
    t = "kahbgdc"
    a = Solution()
    k = a.issubseq(s, t)
    print(k)