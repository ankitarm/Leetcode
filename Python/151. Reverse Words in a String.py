class Solution(object):
    def reversestring(self,s):
        '''s=s.strip()
        slist = list(s)
        words = []
        word=[]
        for i in range(len(slist)):
            if slist[i] != ' ':
                word.append(slist[i])
            elif word:
                words.append(''.join(word))
                word = []
        if word:
            words.append(''.join(word))
        left, right=0,len(words)-1
        while left<right:
            words[left], words[right]= words[right], words[left]
            left+=1
            right-=1
        return ' '.join(words)'''

        '''k = ' '.join(reversed(s.split()))
        print(k)'''

        splitedlist = s.split()
        reverslist = splitedlist[::-1]
        return ' '.join(reverslist)


if __name__ == "__main__":
    #string = "the sky is blue"
    #string = "    hello world     "
    string = "a good   example"
    a = Solution()
    k = a.reversestring(string)
    print(k)