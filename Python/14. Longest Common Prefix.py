class Solution(object):
    def longComPre(self, strs):
        if not strs:
            return ""

        for index, char in enumerate(strs[0]):
            for string in strs[1:]:
                if string[index] != char or index>=len(string):
                    return strs[0][:index]
        return str[0][:index]



if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    a = Solution()
    k = a.longComPre(strs)
    print(k)