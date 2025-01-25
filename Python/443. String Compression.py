class Solution(object):
    def strincomp(self,chars):
        write = 0
        read = 0
        #LOOP for iterating through chars
        while read < len(chars):
            count = 0
            char = chars[read]  #putting 1st char in char
            #keep looping for same char and increment count and loop
            while read < len(chars) and chars[read] == char:
                read+=1
                count+=1
            #ones all same char count is done write char at write index and increment write to writ count
            chars[write] = char
            write+=1
            #handling multiple digits
            if count>1:
                for digit in str(count): #converting count to string, 12 to '12'
                    chars[write]=digit
                    write+=1
        return write




                




if __name__=="__main__":
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    a = Solution()
    k = a.strincomp(chars)
    print(k)