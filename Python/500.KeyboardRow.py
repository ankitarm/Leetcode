
class Solution(object):
    def findWords(self, words):
        r1="qwertyuiop"
        r2="asdfghjkl"
        r3="zxcvbnm"
        result=[]
        for word in words:
            if word[0].lower() in r1:
                if all(x in r1 for x in word.lower()):
                    result.append(word)
            elif word[0].lower() in r2:
                if all(x in r2 for x in word.lower()):
                    result.append(word)
            elif word[0].lower() in r3:
                if all(x in r3 for x in word.lower()):
                    result.append(word)
        return result  

if __name__ == "__main__":
    words = ["Hello","Alaska","Dad","Peace"]
    a=Solution()
    k=a.findWords(words)
    print(k)