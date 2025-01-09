class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0

        while i < len(word1) and i < len(word2):
            result.append(word1[i])
            result.append(word2[i])
            i += 1

        if i < len(word1):
            result.append(word1[i:])


        # elif i<len(word2):
        else:

            result.append(word2[i:])

        return "".join(result)


if __name__== "__main__":
    word1="abcfg"
    word2="pqr"
    a=Solution()
    ans=a.mergeAlternately(word1, word2)
    print(ans)