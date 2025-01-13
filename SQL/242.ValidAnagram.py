class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dic={}
        t_dic={}
        for value in s:
            s_dic[value]=s_dic.get(value,0)+1
        for value in t:
            t_dic[value] = t_dic.get(value,0)+1
        return s_dic==t_dic


if __name__=="__main__":
    s='anagram'
    t='nagaram'
    solution=Solution()
    a=solution.isAnagram(s,t)
    print(a)




