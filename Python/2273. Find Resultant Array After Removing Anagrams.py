class Solution:
    def removeAnagrams(self, words: [str]) -> [str]:
        resultlist=[words[0]]
        for word in range(1,len(words)):
            if sorted(words[word])!= sorted(resultlist[-1]):
                resultlist.append(words[word])
        return resultlist

if __name__=="__main__":
    words = ["abba", "baba", "bbaa", "cd", "cd"]
    solution=Solution()
    a=solution.removeAnagrams(words)
    print(a)
